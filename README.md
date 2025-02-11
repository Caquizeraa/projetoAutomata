get http://localhost:8000/dfa/dfa_1/

get http://localhost:8000/dfa/dfa_1/image

get http://127.0.0.1:8000/dpda/dpda_1/

get http://127.0.0.1:8000/dtm/dtm_1/

post http://127.0.0.1:8000/dfa/
body: {
  "states": ["q0", "q1", "q2"],
  "input_symbols": ["0", "1"],
  "transitions": {
    "q0": {"0": "q0", "1": "q1"},
    "q1": {"0": "q0", "1": "q2"},
    "q2": {"0": "q2", "1": "q1"}
  },
  "initial_state": "q0",
  "final_states": ["q1"]
}

post http://localhost:8000/dfa/dfa_1/accept
body: {
  "input_string": "00111"
}

post http://127.0.0.1:8000/dpda/
body: {
  "states": ["q0", "q1", "q2", "q3"],
  "input_symbols": ["a", "b"],
  "stack_symbols": ["0", "1"],
  "transitions": {
    "q0": {
      "a": {
        "0": ["q1", ["1", "0"]]
      }
    },
    "q1": {
      "a": {
        "1": ["q1", ["1", "1"]]
      },
      "b": {
        "1": ["q2", ""]
      }
    },
    "q2": {
      "b": {
        "1": ["q2", ""]
      },
      "": {
        "0": ["q3", ["0"]]
      }
    }
  },
  "initial_state": "q0",
  "initial_stack_symbol": "0",
  "final_states": ["q3"],
  "acceptance_mode": "final_state"
}

post http://localhost:8000/dpda/dpda_1/accept
body: {
  "input_string": "ab"
}

post http://127.0.0.1:8000/dtm/
body: {
  "states": ["q0", "q1", "q2", "q3", "q4"],
  "input_symbols": ["0", "1"],
  "tape_symbols": ["0", "1", "x", "y", "."],
  "transitions": {
    "q0": {
      "0": ["q1", "x", "R"],
      "y": ["q3", "y", "R"]
    },
    "q1": {
      "0": ["q1", "0", "R"],
      "1": ["q2", "y", "L"],
      "y": ["q1", "y", "R"]
    },
    "q2": {
      "0": ["q2", "0", "L"],
      "x": ["q0", "x", "R"],
      "y": ["q2", "y", "L"]
    },
    "q3": {
      "y": ["q3", "y", "R"],
      ".": ["q4", ".", "R"]
    }
  },
  "initial_state": "q0",
  "blank_symbol": ".",
  "final_states": ["q4"]
}

post http://127.0.0.1:8000/dtm/dtm_1/accept
body: {
  "input_string": "000111"
}
