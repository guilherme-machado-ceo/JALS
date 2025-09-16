# Guia de Início Rápido - JALS

Bem-vindo ao JALS (Journey Amplified Language Systems)! Este guia irá te ajudar a começar rapidamente com o framework.

## Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Git

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/guilherme-machado-ceo/JALS.git
cd JALS
```

### 2. Crie um ambiente virtual (recomendado)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
pip install -e .
```

## Primeiro Exemplo

Aqui está um exemplo básico de como usar o JALS:

```python
from jals.core import CoreIdeogram, AmplificationEngine
from jals.layers import Layer1, Layer2, Layer3, Layer4

# 1. Inicializar componentes
ideogram = CoreIdeogram()
engine = AmplificationEngine()

# 2. Inicializar as camadas
layer1 = Layer1()
layer2 = Layer2()
layer3 = Layer3()
layer4 = Layer4()

# 3. Carregar dados de exemplo
manuscript_data = layer1.capture("data/samples/manuscript_samples.json")
print("Dados manuscritos carregados:", len(manuscript_data['strokes']), "traços")

# 4. Processar através das camadas
# Layer 1: Manuscript Encoding
processed_data = layer1.preprocess(manuscript_data)
features = layer1.extract_features(processed_data)
encoded_data = layer1.encode(features)

# Layer 2: Symbolic Abstraction
symbolic_data = layer2.abstract(encoded_data)
print("Símbolos gerados:", len(symbolic_data['symbols']))

# Layer 3: Language Integration
linguistic_data = layer3.integrate(symbolic_data)
print("Unidades linguísticas:", len(linguistic_data['linguistic_units']))

# Layer 4: Computational Deployment
deployment_result = layer4.deploy(linguistic_data)
print("Deployment realizado para:", list(deployment_result['deployment_results'].keys()))
```

## Exemplo com Core Ideogram

```python
from jals.core import CoreIdeogram

# Criar um novo ideograma
ideogram = CoreIdeogram()

# Carregar dados manuscritos
ideogram.load_manuscript("data/samples/manuscript_samples.json")

# Extrair características
features = ideogram.extract_features()
print("Características extraídas:", list(features.keys()))

# Gerar representação simbólica
ideogram.generate_symbolic_representation(features)

# Converter para representação computacional
comp_rep = ideogram.to_computational_representation()
print("Tokens gerados:", len(comp_rep['tokens']))

# Salvar o ideograma
ideogram.save("meu_ideograma.json")
```

## Exemplo com Amplification Engine

```python
from jals.core import AmplificationEngine
from jals.core.amplification_engine import Layer1ToLayer2Transformer

# Criar engine de amplificação
engine = AmplificationEngine()

# Registrar transformadores
transformer = Layer1ToLayer2Transformer()
engine.register_transformer('layer1_to_layer2', transformer)

# Dados de exemplo
input_data = {
    'strokes': [
        {
            'id': 1,
            'points': [[0, 0], [10, 10], [20, 20]],
            'geometric': {'length': 28.28, 'curvature': 0.1},
            'kinematic': {'velocity': [0, 14.14, 14.14]}
        }
    ]
}

# Amplificar dados
result = engine.amplify(input_data, 'layer1', 'layer2')
print("Amplificação realizada:", result['transformation_info'])

# Verificar qualidade da transformação
quality = engine.get_transformation_quality()
print("Qualidade da transformação:", quality['overall_quality'])
```

## Trabalhando com Dados Personalizados

### Formato de Dados Manuscritos

Seus dados devem seguir este formato JSON:

```json
{
  "metadata": {
    "source": "minha_fonte",
    "resolution": [1920, 1080],
    "sampling_rate": 120,
    "timestamp": "2025-01-16T10:30:00Z"
  },
  "strokes": [
    {
      "id": 1,
      "points": [[x1, y1], [x2, y2], ...],
      "timestamps": [t1, t2, ...],
      "pressure": [p1, p2, ...],
      "velocity": [v1, v2, ...]
    }
  ]
}
```

### Carregando Seus Dados

```python
from jals.layers import Layer1

layer1 = Layer1()

# Carregar seus dados
data = layer1.capture("caminho/para/seus/dados.json")

# Processar
processed = layer1.preprocess(data)
features = layer1.extract_features(processed)
encoded = layer1.encode(features)
```

## Configuração Avançada

### Configurando as Camadas

```python
# Configuração personalizada para Layer 1
config_layer1 = {
    'preprocessing': {
        'normalize_coordinates': True,
        'filter_noise': True,
        'interpolate_points': True
    },
    'feature_extraction': {
        'geometric_features': True,
        'kinematic_features': True,
        'topological_features': True
    }
}

layer1 = Layer1(config=config_layer1)
```

### Salvando e Carregando Estados

```python
# Salvar estado da engine
engine.save_state("minha_engine.json")

# Carregar estado
engine.load_state("minha_engine.json")
```

## Executando Testes

Para verificar se tudo está funcionando corretamente:

```bash
# Executar todos os testes
pytest

# Executar testes específicos
pytest tests/test_core.py

# Executar com verbose
pytest -v
```

## Próximos Passos

1. **Explore a documentação completa**: [Whitepaper](../whitepaper.md)
2. **Leia o manifesto**: [Manifesto JALS](../manifesto.md)
3. **Entenda a arquitetura**: [Arquitetura do Sistema](../architecture/)
4. **Experimente com notebooks**: Veja a pasta `notebooks/` para exemplos interativos
5. **Contribua**: Leia o [CONTRIBUTING.md](../../CONTRIBUTING.md) para contribuir com o projeto

## Solução de Problemas

### Erro de Importação

Se você receber erros de importação:

```bash
# Certifique-se de que o pacote está instalado em modo desenvolvimento
pip install -e .
```

### Problemas com Dependências

```bash
# Atualize o pip
pip install --upgrade pip

# Reinstale as dependências
pip install -r requirements.txt --force-reinstall
```

### Dados de Exemplo Não Encontrados

```bash
# Certifique-se de estar no diretório raiz do projeto
ls data/samples/manuscript_samples.json
```

## Suporte

- **Issues**: [GitHub Issues](https://github.com/guilherme-machado-ceo/JALS/issues)
- **Discussões**: [GitHub Discussions](https://github.com/guilherme-machado-ceo/JALS/discussions)
- **Email**: guilherme.ceo@hubstry.com

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](../../LICENSE) para detalhes.

---

**Parabéns!** 🎉 Você agora tem o JALS funcionando em seu ambiente. Explore, experimente e contribua para o futuro da amplificação linguística!