Scripts and data for the global test set, used in translation notebooks. 
* building_french_global_test_set.ipynb shows an example of building the test set for French. 
* building_global_test_set.ipynb lets you build a test set for any language by just changing the language code. 


# *Edits: Dlamini Lindelwa*

Based on the Masakhane Project. 
Did a lot of heavy editing on the scripts, this, eventually worked, follow below:

###

```shell
(venv) D:\B Eng\NMP - TRANSLATION\masakhane-mt-master\jw300_utils>python get_jw300.py ss --output_dir jw300
Loaded 3571 global test sentences to filter from the training/dev data.
Creating corpus for en-ss (1/1).
Loaded data and skipped 0 lines since contained in test set.
D:\B Eng\NMP - TRANSLATION\masakhane-mt-master\venv\lib\site-packages\pandas\util\_decorators.py:311: SettingWithCopyWarning:
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  return func(*args, **kwargs)

(venv) D:\B Eng\NMP - TRANSLATION\masakhane-mt-master\jw300_utils>
(venv) D:\B Eng\NMP - TRANSLATION\masakhane-mt-master\jw300_utils>
```