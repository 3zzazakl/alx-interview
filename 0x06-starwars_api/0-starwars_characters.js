#!/usr/bin/node

const request = require('request');

function getCharacters(urls) {
    if (!Array.isArray(urls) || urls.length === 0) return;
    request.get(urls[0], (_err, _res, body) => {
        if (_err) return console.error(_err);
        console.log(JSON.parse(body).name);
        getCharacters(urls.slice(1));
    });
}

request.get(
    'https://swapi-api.alx-tools.com/api/films/' + process.argv[2], (_err, _res, body) => {
        const characters = JSON.parse(body).characters;
        getCharacters(characters);
    }
);
