from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import subprocess

class AxiomApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)
        self.label = Label(text="Axiom Sovereign Node\nStatus: Ready", size_hint=(1, 0.8))
        self.btn = Button(text="Run ZK Prover", size_hint=(1, 0.2))
        self.btn.bind(on_press=self.run_prover)
        self.add_widget(self.label)
        self.add_widget(self.btn)

    def run_prover(self, instance):
        self.label.text = "Running Prover..."
        try:
            result = subprocess.run(["python3", "scripts/axiom_zk_prover.py"], capture_output=True, text=True)
            self.label.text = "Success!\n" + result.stdout[-100:]
        except Exception as e:
            self.label.text = f"Error: {str(e)}"

class AxiomSovereign(App):
    def build(self):
        return AxiomApp()

if __name__ == '__main__':
    AxiomSovereign().run()
