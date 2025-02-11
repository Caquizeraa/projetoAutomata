# Imports
import io
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

# Imports DFA
from automata.fa.dfa import DFA
from models.dfa import DFACreationRequest
# Imports DPDA
from automata.pda.dpda import DPDA
from models.dpda import DPDACreationRequest
# Imports DTM
from automata.tm.dtm import DTM
from models.dtm import DTMCreationRequest

app = FastAPI()

# Dicionários para armazenar os autômatos criados
dfa_storage = {}
dpda_storage = {}
dtm_storage = {}

# Modelo para o input da string a ser verificada
class AcceptanceRequest(BaseModel):
    input_string: str

# ---------------- Endpoints para DFA ----------------
@app.post("/dfa/")
def create_dfa(dfa_request: DFACreationRequest):
    try:
        # Cria o DFA com base na requisição
        dfa = DFA(
            states=dfa_request.states,
            input_symbols=dfa_request.input_symbols,
            transitions=dfa_request.transitions,
            initial_state=dfa_request.initial_state,
            final_states=dfa_request.final_states
        )
        # Gera um ID único para o DFA e armazena em memória
        dfa_id = f"dfa_{len(dfa_storage) + 1}"
        dfa_storage[dfa_id] = dfa
        return {"message": "DFA criado com sucesso!", "dfa_id": dfa_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/dfa/{dfa_id}/")
def get_dfa_info(dfa_id: str):
    if dfa_id not in dfa_storage:
        raise HTTPException(status_code=404, detail="DFA não encontrado")
    # Retorna as informações do DFA salvas na memória 
    dfa = dfa_storage[dfa_id]
    return {
        "states": dfa.states,
        "input_symbols": dfa.input_symbols,
        "transitions": dfa.transitions,
        "initial_state": dfa.initial_state,
        "final_states": dfa.final_states
    }

@app.post("/dfa/{dfa_id}/accept")
def accept_dfa(dfa_id: str, acceptance: AcceptanceRequest):
    if dfa_id not in dfa_storage:
        raise HTTPException(status_code=404, detail="DFA não encontrado")
    
    dfa = dfa_storage[dfa_id]
    try:
        # Verifica se o DFA aceita a string
        result = dfa.accepts_input(acceptance.input_string)
        return {"accepted": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# ---------------- Endpoints para DPDA ----------------

@app.post("/dpda/")
def create_dpda(dpda_request: DPDACreationRequest):
    try:
        # Cria o DPDA com base na requisição
        dpda = DPDA(
            states=dpda_request.states,
            input_symbols=dpda_request.input_symbols,
            stack_symbols=dpda_request.stack_symbols,
            transitions=dpda_request.transitions,
            initial_state=dpda_request.initial_state,
            initial_stack_symbol=dpda_request.initial_stack_symbol,
            final_states=dpda_request.final_states,
            acceptance_mode=dpda_request.acceptance_mode
        )
        # Gera um ID único para o DPDA e armazena em memória
        dpda_id = f"dpda_{len(dpda_storage) + 1}"
        dpda_storage[dpda_id] = dpda
        
        return {"message": "DPDA criado com sucesso!", "dpda_id": dpda_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/dpda/{dpda_id}/")
def get_dpda_info(dpda_id: str):
    if dpda_id not in dpda_storage:
        raise HTTPException(status_code=404, detail="DPDA não encontrado")
    # Retorna as informações do DPDA salvas na memória 
    dpda = dpda_storage[dpda_id]
    return {
        "states": dpda.states,
        "input_symbols": dpda.input_symbols,
        "stack_symbols": dpda.stack_symbols,
        "transitions": dpda.transitions,
        "initial_state": dpda.initial_state,
        "initial_stack_symbol": dpda.initial_stack_symbol,
        "final_states": dpda.final_states,
        "acceptance_mode": dpda.acceptance_mode
    }

@app.post("/dpda/{dpda_id}/accept")
def accept_dpda(dpda_id: str, acceptance: AcceptanceRequest):
    if dpda_id not in dpda_storage:
        raise HTTPException(status_code=404, detail="DPDA não encontrado")
    
    dpda = dpda_storage[dpda_id]
    try:
        # Verifica se o DPDA aceita a string
        result = dpda.accepts_input(acceptance.input_string)
        return {"accepted": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ---------------- Endpoints para DTM ----------------

@app.post("/dtm/")
def create_dtm(dtm_request: DTMCreationRequest):
    try:
        # Cria o DTM com base na requisição
        dtm = DTM(
            states=dtm_request.states,
            input_symbols=dtm_request.input_symbols,
            tape_symbols=dtm_request.tape_symbols,
            transitions=dtm_request.transitions,
            initial_state=dtm_request.initial_state,
            blank_symbol=dtm_request.blank_symbol,
            final_states=dtm_request.final_states
        )
        # Gera um ID único para o DTM e armazena em memória
        dtm_id = f"dtm_{len(dtm_storage) + 1}"
        dtm_storage[dtm_id] = dtm
        
        return {"message": "DTM criado com sucesso!", "dtm_id": dtm_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/dtm/{dtm_id}/")
def get_dtm_info(dtm_id: str):
    if dtm_id not in dtm_storage:
        raise HTTPException(status_code=404, detail="DTM não encontrado")
    # Retorna as informações da DTM salvas na memória 
    dtm = dtm_storage[dtm_id]
    return {
        "states": dtm.states,
        "input_symbols": dtm.input_symbols,
        "tape_symbols": dtm.tape_symbols,
        "transitions": dtm.transitions,
        "initial_state": dtm.initial_state,
        "blank_symbol": dtm.blank_symbol,
        "final_states": dtm.final_states
    }

@app.post("/dtm/{dtm_id}/accept")
def accept_dtm(dtm_id: str, acceptance: AcceptanceRequest):
    if dtm_id not in dtm_storage:
        raise HTTPException(status_code=404, detail="DTM não encontrado")
    
    dtm = dtm_storage[dtm_id]
    try:
        # Verifica se o DTM aceita a string
        result = dtm.accepts_input(acceptance.input_string)
        return {"accepted": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
# ---------------- Rota para obter o diagrama (imagem) da DFA ----------------
@app.get("/dfa/{dfa_id}/image")
def get_dfa_image(dfa_id: str):
    # busca a DFA na memória
    if dfa_id in dfa_storage:
        dfa = dfa_storage[dfa_id]
    else:
        raise HTTPException(status_code=404, detail="Autômato não encontrado")
    
    try:
        # Chama o método show_diagram() que deve retornar um objeto de diagrama
        diagram = dfa.show_diagram()
        
        # Verifica se o objeto possui o método 'pipe'; se não, usa 'create_png'
        if hasattr(diagram, "pipe"):
            image_bytes = diagram.pipe(format="png")
        elif hasattr(diagram, "create_png"):
            image_bytes = diagram.create_png()
        else:
            raise HTTPException(status_code=500, detail="O objeto do diagrama não possui método para renderizar imagem")
        
        # Retorna a imagem via StreamingResponse com o media_type adequado
        return StreamingResponse(io.BytesIO(image_bytes), media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))