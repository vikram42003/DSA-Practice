package anotherone

import (
	"fmt"
	"strings"
)

type User struct {
	Name string
}

func preferedName(user User) (string, error) {
	name := strings.TrimSpace(user.Name)
	if name == "" {
		return "", fmt.Errorf("display name: name is empty")
	}
	return name, nil
}

func main() {
	name, err := preferedName(User{Name: " Mina "})
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(name)
}