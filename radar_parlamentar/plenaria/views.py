# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from modelagem import models
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from modelagem import utils 
from . import serializer


def plenaria(request, nome_curto_casa_legislativa, cod_proposicao):
    casa_legislativa = \
        get_object_or_404(models.CasaLegislativa,
                          nome_curto=nome_curto_casa_legislativa)
    return render_to_response(
        'votacao.html',
        {
            'casa_legislativa': casa_legislativa,
            'cod_proposicao': cod_proposicao,
        },
        context_instance=RequestContext(request)
    )



def json_proposicao(request, nome_curto_casa_legislativa, cod_proposicao):
    """Retorna o JSON com os dados de todas as votações de uma proposição."""
    proposicao = get_object_or_404(
        models.Proposicao, id=cod_proposicao)
    proposicao_serializer = serializer.ProposicaoSerializer()
    dados = proposicao_serializer.get_json_proposicao(proposicao)
    return HttpResponse(dados, mimetype='application/json')