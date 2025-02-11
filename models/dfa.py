from pydantic import BaseModel
from typing import Set, Dict
class DFACreationRequest(BaseModel):
    states: Set[str]  # Conjunto de estados
    input_symbols: Set[str]  # Conjunto de símbolos de entrada
    transitions: Dict[str, Dict[str, str]]  # Transições: {estado: {símbolo: estado_destino}}
    initial_state: str  # Estado inicial
    final_states: Set[str]  # Conjunto de estados finais