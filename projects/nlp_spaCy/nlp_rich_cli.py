import spacy
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

def main():
    # Welcome header
    console.print(Panel.fit(
        "[bold cyan]NLP Program[/bold cyan]\n"
        "Process text using spaCy library",
        border_style="cyan"
    ))
    
    # Loading spaCy model
    with console.status("[bold green]Loading spaCy model...", spinner="dots"):
        nlp = spacy.load("en_core_web_sm")
    
    console.print("[green]✓[/green] Model loaded successfully!\n")
    
    while True:
        text = Prompt.ask("[bold yellow]Enter text to analyze[/bold yellow] (or 'quit' to exit)")
        
        if text.lower() == 'quit':
            console.print(Panel("[cyan]Thank you for using the program. Goodbye![/cyan]", border_style="cyan"))
            break
            
        if not text.strip():
            console.print("[red]❌ Error: Please enter some text[/red]\n")
            continue
        
        # Process text
        with console.status("[bold green]Processing text...", spinner="dots"):
            doc = nlp(text)
        
        # Show what was processed
        console.print(Panel(
            f"[dim]{text}[/dim]", 
            title="[bold]Processed Text[/bold]", 
            border_style="green"
        ))
        
        # Operations menu loop
        operations_menu(doc)

def operations_menu(doc):
    while True:
        console.print()
        
        # Create menu panel
        menu_text = """[bold cyan]Choose an operation:[/bold cyan]

  💬 [bold white]1[/bold white]. Tokenization
  📝 [bold white]2[/bold white]. Linguistic Annotation
  🔤 [bold white]3[/bold white]. Lemmatization
  📄 [bold white]4[/bold white]. Sentence Detection
  🏷️  [bold white]5[/bold white]. POS Tagging
  🎯 [bold white]6[/bold white]. Named Entity Recognition
  🚫 [bold white]7[/bold white]. Stop Words Removal
  🔗 [bold white]8[/bold white]. Dependency Parsing
  🔄 [bold white]9[/bold white]. Analyze New Text
  👋 [bold white]0[/bold white]. Exit"""
        
        console.print(Panel(menu_text, border_style="cyan"))
        
        user_input = Prompt.ask("[bold yellow]Option[/bold yellow]").strip()
        
        if user_input == "1":
            console.print(Panel("[bold green]Tokenization[/bold green]", border_style="green"))
            tokenization(doc)
        elif user_input == "2":
            console.print(Panel("[bold green]Linguistic Annotations[/bold green]", border_style="green"))
            linguistical_annotation(doc)
        elif user_input == "3":
            console.print(Panel("[bold green]Lemmatization[/bold green]", border_style="green"))
            lemmatization(doc)
        elif user_input == "4":
            console.print(Panel("[bold green]Sentence Detection[/bold green]", border_style="green"))
            sentence_detection(doc)
        elif user_input == "5":
            console.print(Panel("[bold green]POS Tagging[/bold green]", border_style="green"))
            pos_tagging(doc)
        elif user_input == "6":
            console.print(Panel("[bold green]Named Entity Recognition[/bold green]", border_style="green"))
            ner(doc)
        elif user_input == "7":
            console.print(Panel("[bold green]Stop Words Removal[/bold green]", border_style="green"))
            remove_stop_words(doc)
        elif user_input == "8":
            console.print(Panel("[bold green]Dependency Parsing[/bold green]", border_style="green"))
            dependency_parsing(doc)
        elif user_input == "9":
            return  # Go back to text input
        elif user_input == "0":
            console.print(Panel("[cyan]Thank you for using the program. Goodbye![/cyan]", border_style="cyan"))
            exit()
        else:
            console.print(Panel("[red]❌ Invalid input! Please try again.[/red]", border_style="red"))

def tokenization(doc):
    table = Table(show_header=True, header_style="bold magenta", border_style="blue")
    table.add_column("Token #", style="cyan", justify="right")
    table.add_column("Token", style="yellow")
    
    for index, token in enumerate(doc, start=1):
        table.add_row(str(index), token.text)
    
    console.print(table)

def linguistical_annotation(doc):
    table = Table(show_header=True, header_style="bold magenta", border_style="blue")
    table.add_column("Token", style="yellow")
    table.add_column("POS", style="cyan")
    table.add_column("Lemma", style="green")
    table.add_column("Dependency", style="blue")
    table.add_column("Entity", style="red")
    
    for token in doc:
        table.add_row(
            token.text, 
            token.pos_, 
            token.lemma_, 
            token.dep_, 
            token.ent_type_ if token.ent_type_ else "-"
        )
    
    console.print(table)

def lemmatization(doc):
    table = Table(show_header=True, header_style="bold magenta", border_style="blue")
    table.add_column("Token", style="yellow")
    table.add_column("Lemma", style="green")
    
    for token in doc:
        table.add_row(token.text, token.lemma_)
    
    console.print(table)

def sentence_detection(doc):
    table = Table(show_header=True, header_style="bold magenta", border_style="blue")
    table.add_column("Sentence #", style="cyan", justify="right")
    table.add_column("Sentence", style="yellow")
    
    for index, sent in enumerate(doc.sents, start=1):
        table.add_row(str(index), sent.text)
    
    console.print(table)

def pos_tagging(doc):
    table = Table(show_header=True, header_style="bold magenta", border_style="blue")
    table.add_column("Token", style="yellow")
    table.add_column("POS", style="cyan")
    table.add_column("Tag", style="green")
    table.add_column("Detail", style="blue")
    
    for token in doc:
        table.add_row(
            token.text, 
            token.pos_, 
            token.tag_, 
            spacy.explain(token.tag_) if spacy.explain(token.tag_) else "-"
        )
    
    console.print(table)

def ner(doc):
    if not doc.ents:
        console.print("[yellow]No named entities found in the text.[/yellow]")
        return
    
    table = Table(show_header=True, header_style="bold magenta", border_style="blue")
    table.add_column("Entity", style="yellow")
    table.add_column("Type", style="cyan")
    table.add_column("Explanation", style="green")
    
    for ent in doc.ents:
        table.add_row(
            ent.text, 
            ent.label_,
            spacy.explain(ent.label_) if spacy.explain(ent.label_) else "-"
        )
    
    console.print(table)

def remove_stop_words(doc):
    filtered_tokens = [token.text for token in doc if not token.is_stop]
    filtered_sent = " ".join(filtered_tokens)
    
    console.print(Panel(
        f"[bold]Original:[/bold] {doc.text}\n\n[bold]After stop word removal:[/bold] [yellow]{filtered_sent}[/yellow]",
        border_style="green"
    ))

def dependency_parsing(doc):
    table = Table(show_header=True, header_style="bold magenta", border_style="blue")
    table.add_column("Token", style="yellow")
    table.add_column("Dependency", style="cyan")
    table.add_column("Head", style="green")
    table.add_column("POS", style="blue")
    
    for token in doc:
        table.add_row(
            token.text, 
            token.dep_, 
            token.head.text, 
            token.pos_
        )
    
    console.print(table)

if __name__ == "__main__":
    main()