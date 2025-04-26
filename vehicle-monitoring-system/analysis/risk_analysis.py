from sklearn.cluster import DBSCAN

class RiskAnalyzer:
    def __init__(self, eps=0.5, min_samples=5):
        """初始化聚类分析器"""
        self.clusterer = DBSCAN(eps=eps, min_samples=min_samples)

    def analyze(self, locations):
        """执行风险点聚类"""
        clusters = self.clusterer.fit_predict(locations)
        risk_points = []
        for cluster_id in set(clusters):
            if cluster_id != -1:  # 排除噪声点
                cluster_points = [loc for loc, c in zip(locations, clusters) if c == cluster_id]
                risk_points.append({
                    'level': len(cluster_points),
                    'coordinates': np.mean(cluster_points, axis=0).tolist()
                })
        return sorted(risk_points, key=lambda x: x['level'], reverse=True)