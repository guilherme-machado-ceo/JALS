import pytest
import json
from src.core import CoreIdeogram, AmplificationEngine

class TestCoreIdeogram:
    """Testes para o Core Ideogram."""
    
    def test_initialization(self):
        """Testa inicialização do Core Ideogram."""
        ideogram = CoreIdeogram()
        assert ideogram.data is not None
        assert 'strokes' in ideogram.data
        assert 'metadata' in ideogram.data
        
    def test_extract_features(self):
        """Testa extração de características."""
        ideogram = CoreIdeogram()
        # Simula dados de traços
        ideogram.data['strokes'] = [
            {'id': 1, 'points': [[0, 0], [1, 1], [2, 2]]}
        ]
        
        features = ideogram.extract_features()
        assert 'geometric' in features
        assert 'kinematic' in features
        assert 'topological' in features
        
    def test_generate_symbolic_representation(self):
        """Testa geração de representação simbólica."""
        ideogram = CoreIdeogram()
        ideogram.data['strokes'] = [
            {'id': 1, 'points': [[0, 0], [1, 1]]}
        ]
        
        features = ideogram.extract_features()
        ideogram.generate_symbolic_representation(features)
        
        assert ideogram.data['symbolic_representation'] is not None
        assert 'symbols' in ideogram.data['symbolic_representation']


class TestAmplificationEngine:
    """Testes para a Amplification Engine."""
    
    def test_initialization(self):
        """Testa inicialização da Amplification Engine."""
        engine = AmplificationEngine()
        assert engine.transformers == {}
        assert engine.history == []
        
    def test_register_transformer(self):
        """Testa registro de transformador."""
        from src.core.amplification_engine import Layer1ToLayer2Transformer
        
        engine = AmplificationEngine()
        transformer = Layer1ToLayer2Transformer()
        
        engine.register_transformer('layer1_to_layer2', transformer)
        assert 'layer1_to_layer2' in engine.transformers
        
    def test_amplify(self):
        """Testa amplificação entre camadas."""
        from src.core.amplification_engine import Layer1ToLayer2Transformer
        
        engine = AmplificationEngine()
        transformer = Layer1ToLayer2Transformer()
        engine.register_transformer('layer1_to_layer2', transformer)
        
        input_data = {
            'strokes': [
                {'id': 1, 'points': [[0, 0], [1, 1]]}
            ]
        }
        
        result = engine.amplify(input_data, 'layer1', 'layer2')
        assert 'symbols' in result
        assert 'transformation_info' in result