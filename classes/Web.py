from libs.MicroWebCli.microWebCli import MicroWebCli


def get_json(url):
    web_cli = MicroWebCli(url)
    web_cli.OpenRequest()
    response = web_cli.GetResponse()

    return response.ReadContentAsJSON()
