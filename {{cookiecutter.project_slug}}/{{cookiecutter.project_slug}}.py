{% if cookiecutter.back_compatible_py2 == 'y' -%}
from __future__ import print_function
{%- endif %}

def main():
    print('Hello, {{cookiecutter.full_name}}!')

if __name__ == '__main__':
    main()