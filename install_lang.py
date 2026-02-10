from argostranslate import package

package.update_package_index()
available_packages = package.get_available_packages()

pkg = next(
    p for p in available_packages
    if p.from_code == "en" and p.to_code == "pt"
)

package.install_from_path(pkg.download())

print("Pacote en → pt instalado com sucesso")
