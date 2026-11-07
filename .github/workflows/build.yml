from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class VirusScannerApp(App):
    def build(self):
        self.title = "App Scanner"
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Header Label
        self.header_label = Label(
            text="[b]Security & App Scanner[/b]",
            markup=True,
            font_size=20,
            size_hint_y=None,
            height=50
        )
        layout.add_widget(self.header_label)
        
        # Scan Button
        self.scan_btn = Button(
            text="Start Scan",
            size_hint_y=None,
            height=60,
            background_color=(0.1, 0.6, 0.8, 1)
        )
        self.scan_btn.bind(on_press=self.start_scan)
        layout.add_widget(self.scan_btn)
        
        # Results Label
        self.result_label = Label(
            text="Click 'Start Scan' to check installed apps and permissions.",
            valign='top',
            halign='left',
            markup=True
        )
        self.result_label.bind(
            size=lambda s, w: setattr(s, 'text_size', (w[0], None))
        )
        
        scroll = ScrollView(size_hint=(1, 1))
        scroll.add_widget(self.result_label)
        layout.add_widget(scroll)
        
        return layout

    def start_scan(self, instance):
        self.result_label.text = "Scanning apps and permissions...\n\n"
        
        simulated_apps = [
            {"name": "com.example.app1", "status": "Safe - No dangerous permissions"},
            {"name": "com.unknown.suspicious", "status": "WARNING: Requests Camera & SMS access in background!"},
            {"name": "com.android.tools", "status": "Safe - Trusted system app"},
        ]
        
        report = "[b]Scan Results:[/b]\n\n"
        for app in simulated_apps:
            report += f"• App: [b]{app['name']}[/b]\n  Status: {app['status']}\n\n"
                
        report += "Scan completed successfully."
        self.result_label.text = report

if __name__ == '__main__':
    VirusScannerApp().run()
      
