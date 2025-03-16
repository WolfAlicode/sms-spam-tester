import subprocess
import sys
def install_requirements():
    try:
        print(" chck for update")
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True
        )
    except subprocess.CalledProcessError:
        pass

install_requirements()
from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import partial
import api_list
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TimeElapsedColumn
from rich.prompt import Prompt
from rich.traceback import install

install()
console = Console()

def main():
    console.rule("[bold blue]API Call Runner[/bold blue]")
    phone = Prompt.ask("Enter the phone number in the format [green]09********[/green]")
    total_calls = int(Prompt.ask("Total number of API calls"))

    funcs = api_list.wrapped_api_functions
    all_partial_functions = [
        partial(funcs[i % len(funcs)], phone) for i in range(total_calls)
    ]

    console.print(f"Starting {total_calls} API calls using {len(funcs)} different functions...")

    # Use ThreadPoolExecutor along with a progress bar to show the execution status
    with Progress(
        SpinnerColumn(),
        "[progress.description]{task.description}",
        BarColumn(),
        "[progress.percentage]{task.percentage:>3.0f}%",
        TimeElapsedColumn(),
        console=console,
        transient=True
    ) as progress:
        task = progress.add_task("[cyan]Executing API calls...", total=total_calls)
        results = []
        with ThreadPoolExecutor(max_workers=3) as executor:
            future_to_func = {executor.submit(func): func for func in all_partial_functions}
            for future in as_completed(future_to_func):
                try:
                    result = future.result()
                    results.append(result)
                except Exception as exc:
                    console.print(f"[red]Error occurred: {exc}[/red]")
                progress.advance(task)

    console.rule("[bold green]All API calls completed[/bold green]")
    console.print(f"Number of successful API calls: [bold]{len(results)}[/bold]")

if __name__ == "__main__":
    main()
