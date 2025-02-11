from pydantic import BaseModel
from typing import Set, Dict, Tuple, Union

class DPDACreationRequest(BaseModel):
    states: Set[str] # Conjunto de estados
    input_symbols: Set[str] # Conjunto de símbolos de entrada
    stack_symbols: Set[str]  # Conjunto de símbolos da pilha
    # O campo transitions mapeia: estado -> símbolo de entrada -> símbolo da pilha -> (novo_estado, operação na pilha)
    transitions: Dict[str, Dict[str, Dict[str, Tuple[str, Union[str, Tuple[str, ...]]]]]]
    initial_state: str # Estado inicial
    initial_stack_symbol: str # Símbolo incial da pilha
    final_states: Set[str] # Conjunto de estados finais
    acceptance_mode: str # Modo de aceitação 
