# How to reproduce issue
- `git clone https://github.com/davidnemec/strawberry-mypy-issue-repo-project`
- `cd strawberry-mypy-issue-repo-project`
- `python -m venv .venv && source .venv/bin/activate`
- `pip install poetry && poetry install`

###  Pydantic model is from external library - fail/exception.
- `python -m mypy strawberry_mypy_issue_repo_project/models_not_working.py --ignore-missing-imports --show-traceback`
```
strawberry_mypy_issue_repo_project/models_not_working.py:7: error: INTERNAL ERROR -- Please try using mypy master on GitHub:
https://mypy.readthedocs.io/en/stable/common_issues.html#using-a-development-mypy-build
Please report a bug at https://github.com/python/mypy/issues
version: 1.7.0
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "mypy/semanal.py", line 6525, in accept
  File "mypy/nodes.py", line 1140, in accept
  File "mypy/semanal.py", line 1608, in visit_class_def
  File "mypy/semanal.py", line 1693, in analyze_class
  File "mypy/semanal.py", line 1727, in analyze_class_body_common
  File "mypy/semanal.py", line 1800, in apply_class_plugin_hooks
  File "/home/davis/git/product-detail/api/.venv/lib/python3.11/site-packages/strawberry/ext/mypy_plugin.py", line 402, in strawberry_pydantic_class_callback
    model_type = cast(Instance, _get_type_for_expr(model_expression, ctx.api))
                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/davis/git/product-detail/api/.venv/lib/python3.11/site-packages/strawberry/ext/mypy_plugin.py", line 134, in _get_type_for_expr
    raise InvalidNodeTypeException(sym.node)
InvalidNodeTypeException: Invalid node type: Var:nil(User)
strawberry_mypy_issue_repo_project/models_not_working.py:7: : note: use --pdb to drop into pdb
```
###  Pydantic model is locally - pass
- `python -m mypy strawberry_mypy_issue_repo_project/models_working.py --ignore-missing-imports --show-traceback`
