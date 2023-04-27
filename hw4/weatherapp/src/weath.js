import React, { useEffect, useState } from "react";
import { View, Text, TextInput, StyleSheet, Button, ActivityIndicator } from "react-native";

function Weather() {
  const [inputValue, setInputValue] = useState("");
  const [data, setData] = useState(null);
  const [city, setCity] = useState("");
  const [loading, setLoading] = useState(false);
  const API_KEY = "2fce26b3009e0a66de8c0a0223800869";

  // function get temp data
  const getTempData = (api, query) => {
    setLoading(true);
    let url = `https://api.openweathermap.org/data/2.5/weather?q=${query}&units=metric&appid=${api}`;
    fetch(url)
      .then((res) => {
        return res.json();
      })
      .then((res) => {
        setData(res.main);
        setCity(query);
        setLoading(false);
        // console.log(res.main);
      })
      .catch((err) => {
        console.log("error in get data", err);
        setData(null);
        setLoading(false);
      });
  };

  const handleSubmit = () => {
    if (!inputValue.length) {
      return;
    }
    getTempData(API_KEY, inputValue);
  };

  return (
    <View>
      <Text>WELCOME TO OUR WEATHER APP</Text>
      <TextInput
        style={styles.input}
        placeholder="Enter City Name"
        value={inputValue}
        onChangeText={(text) => setInputValue(text)}
      />
      <Button title="Submit" disabled={loading} onPress={handleSubmit} />
      {loading ? (
        <ActivityIndicator style={styles.loader} size="large" color="#0000ff" />
      ) : !inputValue.length ? null : data ? (
        <View>
          <Text style={styles.city}>Weather Details of City : {city}</Text>

          <View style={styles.infoContainer}>
            <Text>Current Temperature : {data.temp} °C</Text>
            <Text>Feels Like : {data.feels_like}</Text>
            <Text>Temperature Min : {data.temp_min} °C</Text>
            <Text>Temperature Max : {data.temp_max} °C</Text>
            <Text>Humidity : {data.humidity}%</Text>
            <Text>Pressure : {data.pressure} pa</Text>
          </View>
        </View>
      ) : (
        <Text style={styles.validCity}>Enter Valid City Name</Text>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  input: {
    borderWidth: 1,
    borderColor: "gray",
    margin: 10,
    padding: 5,
  },
  city: {
    fontSize: 20,
    fontWeight: "bold",
    marginVertical: 10,
  },
  infoContainer: {
    margin: 10,
  },
  validCity: {
    color: "red",
    margin: 10,
  },
  loader: {
    marginVertical: 20,
  },
});

export default Weather;
