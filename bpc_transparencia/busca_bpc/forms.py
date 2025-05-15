from django import forms
import requests

def get_estados():
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        estados = [(estado['sigla'], estado['nome']) for estado in sorted(data, key=lambda x: x['nome'])]
        estados.insert(0, ('', 'Selecione o Estado'))  # Adiciona uma opção inicial vazia
        return estados
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar estados da API do IBGE: {e}")
        return [('', 'Erro ao carregar estados')]

def get_cidades_por_estado(sigla_estado):
    if not sigla_estado:
        return [('', 'Selecione o Município')]
    url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{sigla_estado}/municipios"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        cidades = [(str(cidade['id']), cidade['nome']) for cidade in sorted(data, key=lambda x: x['nome'])]
        cidades.insert(0, ('', 'Selecione o Município')) # Adiciona uma opção inicial vazia
        return cidades
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar cidades do estado {sigla_estado}: {e}")
        return [('', 'Erro ao carregar municípios')]

class BuscaBPCForm(forms.Form):
    estados = forms.ChoiceField(
        label='Estado',
        choices=get_estados(),
        required=True
    )
    cidades = forms.ChoiceField(
        label='Município',
        choices=[('', 'Selecione o Município')],
        required=True
    )
    mes_ano = forms.CharField(
        label='Mês e Ano (AAAAMM)',
        max_length=6,
        widget=forms.TextInput(attrs={'placeholder': 'Ex: 202412'}),
        required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'estados' in self.data and self.data['estados']:
            sigla_estado = self.data['estados']
            self.fields['cidades'].choices = get_cidades_por_estado(sigla_estado)
        else:
            self.fields['cidades'].choices = [('', 'Selecione o Município')]

    def clean_mes_ano(self):
        mes_ano = self.cleaned_data['mes_ano']
        if not mes_ano.isdigit() or len(mes_ano) != 6:
            raise forms.ValidationError("Formato inválido. Use AAAAMM (ex: 202412).")
        return mes_ano

    def clean(self):
        cleaned_data = super().clean()
        estado = cleaned_data.get('estados')
        cidade = cleaned_data.get('cidades')

        if not estado or estado == '':
            self.add_error('estados', 'Selecione um estado.')
        if not cidade or cidade == '':
            self.add_error('cidades', 'Selecione um município.')

        return cleaned_data