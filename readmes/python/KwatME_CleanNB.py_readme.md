Command-line program for cleaning `Julia` files (`.jl`) and `Jupyter Notebook`s (`.ipynb`) ๐งน

## Use

```bash
clean-jl luffy.jl
```

```bash
clean-jl zoro.ipynb
```

```bash
clean-jl nami.jl usopp.ipynb
```

```bash
find -E . -regex ".*/*\.(jl|ipynb)" -type f -print0 | xargs -0 clean-jl
```

## Install

```bash
git clone https://github.com/KwatMDPhD/Clean.jl &&

cd Clean.jl &&

julia --project --eval "using Pkg; Pkg.instantiate()" &&

julia --project deps/build.jl
```

โ๏ธ commands install `clean-jl` into `~/.julia/bin`.

If not already, add the `bin` to the path by adding ๐ to the profile (`~/.zshrc`, `~/.rc`, ...)

```bash
PATH=~/.julia/bin:$PATH
```

Start a new shell to load the updated profile.

Test installation

```bash
clean-jl --version
```

๐

---

## ๐ ๐ค  Howdy

To report a bug, request a feature, or leave a comment, just [submit an issue](https://github.com/KwatMDPhD/Clean.jl/issues/new/choose).

Powered by https://github.com/KwatMDPhD/Kata.jl ๐
