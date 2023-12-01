package aoc

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func TestZip(t *testing.T) {
	as := []int{1, 2}
	bs := []int{3, 4}
	cs := []int{5, 6}
	zipped := Zip(as, bs, cs)

	require.Equal(t, [][]int{{1, 3, 5}, {2, 4, 6}}, zipped)
}

func TestZip_Rune(t *testing.T) {
	as := []rune{'a', 'b'}
	bs := []rune{'c', 'd'}
	cs := []rune{'e', 'f'}
	zipped := Zip(as, bs, cs)

	require.Equal(t, [][]rune{{'a', 'c', 'e'}, {'b', 'd', 'f'}}, zipped)
}
