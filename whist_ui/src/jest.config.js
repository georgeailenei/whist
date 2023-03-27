module.exports = {
    moduleFileExtentions : [
        "js",
        "json",
        "vue"
    ],
    transform : {
        ".*\\.(js)$": "babel-jest",
        ".*\\.(js)$": "vue-jest",
},
    testEnvironment : "jsdom"
}