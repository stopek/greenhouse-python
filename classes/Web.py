from libs.MicroWebCli.microWebCli import MicroWebCli


def get_json(url):
    wCli = MicroWebCli(url)
    wCli.OpenRequest()
    response = wCli.GetResponse()

    return response.ReadContentAsJSON()
