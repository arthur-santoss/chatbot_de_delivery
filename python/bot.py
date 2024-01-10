import editacodigo_whats
import time
import os

#PUXA AS CONFIGURAÇÕES INICIAIS
bolinha_notificacao, contato_cliente, caixa_msg, msg_cliente,caixa_de_pesquisa,pega_contato = editacodigo_whats.obter_configuracoes_whatsapp('SUA-CHAVE-AQUI')

####CARREGAR NAVEGADOR
driver = editacodigo_whats.carregar_pagina_whatsapp('zap/sessao','https://web.whatsapp.com/')

time.sleep(120)

