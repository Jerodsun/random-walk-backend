# Random Walk Project

### August 2019

The purpose of this backend app is to generate json representations for the frontend.

Two very basic views have been implemented: `SampleDataView` and `BlackScholesView`.

**Regarding Random Walk / Brownian Motion**

The actual data itself does not have to be stored at all in a model; just use a wrapper to store the time and place it was called and the parameters. Use a hash of the time for the seed in order for randomization and reproducibility.

Have the complete design and DB implementation ready before moving on.

Use a separate `router` for the other implementations and change the link.

Migrations are not committed; do a `python manage.py makemigrations` on stage.

Regarding async, the question is whether using celery is overkill; I think it is, but it will allow the serve to handle multiple requests without defaulting to gunicorn.

```python
now = time.time()
np.random.seed(int(str(hash(now))[-8:])) # last 8 integers
```

Update 8/6/2019:

The original plan was to have a random walk and brownian motion implementation stored in one table, one model. But it appears that cross validation is unnecessarily complicated and, after all, that's what multiple tables are for. Therefore, they will be separated into two different models for each type of View.

Next step is to add FE/BE validations, so there's no ZeroDivisionError for example.

Seems to be some weird thing with not allowing .1 for volatility?
