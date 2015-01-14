try:
    from mw import api
except:
    raise

#Retrieve entries from the recentchanges feed.
def get_rc(limit, session):
  
  actions = session.recent_changes.query(
    type = "edit",
    properties = "ids", "sha1", "timestamp"},
    direction="newer",
    limit=limit
  )

  return actions
