from django.shortcuts import render, redirect
from .forms import BuscaBPCForm, get_estados  # Importe get_estados
import requests
import json
from django.http import JsonResponse

def formulario_busca(request):
    form = BuscaBPCForm()
    return render(request, 'busca_bpc/formulario_busca.html', {'form': form})

def exibir_resultados(request):
    if request.method == 'POST':
        form = BuscaBPCForm(request.POST)
        if form.is_valid():
            codigo_ibge = form.cleaned_data['cidades']  # Agora o código IBGE vem do campo 'cidades'
            mes_ano = form.cleaned_data['mes_ano']

            api_key = 'c3c3c3a4b29eb4d051ec092c74825e2e'  # Substitua pela sua chave real
            headers = {'chave-api-dados': api_key}
            url_api = f'https://api.portaldatransparencia.gov.br/api-de-dados/bpc-por-municipio?codigoIbge={codigo_ibge}&mesAno={int(mes_ano)}&pagina=1'

            try:
                response_api = requests.get(url_api, headers=headers)
                response_api.raise_for_status()
                data_api = response_api.json()

                # Adicionando informações de estado e município para exibir no resultado
                estado_sigla = form.cleaned_data['estados']
                # Buscar os municípios do estado selecionado
                municipios_do_estado = []
                cidades_response = requests.get(
                    f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{estado_sigla}/municipios"
                )
                if cidades_response.status_code == 200:
                    municipios_do_estado = cidades_response.json()
                municipio_nome = ''
                for cidade in municipios_do_estado:
                    if str(cidade['id']) == str(codigo_ibge):
                        municipio_nome = cidade['nome']
                        break
                estado_nome = ''
                for sigla, nome in get_estados():
                    if sigla == estado_sigla:
                        estado_nome = nome
                        break

                return render(request, 'busca_bpc/resultados_bpc.html', {
                    'resultados': data_api,
                    'codigo_ibge': codigo_ibge,
                    'mes_ano': mes_ano,
                    'estado': estado_nome,
                    'cidade': municipio_nome,
                })

            except requests.exceptions.RequestException as e:
                erro = f"Erro ao acessar a API: {e}"
                return render(request, 'busca_bpc/erro_bpc.html', {'erro': erro})
            except json.JSONDecodeError:
                erro = "Erro ao decodificar a resposta da API."
                return render(request, 'busca_bpc/erro_bpc.html', {'erro': erro})
        else:
            return render(request, 'busca_bpc/formulario_busca.html', {'form': form, 'erro_form': 'Por favor, corrija os erros no formulário.'})
    else:
        return redirect('formulario_busca')

def get_cidades_por_estado(request, sigla_estado):
    url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{sigla_estado}/municipios"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        cidades = [{'nome': cidade['nome'], 'codigo_ibge': str(cidade['id'])} for cidade in sorted(data, key=lambda x: x['nome'])]
        return JsonResponse(cidades, safe=False)
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar cidades do estado {sigla_estado}: {e}")
        return JsonResponse([], safe=False) 