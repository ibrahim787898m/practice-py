import spacy
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical, ScrollableContainer
from textual.widgets import Header, Footer, Static, Button, TextArea, Label, DataTable
from textual.binding import Binding

class NLPApp(App):
    """A Textual app for NLP operations using spaCy."""
    
    CSS = """
    Screen {
        background: $surface;
    }
    
    #textarea {
        height: 8;
        margin: 1;
    }
    
    #process-btn {
        width: 50;
        margin: 1;
        dock: top;
    }
    
    #sidebar {
        width: 35;
        height: 100%;
        border: solid $accent;
        padding: 1;
    }
    
    #results {
        border: solid $success;
        height: 100%;
        padding: 1;
    }
    
    Button {
        margin: 1;
        width: 100%;
    }
    
    .title {
        background: $primary;
        color: $text;
        padding: 1;
        text-align: center;
        text-style: bold;
    }
    
    #status {
        background: $panel;
        color: $warning;
        padding: 1;
        margin-top: 1;
        text-align: center;
    }
    
    DataTable {
        height: 100%;
    }
    """
    
    BINDINGS = [
        Binding("q", "quit", "Quit", show=True),
        Binding("c", "clear", "Clear", show=True),
    ]
    
    def __init__(self):
        super().__init__()
        self.nlp = None
        self.doc = None
        self.processed_text = ""
    
    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        
        with Container():
            # Input area - split into text and button
            yield Static("Enter Text to Analyze:", classes="title")
            yield TextArea(id="textarea", text="The quick brown fox jumps over the lazy dog.")
            yield Button("▶ Process Text", id="process-btn", variant="primary")
            
            # Main layout with sidebar and results
            with Horizontal():
                # Sidebar with operation buttons
                with Vertical(id="sidebar"):
                    yield Static("Operations", classes="title")
                    yield Button("1. Tokenization", id="btn-tokenization")
                    yield Button("2. Linguistic Annotation", id="btn-linguistic")
                    yield Button("3. Lemmatization", id="btn-lemmatization")
                    yield Button("4. Sentence Detection", id="btn-sentence")
                    yield Button("5. POS Tagging", id="btn-pos")
                    yield Button("6. Named Entity Recognition", id="btn-ner")
                    yield Button("7. Stop Words Removal", id="btn-stopwords")
                    yield Button("8. Dependency Parsing", id="btn-dependency")
                    yield Static("", id="status")
                
                # Results area
                with ScrollableContainer(id="results"):
                    yield DataTable(id="result-table")
                    yield Static("Results will appear here", id="result-display")
        
        yield Footer()
    
    def on_mount(self) -> None:
        """Load spaCy model when app starts."""
        self.update_status("Loading spaCy model...")
        try:
            self.nlp = spacy.load("en_core_web_sm")
            self.update_status("✓ Model loaded! Processing sample text...")
            # Auto-process the sample text
            self.process_text()
        except Exception as e:
            self.update_status(f"❌ Error loading model: {e}")
    
    def update_status(self, message: str):
        """Update status message."""
        status = self.query_one("#status", Static)
        status.update(message)
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button clicks."""
        button_id = event.button.id
        
        if button_id == "process-btn":
            self.process_text()
        elif button_id == "btn-tokenization":
            self.show_tokenization()
        elif button_id == "btn-linguistic":
            self.show_linguistic_annotation()
        elif button_id == "btn-lemmatization":
            self.show_lemmatization()
        elif button_id == "btn-sentence":
            self.show_sentence_detection()
        elif button_id == "btn-pos":
            self.show_pos_tagging()
        elif button_id == "btn-ner":
            self.show_ner()
        elif button_id == "btn-stopwords":
            self.show_stop_words()
        elif button_id == "btn-dependency":
            self.show_dependency_parsing()
    
    def process_text(self):
        """Process the input text with spaCy."""
        textarea = self.query_one("#textarea", TextArea)
        text = textarea.text.strip()
        
        if not text:
            self.update_status("❌ Please enter some text")
            return
        
        if not self.nlp:
            self.update_status("❌ Model not loaded yet")
            return
        
        self.update_status("Processing text...")
        try:
            self.doc = self.nlp(text)
            self.processed_text = text
            self.update_status(f"✓ Processed: '{text[:50]}...' ({len(self.doc)} tokens)")
            
            # Show tokenization by default
            self.show_tokenization()
        except Exception as e:
            self.update_status(f"❌ Error: {e}")
    
    def show_tokenization(self):
        """Display tokenization results."""
        if not self.doc:
            self.update_status("❌ Please process text first")
            return
        
        # Get the table widget
        table = self.query_one("#result-table", DataTable)
        table.clear(columns=True)
        table.display = True
        
        # Hide text display
        result_display = self.query_one("#result-display", Static)
        result_display.display = False
        
        # Setup table
        table.add_column("Token #", width=10)
        table.add_column("Token", width=30)
        
        for index, token in enumerate(self.doc, start=1):
            table.add_row(str(index), token.text)
    
    def show_linguistic_annotation(self):
        """Display linguistic annotations."""
        if not self.doc:
            self.update_status("❌ Please process text first")
            return
        
        table = self.query_one("#result-table", DataTable)
        table.clear(columns=True)
        table.display = True
        
        result_display = self.query_one("#result-display", Static)
        result_display.display = False
        
        table.add_column("Token", width=15)
        table.add_column("POS", width=10)
        table.add_column("Lemma", width=15)
        table.add_column("Dependency", width=12)
        table.add_column("Entity", width=10)
        
        for token in self.doc:
            table.add_row(
                token.text,
                token.pos_,
                token.lemma_,
                token.dep_,
                token.ent_type_ if token.ent_type_ else "-"
            )
    
    def show_lemmatization(self):
        """Display lemmatization results."""
        if not self.doc:
            self.update_status("❌ Please process text first")
            return
        
        table = self.query_one("#result-table", DataTable)
        table.clear(columns=True)
        table.display = True
        
        result_display = self.query_one("#result-display", Static)
        result_display.display = False
        
        table.add_column("Token", width=25)
        table.add_column("Lemma", width=25)
        
        for token in self.doc:
            table.add_row(token.text, token.lemma_)
    
    def show_sentence_detection(self):
        """Display sentence detection results."""
        if not self.doc:
            self.update_status("❌ Please process text first")
            return
        
        table = self.query_one("#result-table", DataTable)
        table.clear(columns=True)
        table.display = True
        
        result_display = self.query_one("#result-display", Static)
        result_display.display = False
        
        table.add_column("Sentence #", width=12)
        table.add_column("Sentence", width=70)
        
        for index, sent in enumerate(self.doc.sents, start=1):
            table.add_row(str(index), sent.text)
    
    def show_pos_tagging(self):
        """Display POS tagging results."""
        if not self.doc:
            self.update_status("❌ Please process text first")
            return
        
        table = self.query_one("#result-table", DataTable)
        table.clear(columns=True)
        table.display = True
        
        result_display = self.query_one("#result-display", Static)
        result_display.display = False
        
        table.add_column("Token", width=15)
        table.add_column("POS", width=10)
        table.add_column("Tag", width=10)
        table.add_column("Detail", width=40)
        
        for token in self.doc:
            detail = spacy.explain(token.tag_) if spacy.explain(token.tag_) else "-"
            table.add_row(token.text, token.pos_, token.tag_, detail)
    
    def show_ner(self):
        """Display named entity recognition results."""
        if not self.doc:
            self.update_status("❌ Please process text first")
            return
        
        result_display = self.query_one("#result-display", Static)
        table = self.query_one("#result-table", DataTable)
        
        if not self.doc.ents:
            table.display = False
            result_display.display = True
            result_display.update("No named entities found in the text.")
            return
        
        table.clear(columns=True)
        table.display = True
        result_display.display = False
        
        table.add_column("Entity", width=25)
        table.add_column("Type", width=15)
        table.add_column("Explanation", width=40)
        
        for ent in self.doc.ents:
            explanation = spacy.explain(ent.label_) if spacy.explain(ent.label_) else "-"
            table.add_row(ent.text, ent.label_, explanation)
    
    def show_stop_words(self):
        """Display stop words removal results."""
        if not self.doc:
            self.update_status("❌ Please process text first")
            return
        
        result_display = self.query_one("#result-display", Static)
        table = self.query_one("#result-table", DataTable)
        
        table.display = False
        result_display.display = True
        
        filtered_tokens = [token.text for token in self.doc if not token.is_stop]
        filtered_sent = " ".join(filtered_tokens)
        
        output = f"Original Text:\n{self.processed_text}\n\n"
        output += f"After Stop Word Removal:\n{filtered_sent}\n\n"
        output += f"Removed {len(self.doc) - len(filtered_tokens)} stop words"
        
        result_display.update(output)
    
    def show_dependency_parsing(self):
        """Display dependency parsing results."""
        if not self.doc:
            self.update_status("❌ Please process text first")
            return
        
        table = self.query_one("#result-table", DataTable)
        table.clear(columns=True)
        table.display = True
        
        result_display = self.query_one("#result-display", Static)
        result_display.display = False
        
        table.add_column("Token", width=15)
        table.add_column("Dependency", width=12)
        table.add_column("Head", width=15)
        table.add_column("POS", width=10)
        
        for token in self.doc:
            table.add_row(token.text, token.dep_, token.head.text, token.pos_)
    
    def action_clear(self):
        """Clear the results."""
        result_display = self.query_one("#result-display", Static)
        table = self.query_one("#result-table", DataTable)
        
        table.display = False
        result_display.display = True
        result_display.update("Results will appear here")
        self.update_status("✓ Cleared")
    
    def action_quit(self):
        """Quit the application."""
        self.exit()


if __name__ == "__main__":
    app = NLPApp()
    app.run()