// Package weather is weather packae.
package weather

// CurrentCondition var.
var CurrentCondition string
// CurrentLocation var.
var CurrentLocation string

// Forecast returns a formated string of the forcast of the given city and weather.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
