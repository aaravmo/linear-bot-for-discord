import requests

def handler(key: String):
  headers = {"Authorization": key, "Content-Type": 'application/json'}
  data = {"query": f''' {{
  issues(first: 100) {{
    edges {{
      node {{
        id
        title
        priority
        createdAt
        state {{
          name
        }}
        assignee {{
          name
        }}
      }}
      cursor
    }}
    pageInfo {{
      hasNextPage
      endCursor
    }}
  }}
}}'''
}
  r = requests.post('https://api.linear.app/graphql', headers=headers, json=data)
  return r.json()
