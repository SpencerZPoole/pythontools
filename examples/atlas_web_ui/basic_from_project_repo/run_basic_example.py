import atlastk

# example from : https://github.com/epeios-q37/atlas-python

BODY = """
<fieldset>
 <input id="Input" data-xdh-onevent="Submit" value="World"/>
 <button data-xdh-onevent="Submit">Hello</button>
 <hr/>
 <fieldset>
  <output id="Output">Greetings displayed here!</output>
 </fieldset>
</fieldset>
"""

def ac_connect(dom):
  dom.inner("", BODY)
  dom.focus("Input")

def ac_submit(dom):
  name = dom.get_value("Input")
  dom.set_value("Output", f"Hello, {name}!")
  dom.set_value("Input", "")
  dom.focus("Input")

CALLBACKS = {
  "": ac_connect,
  "Submit": ac_submit
}

atlastk.launch(CALLBACKS)