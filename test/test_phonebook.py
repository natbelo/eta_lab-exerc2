from src.phonebook import Phonebook

class TestPhonebook:

    #def test_add(self):
        #assert False
    def test_add_validit(self):
        #setup
        phonebook = Phonebook()
        nome_valido = 'Maria'
        numero_valido = '5325'
        resultado_esperado = 'Número adicionado'

        #chamada
        resultado = phonebook.add(nome_valido, numero_valido)

        #validação
        assert resultado == resultado_esperado
        assert phonebook.entries.keys().__contains__(nome_valido)
        assert phonebook.entries.get(nome_valido) == numero_valido

    def test_add_invalidit1(self):
        # setup
        phonebook = Phonebook()
        nome_invalido = 'Maria#'
        numero_valido = '5325'
        resultado_esperado = 'Nome inválido'

        # chamada
        resultado = phonebook.add(nome_invalido, numero_valido)

        # validação
        assert resultado == resultado_esperado

    def test_add_invalidit2(self):
        # setup
        phonebook = Phonebook()
        nome_invalido = 'Maria@'
        numero_valido = '5325'
        resultado_esperado = 'Nome inválido'

        # chamada
        resultado = phonebook.add(nome_invalido, numero_valido)

        # validação
        assert resultado == resultado_esperado

    def test_add_invalidit3(self):
        # setup
        phonebook = Phonebook()
        nome_invalido = 'Maria!'
        numero_valido = '5325'
        resultado_esperado = 'Nome inválido'

        # chamada
        resultado = phonebook.add(nome_invalido, numero_valido)

        # validação
        assert resultado == resultado_esperado

    def test_add_invalidit4(self):
        # setup
        phonebook = Phonebook()
        nome_invalido = 'Maria$'
        numero_valido = '5325'
        resultado_esperado = 'Nome inválido'

        # chamada
        resultado = phonebook.add(nome_invalido, numero_valido)

        # validação
        assert resultado == resultado_esperado

    def test_add_invalidit5(self):
        # setup
        phonebook = Phonebook()
        nome_invalido = 'Maria%'
        numero_valido = '5325'
        resultado_esperado = 'Nome inválido'

        # chamada
        resultado = phonebook.add(nome_invalido, numero_valido)

        # validação
        assert resultado == resultado_esperado

    def test_add_invalidit6(self):
        # setup
        phonebook = Phonebook()
        nome_invalido = 'Maria%'
        numero_valido = '5325'
        resultado_esperado = 'Nome inválido'

        # chamada
        resultado = phonebook.add(nome_invalido, numero_valido)

        # validação
        assert resultado == resultado_esperado

    def test_add_invalidit7(self):
        # setup
        phonebook = Phonebook()
        nome_valido = 'Maria'
        numero_invalido = ''
        resultado_esperado = 'Número inválido'

        # chamada
        resultado = phonebook.add(nome_valido, numero_invalido)

        # validação
        assert resultado == resultado_esperado

    def test_lookup_validit(self):
        # setup
        phonebook = Phonebook()
        phonebook.add("Fernanda", "987654321")
        phonebook.add("Carla", "8987654321")
        phonebook.add("Andrea", "9876543219")
        phonebook.add("Willams", "777654321")

        nome_valido = 'Fernanda'
        numero_esperado = '987654321'

        # chamada
        resultado = phonebook.lookup(nome_valido)

        # validação
        assert resultado == numero_esperado

    def test_lookup_invalidit1(self):
        # setup
        phonebook = Phonebook()
        phonebook.add("Fernanda", "987654321")

        nome_invalido = 'Fernanda#'
        mensagem_esperada = 'Nome inválido'

        # chamada
        resultado = phonebook.lookup(nome_invalido)

        # validação
        assert resultado == mensagem_esperada

    def test_lookup_invalidit2(self):
        # setup
        phonebook = Phonebook()
        phonebook.add("Fernanda", "987654321")

        nome_invalido = 'Fernanda@'
        mensagem_esperada = 'Nome inválido'

        # chamada
        resultado = phonebook.lookup(nome_invalido)

        # validação
        assert resultado == mensagem_esperada

    def test_lookup_invalidit3(self):
        # setup
        phonebook = Phonebook()
        phonebook.add("Fernanda", "987654321")

        nome_invalido = 'Fernanda!'
        mensagem_esperada = 'Nome inválido'

        # chamada
        resultado = phonebook.lookup(nome_invalido)

        # validação
        assert resultado == mensagem_esperada

    def test_lookup_invalidit4(self):
        # setup
        phonebook = Phonebook()
        phonebook.add("Fernanda", "987654321")

        nome_invalido = 'Fernanda$'
        mensagem_esperada = 'Nome inválido'

        # chamada
        resultado = phonebook.lookup(nome_invalido)

        # validação
        assert resultado == mensagem_esperada

    def test_lookup_invalidit5(self):
        # setup
        phonebook = Phonebook()
        phonebook.add("Fernanda", "987654321")

        nome_invalido = 'Fernanda%'
        mensagem_esperada = 'Nome inválido'

        # chamada
        resultado = phonebook.lookup(nome_invalido)

        # validação
        assert resultado == mensagem_esperada

    def test_get_names(self):
        # setup
        phonebook = Phonebook()
        phonebook.add("Fernanda", "987654321")
        phonebook.add("Carla", "8987654321")
        phonebook.add("Andrea", "9876543219")
        phonebook.add("Willams", "777654321")

        resultado_esperado = ["POLICIA", "Fernanda", "Carla", "Andrea", "Willams"]


        # chamada
        resultado = phonebook.get_names()

        # validação
        assert resultado == resultado_esperado

    def test_get_numbers(self):
        # setup
        phonebook = Phonebook()
        phonebook.add("Fernanda", "987654321")
        phonebook.add("Carla", "8987654321")
        phonebook.add("Andrea", "9876543219")
        phonebook.add("Willams", "777654321")

        resultado_esperado = ["190", "987654321", "8987654321", "9876543219", "777654321"]


        # chamada
        resultado = phonebook.get_numbers()

        # validação
        assert resultado == resultado_esperado


