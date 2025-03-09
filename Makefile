.PHONY: all setup generate-data run-pipeline clean lint format test

# 默认任务： 设置环境、生成数据并运行管道
all: setup generate-data run-pipeline

# 设置环境
setup:
	docker compose build
	docker compose up -d
	@echo "环境设置完成，容器已启动"

# 生成数据
generate-data:
	docker compose exec data_engine poetry run python -m src.data.generate_sample_data
	@echo "数据生成完成"

# 运行管道
run-pipeline:
	docker compose exec data_engine bash scripts/run_pipeline.sh
	@echo "管道运行完成"

# 清理
clean:
	rm -rf data/processed/* data/final/* logs/*.logs
	@echo "已清理数据和日志"
