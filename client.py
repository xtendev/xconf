if __name__ == "__main__":
    from xconf import Config

    c = Config("test.ini", "xten_")

    print(c)
    assert c.get("name") == "xtendev"
    assert c.get("project") == "xconf"
    assert c.get("non_existent_prop") is None
