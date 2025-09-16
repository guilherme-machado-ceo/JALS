# JALS Data Directory

Este diretório contém dados de exemplo e datasets para o projeto JALS.

## Estrutura

- `samples/` - Dados de exemplo para testes e demonstrações
  - `manuscript_samples.json` - Exemplos de dados manuscritos capturados
  - `symbolic_samples.json` - Exemplos de representações simbólicas

## Formato dos Dados

### Manuscript Data
Os dados manuscritos seguem o formato:
```json
{
  "metadata": {
    "source": "fonte_dos_dados",
    "resolution": [largura, altura],
    "sampling_rate": taxa_amostragem,
    "timestamp": "timestamp_iso",
    "user_id": "identificador_usuario"
  },
  "strokes": [
    {
      "id": identificador_traço,
      "points": [[x1, y1], [x2, y2], ...],
      "timestamps": [t1, t2, ...],
      "pressure": [p1, p2, ...],
      "velocity": [v1, v2, ...]
    }
  ]
}
```

### Symbolic Data
As representações simbólicas seguem o formato:
```json
{
  "symbols": [
    {
      "id": identificador_simbolo,
      "type": "tipo_simbolo",
      "properties": {
        "propriedades_especificas": "valores"
      }
    }
  ],
  "relationships": [
    {
      "source": "id_simbolo_origem",
      "target": "id_simbolo_destino",
      "type": "tipo_relacionamento",
      "strength": valor_forca
    }
  ]
}
```

## Uso

Para carregar dados de exemplo:

```python
from jals.layers import Layer1
import json

# Carregar dados manuscritos
layer1 = Layer1()
data = layer1.capture('data/samples/manuscript_samples.json')

# Processar dados
processed = layer1.preprocess(data)
features = layer1.extract_features(processed)
encoded = layer1.encode(features)
```