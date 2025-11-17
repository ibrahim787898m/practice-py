import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import spacy
import threading

class NLPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NLP Analysis Tool - spaCy")
        self.root.geometry("1200x700")
        self.root.configure(bg="#f0f0f0")
        
        # Initialize variables
        self.nlp = None
        self.doc = None
        self.processed_text = ""
        
        # Load spaCy model in background
        self.load_model()
        
        # Create UI
        self.create_widgets()
    
    def create_widgets(self):
        # ===== TOP FRAME: Title and Input =====
        top_frame = tk.Frame(self.root, bg="#2c3e50", pady=10)
        top_frame.pack(fill=tk.X)
        
        title_label = tk.Label(
            top_frame, 
            text="🔍 NLP Analysis Tool", 
            font=("Arial", 20, "bold"),
            bg="#2c3e50", 
            fg="white"
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            top_frame,
            text="Powered by spaCy",
            font=("Arial", 10),
            bg="#2c3e50",
            fg="#95a5a6"
        )
        subtitle_label.pack()
        
        # ===== INPUT SECTION =====
        input_frame = tk.Frame(self.root, bg="#ecf0f1", padx=20, pady=15)
        input_frame.pack(fill=tk.X)
        
        input_label = tk.Label(
            input_frame,
            text="Enter Text to Analyze:",
            font=("Arial", 12, "bold"),
            bg="#ecf0f1"
        )
        input_label.pack(anchor=tk.W)
        
        self.text_input = scrolledtext.ScrolledText(
            input_frame,
            height=5,
            font=("Arial", 11),
            wrap=tk.WORD,
            relief=tk.SOLID,
            borderwidth=1
        )
        self.text_input.pack(fill=tk.BOTH, expand=True, pady=(5, 10))
        self.text_input.insert(tk.END, "The quick brown fox jumps over the lazy dog.")
        
        process_btn = tk.Button(
            input_frame,
            text="🚀 Process Text",
            font=("Arial", 12, "bold"),
            bg="#3498db",
            fg="white",
            activebackground="#2980b9",
            activeforeground="white",
            relief=tk.RAISED,
            borderwidth=2,
            padx=20,
            pady=10,
            cursor="hand2",
            command=self.process_text
        )
        process_btn.pack()
        
        # Status label
        self.status_label = tk.Label(
            input_frame,
            text="Status: Loading spaCy model...",
            font=("Arial", 10),
            bg="#ecf0f1",
            fg="#7f8c8d"
        )
        self.status_label.pack(pady=(5, 0))
        
        # ===== MAIN CONTENT: SIDEBAR + RESULTS =====
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # SIDEBAR: Operations
        sidebar = tk.Frame(main_frame, bg="white", relief=tk.SOLID, borderwidth=1)
        sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        
        sidebar_title = tk.Label(
            sidebar,
            text="Operations",
            font=("Arial", 14, "bold"),
            bg="#34495e",
            fg="white",
            pady=10
        )
        sidebar_title.pack(fill=tk.X)
        
        # Operation buttons
        operations = [
            ("📝 Tokenization", self.show_tokenization),
            ("📊 Linguistic Annotation", self.show_linguistic_annotation),
            ("🔤 Lemmatization", self.show_lemmatization),
            ("📄 Sentence Detection", self.show_sentence_detection),
            ("🏷️ POS Tagging", self.show_pos_tagging),
            ("🎯 Named Entity Recognition", self.show_ner),
            ("🚫 Stop Words Removal", self.show_stop_words),
            ("🔗 Dependency Parsing", self.show_dependency_parsing),
        ]
        
        for text, command in operations:
            btn = tk.Button(
                sidebar,
                text=text,
                font=("Arial", 11),
                bg="white",
                fg="#2c3e50",
                activebackground="#3498db",
                activeforeground="white",
                relief=tk.FLAT,
                borderwidth=0,
                padx=20,
                pady=12,
                cursor="hand2",
                command=command,
                anchor=tk.W
            )
            btn.pack(fill=tk.X, padx=5, pady=2)
            
            # Hover effects
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#ecf0f1"))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg="white"))
        
        # RESULTS AREA
        results_frame = tk.Frame(main_frame, bg="white", relief=tk.SOLID, borderwidth=1)
        results_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        results_title = tk.Label(
            results_frame,
            text="Results",
            font=("Arial", 14, "bold"),
            bg="#27ae60",
            fg="white",
            pady=10
        )
        results_title.pack(fill=tk.X)
        
        # Results display (Treeview for tables)
        self.results_tree = ttk.Treeview(results_frame, show="headings")
        self.results_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Scrollbars for results
        vsb = ttk.Scrollbar(self.results_tree, orient="vertical", command=self.results_tree.yview)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        self.results_tree.configure(yscrollcommand=vsb.set)
        
        # Text display for non-tabular results
        self.results_text = scrolledtext.ScrolledText(
            results_frame,
            font=("Arial", 11),
            wrap=tk.WORD,
            relief=tk.FLAT
        )
        
    def load_model(self):
        """Load spaCy model in background thread."""
        def load():
            try:
                self.nlp = spacy.load("en_core_web_sm")
                self.status_label.config(
                    text="✓ Status: Model loaded! Enter text and click Process.",
                    fg="#27ae60"
                )
            except Exception as e:
                self.status_label.config(
                    text=f"❌ Error: {str(e)}",
                    fg="#e74c3c"
                )
        
        thread = threading.Thread(target=load, daemon=True)
        thread.start()
    
    def process_text(self):
        """Process the input text with spaCy."""
        text = self.text_input.get("1.0", tk.END).strip()
        
        if not text:
            messagebox.showwarning("Empty Input", "Please enter some text to analyze.")
            return
        
        if not self.nlp:
            messagebox.showerror("Model Not Ready", "spaCy model is still loading. Please wait.")
            return
        
        self.status_label.config(text="⏳ Processing text...", fg="#f39c12")
        self.root.update()
        
        try:
            self.doc = self.nlp(text)
            self.processed_text = text
            self.status_label.config(
                text=f"✓ Status: Processed {len(self.doc)} tokens successfully!",
                fg="#27ae60"
            )
            
            # Auto-show tokenization
            self.show_tokenization()
        except Exception as e:
            messagebox.showerror("Processing Error", str(e))
            self.status_label.config(text=f"❌ Error: {str(e)}", fg="#e74c3c")
    
    def clear_results(self):
        """Clear the results display."""
        # Clear treeview
        for item in self.results_tree.get_children():
            self.results_tree.delete(item)
        self.results_tree["columns"] = ()
        
        # Hide text display
        self.results_text.pack_forget()
        self.results_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    def show_table(self, columns, data):
        """Display data in table format."""
        self.clear_results()
        
        # Configure columns
        self.results_tree["columns"] = columns
        for col in columns:
            self.results_tree.heading(col, text=col)
            self.results_tree.column(col, anchor=tk.W, width=150)
        
        # Add data
        for row in data:
            self.results_tree.insert("", tk.END, values=row)
    
    def show_text(self, text):
        """Display text results."""
        self.clear_results()
        self.results_tree.pack_forget()
        self.results_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert(tk.END, text)
    
    def check_doc(self):
        """Check if document is processed."""
        if not self.doc:
            messagebox.showwarning("Not Processed", "Please process text first!")
            return False
        return True
    
    def show_tokenization(self):
        if not self.check_doc():
            return
        
        columns = ("Token #", "Token")
        data = [(str(i), token.text) for i, token in enumerate(self.doc, start=1)]
        self.show_table(columns, data)
    
    def show_linguistic_annotation(self):
        if not self.check_doc():
            return
        
        columns = ("Token", "POS", "Lemma", "Dependency", "Entity")
        data = [
            (token.text, token.pos_, token.lemma_, token.dep_, token.ent_type_ or "-")
            for token in self.doc
        ]
        self.show_table(columns, data)
    
    def show_lemmatization(self):
        if not self.check_doc():
            return
        
        columns = ("Token", "Lemma")
        data = [(token.text, token.lemma_) for token in self.doc]
        self.show_table(columns, data)
    
    def show_sentence_detection(self):
        if not self.check_doc():
            return
        
        columns = ("Sentence #", "Sentence")
        data = [(str(i), sent.text) for i, sent in enumerate(self.doc.sents, start=1)]
        self.show_table(columns, data)
    
    def show_pos_tagging(self):
        if not self.check_doc():
            return
        
        columns = ("Token", "POS", "Tag", "Detail")
        data = [
            (token.text, token.pos_, token.tag_, spacy.explain(token.tag_) or "-")
            for token in self.doc
        ]
        self.show_table(columns, data)
    
    def show_ner(self):
        if not self.check_doc():
            return
        
        if not self.doc.ents:
            self.show_text("No named entities found in the text.")
            return
        
        columns = ("Entity", "Type", "Explanation")
        data = [
            (ent.text, ent.label_, spacy.explain(ent.label_) or "-")
            for ent in self.doc.ents
        ]
        self.show_table(columns, data)
    
    def show_stop_words(self):
        if not self.check_doc():
            return
        
        filtered_tokens = [token.text for token in self.doc if not token.is_stop]
        filtered_sent = " ".join(filtered_tokens)
        
        text = f"Original Text:\n{self.processed_text}\n\n"
        text += f"After Stop Word Removal:\n{filtered_sent}\n\n"
        text += f"Statistics:\n"
        text += f"  • Original tokens: {len(self.doc)}\n"
        text += f"  • After removal: {len(filtered_tokens)}\n"
        text += f"  • Stop words removed: {len(self.doc) - len(filtered_tokens)}"
        
        self.show_text(text)
    
    def show_dependency_parsing(self):
        if not self.check_doc():
            return
        
        columns = ("Token", "Dependency", "Head", "POS")
        data = [
            (token.text, token.dep_, token.head.text, token.pos_)
            for token in self.doc
        ]
        self.show_table(columns, data)


if __name__ == "__main__":
    root = tk.Tk()
    app = NLPApp(root)
    root.mainloop()