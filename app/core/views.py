from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, \
                  abort, jsonify
from app.core.repository import *
from app.core.forms import SearchForm

import pickle as pk
# from mtree import MTree

mod = Blueprint('core', __name__)
# tree = pk.load(open("./icsd_unq_tree_7.pk", "rb"))

# @mod.route('/')
# def index():
  #repository = Repository()
  #return (render_template('core/index.html', resources=repository.getResources()))

@mod.route('/')
def index():
    form = SearchForm()

    compounds = []
    scores = []
    time_taken = []
    total_count = 0

 #    return ("All good to here")

    if form.validate_on_submit():
        time_start = time.time()
        scores, total_count = ([5, 5, 5], [12, 1, 6]) # query_db(form)
 #        print(scores)
        time_taken = f"{time.time() - time_start:.2f}"

    return render_template('core/atomic_search.html', title='Search',
                                            form=form,
                                            compounds=compounds,
                                            scores = scores,
                                            total_count = total_count,
                                            num_results = form.results_to_display.data,
                                            time_taken = time_taken)
    
    
    import os
    x = os.getcwd()
    from app.mtree import MTree
    tree = pk.load(open("./elmdSearch/icsd_unq_tree_7.pk", "rb"))
    try:
        y = tree.search("NaCl", 2)
        return str(y) # ys.getsizeof(tree))
    except Exception as e:
        return str(e)

    try: 
        from mtree import MTree
    except Exception as e:
        y = str(e)
    return(f"{x}\n{y}")'''
