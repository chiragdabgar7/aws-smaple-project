class myblog {

    $app_path = "/srv/mezzanine"

    class {"supervisor": }

    require myblog::requirements

}
