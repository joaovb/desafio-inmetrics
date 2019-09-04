Feature: Realizar a compra de um produto no site

    '''Funcionalidade para realizar a compra de um produto no site'''

    Scenario: Comprar produto sem preencher cidade e estado
        Given escolho produto para realizar compra
        When realizo o checkout no site 
        Then devo receber alerta para preencher cidade e estado   
