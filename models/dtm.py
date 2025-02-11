from pydantic import BaseModel
from typing import Set, Dict, Tuple

class DTMCreationRequest(BaseModel):
    states: Set[str]  # Conjunto de estados
    input_symbols: Set[str] # Conjunto de símbolos de entrada
    tape_symbols: Set[str] # Conjunto de símbolos da fita
    # O campo transitions mapeia: estado -> símbolo da fita -> (novo_estado, símbolo a escrever, direção)
    transitions: Dict[str, Dict[str, Tuple[str, str, str]]]
    initial_state: str # Estado inicial
    blank_symbol: str # Símbolo que representa branco
    final_states: Set[str] # Conjunto de estados finais
