from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class ScannerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        self.title_label = Label(
            text='تطبيق الماسح الضوئي',
            font_size='24sp',
            size_hint=(1, 0.2)
        )
        
        self.input_field = TextInput(
            text='',
            hint_text='أدخل النص أو الكود هنا...',
            size_hint=(1, 0.2),
            multiline=False
        )
        
        self.result_label = Label(
            text='النتيجة ستظهر هنا',
            font_size='18sp',
            size_hint=(1, 0.4)
        )
        
        scan_button = Button(
            text='مسح (Scan)',
            font_size='20sp',
            size_hint=(1, 0.2),
            background_color=(0.1, 0.6, 0.3, 1)
        )
        scan_button.bind(on_press=self.on_scan)
        
        layout.add_widget(self.title_label)
        layout.add_widget(self.input_field)
        layout.add_widget(scan_button)
        layout.add_widget(self.result_label)
        
        return layout

    def on_scan(self, instance):
        text = self.input_field.text
        if text:
            self.result_label.text = f"تم مسح العنصر بنجاح:\n{text}"
        else:
            self.result_label.text = "الرجاء إدخال نص أولاً!"

if __name__ == '__main__':
    ScannerApp().run()
          
