# Requests

## JSON

```json
const jsonObj = {
  "name": "Rick",
  "id": "11A",
  "level": 4
};
```

Also see: [JSON cheatsheet](/json)

## XMLHttpRequest

```javascript
const xhr = new XMLHttpRequest();
xhr.open("GET", "mysite.com/getjson");
```

`XMLHttpRequest` is a browser-level API that enables the client to script data transfers via JavaScript, NOT part of the
JavaScript language.

## GET

```javascript
const req = new XMLHttpRequest();
req.responseType = "json";
req.open("GET", "/getdata?id=65");
req.onload = () => {
  console.log(xhr.response);
};

req.send();
```

## POST

```javascript
const data = {
  fish: "Salmon",
  weight: "1.5 KG",
  units: 5,
};
const xhr = new XMLHttpRequest();
xhr.open("POST", "/inventory/add");
xhr.responseType = "json";
xhr.send(JSON.stringify(data));

xhr.onload = () => {
  console.log(xhr.response);
};
```

## fetch api

```javascript
fetch(url, {
    method: 'POST',
    headers: {
      'Content-type': 'application/json',
      'apikey': apiKey
    },
    body: data
  }).then(response => {
    if (response.ok) {
      return response.json();
    }
    throw new Error('Request failed!');
  }, networkError => {
    console.log(networkError.message)
  })
}
```

## JSON Formatted

```javascript
fetch("url-that-returns-JSON")
  .then((response) => response.json())
  .then((jsonResponse) => {
    console.log(jsonResponse);
  });
```

## promise url parameter fetch api

```javascript
fetch('url')
.then(
  response  => {
    console.log(response);
  },
 rejection => {
    console.error(rejection.message);
);
```

## Fetch API Function

```javascript
fetch("https://api-xxx.com/endpoint", {
  method: "POST",
  body: JSON.stringify({ id: "200" }),
})
  .then(
    (response) => {
      if (response.ok) {
        return response.json();
      }
      throw new Error("Request failed!");
    },
    (networkError) => {
      console.log(networkError.message);
    },
  )
  .then((jsonResponse) => {
    console.log(jsonResponse);
  });
```

## async await syntax

```javascript
const getSuggestions = async () => {
  const wordQuery = inputField.value;
  const endpoint = `${url}${queryParams}${wordQuery}`;
  try {
    const response = await fetch(endpoint, { cache: "no-cache" });
    if (response.ok) {
      const jsonResponse = await response.json();
    }
  } catch (error) {
    console.log(error);
  }
};
```
