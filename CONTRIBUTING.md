# Contribuindo para o JALS

Obrigado por seu interesse em contribuir para o JALS (Journey Amplified Language Systems)! Este documento fornece diretrizes para contribuições ao projeto.

## 🌟 Como Contribuir

Existem várias maneiras de contribuir para o JALS:

- 🐛 **Reportar bugs**
- 💡 **Sugerir novas funcionalidades**
- 📝 **Melhorar a documentação**
- 🔧 **Contribuir com código**
- 🧪 **Escrever testes**
- 🎨 **Melhorar a interface**
- 📊 **Contribuir com dados de exemplo**

## 🚀 Primeiros Passos

### 1. Fork do Repositório

```bash
# Clone seu fork
git clone https://github.com/SEU_USUARIO/JALS.git
cd JALS

# Adicione o repositório original como upstream
git remote add upstream https://github.com/guilherme-machado-ceo/JALS.git
```

### 2. Configuração do Ambiente

```bash
# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt
pip install -e .

# Instale dependências de desenvolvimento
pip install pytest black flake8 jupyter
```

### 3. Execute os Testes

```bash
# Execute todos os testes
pytest

# Execute com cobertura
pytest --cov=src

# Execute testes específicos
pytest tests/test_core.py
```

## 📋 Processo de Contribuição

### 1. Crie uma Branch

```bash
# Mantenha sua branch main atualizada
git checkout main
git pull upstream main

# Crie uma nova branch para sua contribuição
git checkout -b feature/nome-da-funcionalidade
# ou
git checkout -b bugfix/nome-do-bug
# ou
git checkout -b docs/melhoria-documentacao
```

### 2. Faça suas Alterações

