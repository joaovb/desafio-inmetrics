@given(u'escolho produto para realizar compra')
def step_impl(context):
    context.page.home_page()
    context.page.seleciona_produto()
    


@when(u'realizo o checkout no site')
def step_impl(context):
    context.page.preenche_informacoes()


@then(u'devo receber alerta para preencher cidade e estado')
def step_impl(context):
    context.page.exibe_alerta()

    
    