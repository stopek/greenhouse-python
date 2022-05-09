from classes.MicroWebCli import MicroWebCli


def get_json(url: str):
    web_cli = MicroWebCli(url)
    web_cli.OpenRequest()
    response = web_cli.GetResponse()

    return response.ReadContentAsJSON()