- Siga as [diretrizes de código](#diretrizes-de-código)
- Adicione testes para novas funcionalidades
- Atualize a documentação conforme necessário
- Mantenha commits pequenos e focados

### 3. Teste suas Alterações

```bash
# Execute os testes
pytest

# Verifique o estilo do código
flake8 src tests

# Formate o código
black src tests
```

### 4. Commit e Push

```bash
# Adicione suas alterações
git add .

# Faça commit com mensagem descritiva
git commit -m "feat: adiciona funcionalidade X para Layer 2"

# Push para seu fork
git push origin feature/nome-da-funcionalidade
```

### 5. Abra um Pull Request

1. Vá para o repositório no GitHub
2. Clique em "New Pull Request"
3. Selecione sua branch
4. Preencha o template de PR
5. Aguarde a revisão

## 📝 Diretrizes de Código

### Estilo de Código

- **Python**: Seguimos PEP 8
- **Formatação**: Usamos `black` para formatação automática
- **Linting**: Usamos `flake8` para verificação de estilo
- **Docstrings**: Usamos formato Google/NumPy

### Exemplo de Docstring

```python
def process_linguistic_unit(unit: Dict[str, Any], config: Optional[Dict] = None) -> Dict[str, Any]:
    """
    Processa uma unidade linguística através das camadas do JALS.
    
    Args:
        unit: Dicionário contendo dados da unidade linguística
        config: Configurações opcionais para processamento
        
    Returns:
        Dicionário com a unidade processada
        
    Raises:
        ValueError: Se a unidade não contém dados válidos
        
    Example:
        >>> unit = {'id': 1, 'type': 'morpheme', 'data': [...]}
        >>> result = process_linguistic_unit(unit)
        >>> print(result['processed'])
        True
    """
```

### Convenções de Nomenclatura

- **Classes**: PascalCase (`CoreIdeogram`, `AmplificationEngine`)
- **Funções/Métodos**: snake_case (`extract_features`, `build_network`)
- **Variáveis**: snake_case (`linguistic_units`, `symbol_data`)
- **Constantes**: UPPER_SNAKE_CASE (`MAX_ITERATIONS`, `DEFAULT_CONFIG`)

## 🧪 Escrevendo Testes

### Estrutura de Testes

```python
import pytest
from src.core import CoreIdeogram

class TestCoreIdeogram:
    """Testes para o Core Ideogram."""
    
    def setup_method(self):
        """Configuração executada antes de cada teste."""
        self.ideogram = CoreIdeogram()
        
    def test_initialization(self):
        """Testa inicialização correta."""
        assert self.ideogram.data is not None
        assert 'strokes' in self.ideogram.data
        
    def test_feature_extraction(self):
        """Testa extração de características."""
        # Arrange
        test_data = {'strokes': [{'id': 1, 'points': [[0, 0], [1, 1]]}]}
        self.ideogram.data = test_data
        
        # Act
        features = self.ideogram.extract_features()
        
        # Assert
        assert 'geometric' in features
        assert 'kinematic' in features
```

### Cobertura de Testes

- Mantenha cobertura > 80%
- Teste casos de sucesso e falha
- Inclua testes de integração
- Teste casos extremos

## 📚 Documentação

### Tipos de Documentação

1. **Docstrings**: Para funções e classes
2. **README**: Visão geral e instruções básicas
3. **Tutoriais**: Guias passo-a-passo
4. **API Reference**: Documentação técnica detalhada
5. **Whitepaper**: Fundamentação teórica

### Atualizando Documentação

- Mantenha documentação sincronizada com código
- Use exemplos práticos
- Inclua diagramas quando apropriado
- Traduza para português quando possível

## 🐛 Reportando Bugs

Use o template de issue para bugs:

1. **Descrição clara** do problema
2. **Passos para reproduzir**
3. **Comportamento esperado vs atual**
4. **Ambiente** (OS, Python version, etc.)
5. **Logs de erro** se disponíveis

## 💡 Sugerindo Funcionalidades

Use o template de feature request:

1. **Problema** que a funcionalidade resolve
2. **Solução proposta**
3. **Alternativas consideradas**
4. **Contexto adicional**

## 🏷️ Convenções de Commit

Usamos [Conventional Commits](https://www.conventionalcommits.org/):

```
<tipo>[escopo opcional]: <descrição>

[corpo opcional]

[rodapé opcional]
```

### Tipos de Commit

- `feat`: Nova funcionalidade
- `fix`: Correção de bug
- `docs`: Mudanças na documentação
- `style`: Formatação, sem mudança de código
- `refactor`: Refatoração de código
- `test`: Adição ou correção de testes
- `chore`: Tarefas de manutenção

### Exemplos

```bash
feat(layer2): adiciona abstração simbólica avançada
fix(core): corrige bug na extração de características
docs(readme): atualiza instruções de instalação
test(layer1): adiciona testes para captura de dados
```

## 🔄 Processo de Review

### Para Revisores

- Seja construtivo e respeitoso
- Foque na qualidade do código e design
- Teste as mudanças localmente
- Verifique documentação e testes

### Para Contribuidores

- Responda aos comentários prontamente
- Faça alterações solicitadas
- Mantenha discussões focadas no código
- Seja paciente durante o processo

## 🏆 Reconhecimento

Contribuidores são reconhecidos:

- **README**: Lista de contribuidores
- **Releases**: Menção em notas de versão
- **Documentação**: Créditos em páginas relevantes

## 📞 Obtendo Ajuda

- **Issues**: Para bugs e funcionalidades
- **Discussions**: Para perguntas gerais
- **Email**: guilherme.ceo@hubstry.com

## 📄 Código de Conduta

Este projeto adere ao [Contributor Covenant](https://www.contributor-covenant.org/). Ao participar, você concorda em manter um ambiente respeitoso e inclusivo.

### Nossos Compromissos

- **Respeito**: Tratamos todos com dignidade
- **Inclusão**: Valorizamos diversidade de perspectivas
- **Colaboração**: Trabalhamos juntos construtivamente
- **Aprendizado**: Apoiamos crescimento mútuo

## 🎯 Roadmap de Contribuições

### Prioridades Atuais

1. **Implementação das Layers 2-4**: Completar funcionalidades básicas
2. **Testes**: Aumentar cobertura para >90%
3. **Documentação**: Criar tutoriais e exemplos
4. **Performance**: Otimizar processamento de dados
5. **Interface**: Desenvolver interface web/desktop

### Áreas que Precisam de Ajuda

- 🧠 **Algoritmos de ML**: Implementação de modelos
- 📊 **Visualização**: Dashboards e gráficos
- 🌐 **Internacionalização**: Suporte a múltiplas línguas
- 🔧 **DevOps**: CI/CD e deployment
- 📱 **Mobile**: Aplicações móveis

## 🙏 Agradecimentos

Obrigado por contribuir para o JALS! Sua participação ajuda a construir um futuro onde a linguagem humana é amplificada e celebrada através da tecnologia.

---

**Lembre-se**: Toda contribuição, por menor que seja, é valiosa. Desde correções de typos até implementações de funcionalidades complexas, tudo ajuda a tornar o JALS melhor!

*Happy coding!* 🚀