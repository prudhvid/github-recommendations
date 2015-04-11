import graphlab


sf = graphlab.SFrame({'user_id': ["0", "0", "0", "1", "1", "2", "2", "2"],'item_id': ["a", "b", "c", "a", "b", "b", "c", "d"],
                        'rating':["2", "2", "3", "1", "1", "2", "2", "2"]})
m = graphlab.recommender.create(sf)
nn = m.get_similar_items()
m2 = graphlab.create(sf, nearest_items=nn)
recs = m2.recommend()
print recs
