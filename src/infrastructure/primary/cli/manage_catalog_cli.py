import click

@click.group()
def cli():
    pass

@cli.command()
def create_product():
    click.echo("Creating a product...")

@cli.command()
def create_category():
    click.echo("Creating a category...")

if __name__ == '__main__':
    cli()
