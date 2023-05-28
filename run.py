from streamlit.web import bootstrap

real_script = 'newUI2.py'
bootstrap.run(real_script,f'run.py{real_script}',[],{})
