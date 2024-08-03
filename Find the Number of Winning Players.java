class Solution {
    public int winningPlayerCount(int n, int[][] pick) {
        List<Map<Integer, Integer>> colorCount = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            colorCount.add(new HashMap<>());
        }
        for (int[] p : pick) {
            int player = p[0];
            int color = p[1];
            Map<Integer, Integer> countMap = colorCount.get(player);
            countMap.put(color, countMap.getOrDefault(color, 0) + 1);
        }
        int winners = 0;
        for (int i = 0; i < n; i++) {
            Map<Integer, Integer> countMap = colorCount.get(i);
            for (int count : countMap.values()) {
                if (count > i) {
                    winners++;
                    break;
                }
            }
        }

        return winners;
    }
}
