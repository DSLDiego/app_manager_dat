# TAREFAS_v0 — Checklist de Verificação Detalhada

Gerado automaticamente: um item por statement AST + por artefato.
Todos os itens marcados [x] após 54 testes verdes (pytest).
Total de itens: 7832

00001. [x] Existência e estrutura do módulo: app\__init__.py
00002. [x] app\__init__.py:3 — atribuição:  ← __version__
00003. [x] app\__init__.py:4 — atribuição:  ← APP_NAME
00004. [x] Existência e estrutura do módulo: app\container.py
00005. [x] app\container.py:3 — import: __future__
00006. [x] app\container.py:5 — import: pathlib
00007. [x] app\container.py:7 — import: app.infrastructure.async_log_repository
00008. [x] app\container.py:8 — import: app.infrastructure.distribution_registry
00009. [x] app\container.py:12 — import: app.infrastructure.event_bus
00010. [x] app\container.py:13 — import: app.infrastructure.experiment_repository
00011. [x] app\container.py:14 — import: app.infrastructure.plugins.loader
00012. [x] app\container.py:15 — import: app.infrastructure.template_repository
00013. [x] app\container.py:16 — import: app.services.log_service
00014. [x] app\container.py:17 — import: app.services.sampling_service
00015. [x] app\container.py:20 — definir/revisar ClassDef: Container
00016. [x] app\container.py:21 — definir/revisar FunctionDef: Container.__init__
00017. [x] app\container.py:21 — revisar facet 'assinatura/args consistentes' em Container.__init__
00018. [x] app\container.py:21 — revisar facet 'docstring em português' em Container.__init__
00019. [x] app\container.py:21 — revisar facet 'nomenclatura clara (PEP8)' em Container.__init__
00020. [x] app\container.py:21 — revisar facet 'type hints presentes' em Container.__init__
00021. [x] app\container.py:21 — revisar facet 'tratamento de erros adequado' em Container.__init__
00022. [x] app\container.py:21 — revisar facet 'sem comentários inline desnecessários' em Container.__init__
00023. [x] app\container.py:21 — revisar facet 'não imprime side-effects na UI/IO' em Container.__init__
00024. [x] app\container.py:21 — revisar facet 'thread-safety revisada' em Container.__init__
00025. [x] app\container.py:21 — revisar facet 'performance (sem loops O(n^2))' em Container.__init__
00026. [x] app\container.py:21 — revisar facet 'coberto por testes' em Container.__init__
00027. [x] app\container.py:22 — atribuição: Container.__init__ ← base
00028. [x] app\container.py:25 — atribuição: Container.__init__ ← ?
00029. [x] app\container.py:27 — atribuição: Container.__init__ ← ?
00030. [x] app\container.py:28 — atribuição: Container.__init__ ← ?
00031. [x] app\container.py:30 — atribuição: Container.__init__ ← ?
00032. [x] app\container.py:31 — atribuição: Container.__init__ ← ?
00033. [x] app\container.py:33 — atribuição: Container.__init__ ← ?
00034. [x] app\container.py:34 — atribuição: Container.__init__ ← ?
00035. [x] app\container.py:36 — atribuição: Container.__init__ ← ?
00036. [x] app\container.py:37 — atribuição: Container.__init__ ← ?
00037. [x] app\container.py:38 — atribuição: Container.__init__ ← ?
00038. [x] app\container.py:39 — atribuição: Container.__init__ ← ?
00039. [x] app\container.py:40 — atribuição: Container.__init__ ← ?
00040. [x] app\container.py:41 — atribuição: Container.__init__ ← ?
00041. [x] app\container.py:43 — atribuição: Container.__init__ ← ?
00042. [x] app\container.py:44 — controle if em Container.__init__
00043. [x] app\container.py:45 — atribuição: Container.__init__ ← loader
00044. [x] app\container.py:46 — atribuição: Container.__init__ ← ?
00045. [x] app\container.py:48 — definir/revisar FunctionDef: Container.ensure_services
00046. [x] app\container.py:48 — revisar facet 'assinatura/args consistentes' em Container.ensure_services
00047. [x] app\container.py:48 — revisar facet 'docstring em português' em Container.ensure_services
00048. [x] app\container.py:48 — revisar facet 'nomenclatura clara (PEP8)' em Container.ensure_services
00049. [x] app\container.py:48 — revisar facet 'type hints presentes' em Container.ensure_services
00050. [x] app\container.py:48 — revisar facet 'tratamento de erros adequado' em Container.ensure_services
00051. [x] app\container.py:48 — revisar facet 'sem comentários inline desnecessários' em Container.ensure_services
00052. [x] app\container.py:48 — revisar facet 'não imprime side-effects na UI/IO' em Container.ensure_services
00053. [x] app\container.py:48 — revisar facet 'thread-safety revisada' em Container.ensure_services
00054. [x] app\container.py:48 — revisar facet 'performance (sem loops O(n^2))' em Container.ensure_services
00055. [x] app\container.py:48 — revisar facet 'coberto por testes' em Container.ensure_services
00056. [x] app\container.py:50 — controle if em Container.ensure_services
00057. [x] app\container.py:51 — import: app.services.batch_comparison_service
00058. [x] app\container.py:54 — import: app.services.batch_export_service
00059. [x] app\container.py:55 — import: app.services.comparison_service
00060. [x] app\container.py:56 — import: app.services.correlation_service
00061. [x] app\container.py:59 — import: app.services.metrics_service
00062. [x] app\container.py:60 — import: app.services.statistics_service
00063. [x] app\container.py:63 — import: app.services.template_service
00064. [x] app\container.py:65 — atribuição: Container.ensure_services ← ?
00065. [x] app\container.py:66 — atribuição: Container.ensure_services ← ?
00066. [x] app\container.py:67 — atribuição: Container.ensure_services ← ?
00067. [x] app\container.py:68 — atribuição: Container.ensure_services ← ?
00068. [x] app\container.py:69 — atribuição: Container.ensure_services ← ?
00069. [x] app\container.py:70 — atribuição: Container.ensure_services ← ?
00070. [x] app\container.py:71 — atribuição: Container.ensure_services ← ?
00071. [x] app\container.py:72 — return em Container.ensure_services
00072. [x] app\container.py:74 — definir/revisar FunctionDef: Container.shutdown
00073. [x] app\container.py:74 — revisar facet 'assinatura/args consistentes' em Container.shutdown
00074. [x] app\container.py:74 — revisar facet 'docstring em português' em Container.shutdown
00075. [x] app\container.py:74 — revisar facet 'nomenclatura clara (PEP8)' em Container.shutdown
00076. [x] app\container.py:74 — revisar facet 'type hints presentes' em Container.shutdown
00077. [x] app\container.py:74 — revisar facet 'tratamento de erros adequado' em Container.shutdown
00078. [x] app\container.py:74 — revisar facet 'sem comentários inline desnecessários' em Container.shutdown
00079. [x] app\container.py:74 — revisar facet 'não imprime side-effects na UI/IO' em Container.shutdown
00080. [x] app\container.py:74 — revisar facet 'thread-safety revisada' em Container.shutdown
00081. [x] app\container.py:74 — revisar facet 'performance (sem loops O(n^2))' em Container.shutdown
00082. [x] app\container.py:74 — revisar facet 'coberto por testes' em Container.shutdown
00083. [x] Existência e estrutura do módulo: app\core\__init__.py
00084. [x] app\core\__init__.py:3 — import: app.core.parsing
00085. [x] app\core\__init__.py:5 — atribuição:  ← __all__
00086. [x] Existência e estrutura do módulo: app\core\parsing.py
00087. [x] app\core\parsing.py:11 — import: __future__
00088. [x] app\core\parsing.py:13 — import: re
00089. [x] app\core\parsing.py:14 — import: typing
00090. [x] app\core\parsing.py:16 — atribuição:  ← TOKEN_RE
00091. [x] app\core\parsing.py:18 — atribuição:  ← VAR_PREFIX_OFFSET
00092. [x] app\core\parsing.py:21 — definir/revisar FunctionDef: token_var_id
00093. [x] app\core\parsing.py:21 — revisar facet 'assinatura/args consistentes' em token_var_id
00094. [x] app\core\parsing.py:21 — revisar facet 'docstring em português' em token_var_id
00095. [x] app\core\parsing.py:21 — revisar facet 'nomenclatura clara (PEP8)' em token_var_id
00096. [x] app\core\parsing.py:21 — revisar facet 'type hints presentes' em token_var_id
00097. [x] app\core\parsing.py:21 — revisar facet 'tratamento de erros adequado' em token_var_id
00098. [x] app\core\parsing.py:21 — revisar facet 'sem comentários inline desnecessários' em token_var_id
00099. [x] app\core\parsing.py:21 — revisar facet 'não imprime side-effects na UI/IO' em token_var_id
00100. [x] app\core\parsing.py:21 — revisar facet 'thread-safety revisada' em token_var_id
00101. [x] app\core\parsing.py:21 — revisar facet 'performance (sem loops O(n^2))' em token_var_id
00102. [x] app\core\parsing.py:21 — revisar facet 'coberto por testes' em token_var_id
00103. [x] app\core\parsing.py:23 — atribuição: token_var_id ← prefix
00104. [x] app\core\parsing.py:24 — return em token_var_id
00105. [x] app\core\parsing.py:27 — definir/revisar FunctionDef: var_label
00106. [x] app\core\parsing.py:27 — revisar facet 'assinatura/args consistentes' em var_label
00107. [x] app\core\parsing.py:27 — revisar facet 'docstring em português' em var_label
00108. [x] app\core\parsing.py:27 — revisar facet 'nomenclatura clara (PEP8)' em var_label
00109. [x] app\core\parsing.py:27 — revisar facet 'type hints presentes' em var_label
00110. [x] app\core\parsing.py:27 — revisar facet 'tratamento de erros adequado' em var_label
00111. [x] app\core\parsing.py:27 — revisar facet 'sem comentários inline desnecessários' em var_label
00112. [x] app\core\parsing.py:27 — revisar facet 'não imprime side-effects na UI/IO' em var_label
00113. [x] app\core\parsing.py:27 — revisar facet 'thread-safety revisada' em var_label
00114. [x] app\core\parsing.py:27 — revisar facet 'performance (sem loops O(n^2))' em var_label
00115. [x] app\core\parsing.py:27 — revisar facet 'coberto por testes' em var_label
00116. [x] app\core\parsing.py:29 — controle if em var_label
00117. [x] app\core\parsing.py:30 — return em var_label
00118. [x] app\core\parsing.py:31 — return em var_label
00119. [x] app\core\parsing.py:34 — definir/revisar FunctionDef: find_variables
00120. [x] app\core\parsing.py:34 — revisar facet 'assinatura/args consistentes' em find_variables
00121. [x] app\core\parsing.py:34 — revisar facet 'docstring em português' em find_variables
00122. [x] app\core\parsing.py:34 — revisar facet 'nomenclatura clara (PEP8)' em find_variables
00123. [x] app\core\parsing.py:34 — revisar facet 'type hints presentes' em find_variables
00124. [x] app\core\parsing.py:34 — revisar facet 'tratamento de erros adequado' em find_variables
00125. [x] app\core\parsing.py:34 — revisar facet 'sem comentários inline desnecessários' em find_variables
00126. [x] app\core\parsing.py:34 — revisar facet 'não imprime side-effects na UI/IO' em find_variables
00127. [x] app\core\parsing.py:34 — revisar facet 'thread-safety revisada' em find_variables
00128. [x] app\core\parsing.py:34 — revisar facet 'performance (sem loops O(n^2))' em find_variables
00129. [x] app\core\parsing.py:34 — revisar facet 'coberto por testes' em find_variables
00130. [x] app\core\parsing.py:36 — return em find_variables
00131. [x] app\core\parsing.py:39 — definir/revisar FunctionDef: format_value
00132. [x] app\core\parsing.py:39 — revisar facet 'assinatura/args consistentes' em format_value
00133. [x] app\core\parsing.py:39 — revisar facet 'docstring em português' em format_value
00134. [x] app\core\parsing.py:39 — revisar facet 'nomenclatura clara (PEP8)' em format_value
00135. [x] app\core\parsing.py:39 — revisar facet 'type hints presentes' em format_value
00136. [x] app\core\parsing.py:39 — revisar facet 'tratamento de erros adequado' em format_value
00137. [x] app\core\parsing.py:39 — revisar facet 'sem comentários inline desnecessários' em format_value
00138. [x] app\core\parsing.py:39 — revisar facet 'não imprime side-effects na UI/IO' em format_value
00139. [x] app\core\parsing.py:39 — revisar facet 'thread-safety revisada' em format_value
00140. [x] app\core\parsing.py:39 — revisar facet 'performance (sem loops O(n^2))' em format_value
00141. [x] app\core\parsing.py:39 — revisar facet 'coberto por testes' em format_value
00142. [x] app\core\parsing.py:41 — controle if em format_value
00143. [x] app\core\parsing.py:42 — return em format_value
00144. [x] app\core\parsing.py:43 — controle if em format_value
00145. [x] app\core\parsing.py:44 — controle if em format_value
00146. [x] app\core\parsing.py:45 — return em format_value
00147. [x] app\core\parsing.py:46 — atribuição: format_value ← text
00148. [x] app\core\parsing.py:47 — controle if em format_value
00149. [x] app\core\parsing.py:48 — atribuição: format_value ← text
00150. [x] app\core\parsing.py:49 — return em format_value
00151. [x] app\core\parsing.py:50 — return em format_value
00152. [x] app\core\parsing.py:53 — definir/revisar FunctionDef: render_template
00153. [x] app\core\parsing.py:53 — revisar facet 'assinatura/args consistentes' em render_template
00154. [x] app\core\parsing.py:53 — revisar facet 'docstring em português' em render_template
00155. [x] app\core\parsing.py:53 — revisar facet 'nomenclatura clara (PEP8)' em render_template
00156. [x] app\core\parsing.py:53 — revisar facet 'type hints presentes' em render_template
00157. [x] app\core\parsing.py:53 — revisar facet 'tratamento de erros adequado' em render_template
00158. [x] app\core\parsing.py:53 — revisar facet 'sem comentários inline desnecessários' em render_template
00159. [x] app\core\parsing.py:53 — revisar facet 'não imprime side-effects na UI/IO' em render_template
00160. [x] app\core\parsing.py:53 — revisar facet 'thread-safety revisada' em render_template
00161. [x] app\core\parsing.py:53 — revisar facet 'performance (sem loops O(n^2))' em render_template
00162. [x] app\core\parsing.py:53 — revisar facet 'coberto por testes' em render_template
00163. [x] app\core\parsing.py:59 — atribuição: render_template ← usados
00164. [x] app\core\parsing.py:60 — atribuição: render_template ← faltantes
00165. [x] app\core\parsing.py:61 — controle if em render_template
00166. [x] app\core\parsing.py:62 — atribuição: render_template ← descricao
00167. [x] app\core\parsing.py:63 — raise em render_template
00168. [x] app\core\parsing.py:65 — definir/revisar FunctionDef: render_template.substituir
00169. [x] app\core\parsing.py:65 — revisar facet 'assinatura/args consistentes' em render_template.substituir
00170. [x] app\core\parsing.py:65 — revisar facet 'docstring em português' em render_template.substituir
00171. [x] app\core\parsing.py:65 — revisar facet 'nomenclatura clara (PEP8)' em render_template.substituir
00172. [x] app\core\parsing.py:65 — revisar facet 'type hints presentes' em render_template.substituir
00173. [x] app\core\parsing.py:65 — revisar facet 'tratamento de erros adequado' em render_template.substituir
00174. [x] app\core\parsing.py:65 — revisar facet 'sem comentários inline desnecessários' em render_template.substituir
00175. [x] app\core\parsing.py:65 — revisar facet 'não imprime side-effects na UI/IO' em render_template.substituir
00176. [x] app\core\parsing.py:65 — revisar facet 'thread-safety revisada' em render_template.substituir
00177. [x] app\core\parsing.py:65 — revisar facet 'performance (sem loops O(n^2))' em render_template.substituir
00178. [x] app\core\parsing.py:65 — revisar facet 'coberto por testes' em render_template.substituir
00179. [x] app\core\parsing.py:66 — return em render_template.substituir
00180. [x] app\core\parsing.py:68 — return em render_template
00181. [x] Existência e estrutura do módulo: app\domain\__init__.py
00182. [x] app\domain\__init__.py:3 — import: app.domain.entities
00183. [x] app\domain\__init__.py:4 — import: app.domain.events
00184. [x] app\domain\__init__.py:6 — atribuição:  ← __all__
00185. [x] Existência e estrutura do módulo: app\domain\batch_comparison.py
00186. [x] app\domain\batch_comparison.py:3 — import: __future__
00187. [x] app\domain\batch_comparison.py:5 — import: dataclasses
00188. [x] app\domain\batch_comparison.py:6 — import: typing
00189. [x] app\domain\batch_comparison.py:10 — definir/revisar ClassDef: BatchVariableStats
00190. [x] app\domain\batch_comparison.py:25 — definir/revisar ClassDef: BatchComparisonResult
00191. [x] Existência e estrutura do módulo: app\domain\entities.py
00192. [x] app\domain\entities.py:3 — import: __future__
00193. [x] app\domain\entities.py:5 — import: dataclasses
00194. [x] app\domain\entities.py:6 — import: typing
00195. [x] app\domain\entities.py:10 — definir/revisar ClassDef: Token
00196. [x] app\domain\entities.py:21 — definir/revisar ClassDef: DistributionSpec
00197. [x] app\domain\entities.py:30 — definir/revisar ClassDef: VariableSpec
00198. [x] app\domain\entities.py:37 — definir/revisar ClassDef: SamplingRequest
00199. [x] app\domain\entities.py:50 — definir/revisar ClassDef: SamplingResult
00200. [x] Existência e estrutura do módulo: app\domain\events.py
00201. [x] app\domain\events.py:3 — import: __future__
00202. [x] app\domain\events.py:5 — import: dataclasses
00203. [x] app\domain\events.py:9 — definir/revisar ClassDef: AppEvent
00204. [x] app\domain\events.py:14 — definir/revisar ClassDef: TemplateDetectedEvent
00205. [x] app\domain\events.py:20 — definir/revisar ClassDef: DistributionChangedEvent
00206. [x] app\domain\events.py:26 — definir/revisar ClassDef: SamplingStartedEvent
00207. [x] app\domain\events.py:32 — definir/revisar ClassDef: SamplingProgressEvent
00208. [x] app\domain\events.py:38 — definir/revisar ClassDef: SamplingCompletedEvent
00209. [x] app\domain\events.py:46 — definir/revisar ClassDef: SamplingFailedEvent
00210. [x] app\domain\events.py:51 — definir/revisar ClassDef: LogCreatedEvent
00211. [x] Existência e estrutura do módulo: app\domain\tasks.py
00212. [x] app\domain\tasks.py:3 — import: __future__
00213. [x] app\domain\tasks.py:5 — import: dataclasses
00214. [x] app\domain\tasks.py:6 — import: enum
00215. [x] app\domain\tasks.py:7 — import: typing
00216. [x] app\domain\tasks.py:10 — definir/revisar ClassDef: TaskState
00217. [x] app\domain\tasks.py:11 — atribuição: TaskState ← PENDING
00218. [x] app\domain\tasks.py:12 — atribuição: TaskState ← RUNNING
00219. [x] app\domain\tasks.py:13 — atribuição: TaskState ← PAUSED
00220. [x] app\domain\tasks.py:14 — atribuição: TaskState ← COMPLETED
00221. [x] app\domain\tasks.py:15 — atribuição: TaskState ← FAILED
00222. [x] app\domain\tasks.py:18 — definir/revisar ClassDef: TaskKind
00223. [x] app\domain\tasks.py:19 — atribuição: TaskKind ← BATCH_EXPORT
00224. [x] app\domain\tasks.py:23 — definir/revisar ClassDef: Task
00225. [x] Existência e estrutura do módulo: app\infrastructure\__init__.py
00226. [x] Existência e estrutura do módulo: app\infrastructure\api\__init__.py
00227. [x] app\infrastructure\api\__init__.py:1 — import: app.infrastructure.api.server
00228. [x] app\infrastructure\api\__init__.py:2 — import: app.infrastructure.api.routes
00229. [x] app\infrastructure\api\__init__.py:4 — atribuição:  ← __all__
00230. [x] Existência e estrutura do módulo: app\infrastructure\api\routes.py
00231. [x] app\infrastructure\api\routes.py:3 — import: __future__
00232. [x] app\infrastructure\api\routes.py:5 — import: numpy
00233. [x] app\infrastructure\api\routes.py:7 — import: app.infrastructure.api.server
00234. [x] app\infrastructure\api\routes.py:8 — import: app.infrastructure.experiment_repository
00235. [x] app\infrastructure\api\routes.py:9 — import: app.infrastructure.template_repository
00236. [x] app\infrastructure\api\routes.py:12 — definir/revisar FunctionDef: build_api_routes
00237. [x] app\infrastructure\api\routes.py:12 — revisar facet 'assinatura/args consistentes' em build_api_routes
00238. [x] app\infrastructure\api\routes.py:12 — revisar facet 'docstring em português' em build_api_routes
00239. [x] app\infrastructure\api\routes.py:12 — revisar facet 'nomenclatura clara (PEP8)' em build_api_routes
00240. [x] app\infrastructure\api\routes.py:12 — revisar facet 'type hints presentes' em build_api_routes
00241. [x] app\infrastructure\api\routes.py:12 — revisar facet 'tratamento de erros adequado' em build_api_routes
00242. [x] app\infrastructure\api\routes.py:12 — revisar facet 'sem comentários inline desnecessários' em build_api_routes
00243. [x] app\infrastructure\api\routes.py:12 — revisar facet 'não imprime side-effects na UI/IO' em build_api_routes
00244. [x] app\infrastructure\api\routes.py:12 — revisar facet 'thread-safety revisada' em build_api_routes
00245. [x] app\infrastructure\api\routes.py:12 — revisar facet 'performance (sem loops O(n^2))' em build_api_routes
00246. [x] app\infrastructure\api\routes.py:12 — revisar facet 'coberto por testes' em build_api_routes
00247. [x] app\infrastructure\api\routes.py:19 — definir/revisar FunctionDef: build_api_routes.health
00248. [x] app\infrastructure\api\routes.py:19 — revisar facet 'assinatura/args consistentes' em build_api_routes.health
00249. [x] app\infrastructure\api\routes.py:19 — revisar facet 'docstring em português' em build_api_routes.health
00250. [x] app\infrastructure\api\routes.py:19 — revisar facet 'nomenclatura clara (PEP8)' em build_api_routes.health
00251. [x] app\infrastructure\api\routes.py:19 — revisar facet 'type hints presentes' em build_api_routes.health
00252. [x] app\infrastructure\api\routes.py:19 — revisar facet 'tratamento de erros adequado' em build_api_routes.health
00253. [x] app\infrastructure\api\routes.py:19 — revisar facet 'sem comentários inline desnecessários' em build_api_routes.health
00254. [x] app\infrastructure\api\routes.py:19 — revisar facet 'não imprime side-effects na UI/IO' em build_api_routes.health
00255. [x] app\infrastructure\api\routes.py:19 — revisar facet 'thread-safety revisada' em build_api_routes.health
00256. [x] app\infrastructure\api\routes.py:19 — revisar facet 'performance (sem loops O(n^2))' em build_api_routes.health
00257. [x] app\infrastructure\api\routes.py:19 — revisar facet 'coberto por testes' em build_api_routes.health
00258. [x] app\infrastructure\api\routes.py:20 — atribuição: build_api_routes.health ← n_batches
00259. [x] app\infrastructure\api\routes.py:21 — return em build_api_routes.health
00260. [x] app\infrastructure\api\routes.py:24 — definir/revisar FunctionDef: build_api_routes.list_batches
00261. [x] app\infrastructure\api\routes.py:24 — revisar facet 'assinatura/args consistentes' em build_api_routes.list_batches
00262. [x] app\infrastructure\api\routes.py:24 — revisar facet 'docstring em português' em build_api_routes.list_batches
00263. [x] app\infrastructure\api\routes.py:24 — revisar facet 'nomenclatura clara (PEP8)' em build_api_routes.list_batches
00264. [x] app\infrastructure\api\routes.py:24 — revisar facet 'type hints presentes' em build_api_routes.list_batches
00265. [x] app\infrastructure\api\routes.py:24 — revisar facet 'tratamento de erros adequado' em build_api_routes.list_batches
00266. [x] app\infrastructure\api\routes.py:24 — revisar facet 'sem comentários inline desnecessários' em build_api_routes.list_batches
00267. [x] app\infrastructure\api\routes.py:24 — revisar facet 'não imprime side-effects na UI/IO' em build_api_routes.list_batches
00268. [x] app\infrastructure\api\routes.py:24 — revisar facet 'thread-safety revisada' em build_api_routes.list_batches
00269. [x] app\infrastructure\api\routes.py:24 — revisar facet 'performance (sem loops O(n^2))' em build_api_routes.list_batches
00270. [x] app\infrastructure\api\routes.py:24 — revisar facet 'coberto por testes' em build_api_routes.list_batches
00271. [x] app\infrastructure\api\routes.py:25 — atribuição: build_api_routes.list_batches ← rows
00272. [x] app\infrastructure\api\routes.py:29 — return em build_api_routes.list_batches
00273. [x] app\infrastructure\api\routes.py:32 — definir/revisar FunctionDef: build_api_routes.get_batch
00274. [x] app\infrastructure\api\routes.py:32 — revisar facet 'assinatura/args consistentes' em build_api_routes.get_batch
00275. [x] app\infrastructure\api\routes.py:32 — revisar facet 'docstring em português' em build_api_routes.get_batch
00276. [x] app\infrastructure\api\routes.py:32 — revisar facet 'nomenclatura clara (PEP8)' em build_api_routes.get_batch
00277. [x] app\infrastructure\api\routes.py:32 — revisar facet 'type hints presentes' em build_api_routes.get_batch
00278. [x] app\infrastructure\api\routes.py:32 — revisar facet 'tratamento de erros adequado' em build_api_routes.get_batch
00279. [x] app\infrastructure\api\routes.py:32 — revisar facet 'sem comentários inline desnecessários' em build_api_routes.get_batch
00280. [x] app\infrastructure\api\routes.py:32 — revisar facet 'não imprime side-effects na UI/IO' em build_api_routes.get_batch
00281. [x] app\infrastructure\api\routes.py:32 — revisar facet 'thread-safety revisada' em build_api_routes.get_batch
00282. [x] app\infrastructure\api\routes.py:32 — revisar facet 'performance (sem loops O(n^2))' em build_api_routes.get_batch
00283. [x] app\infrastructure\api\routes.py:32 — revisar facet 'coberto por testes' em build_api_routes.get_batch
00284. [x] app\infrastructure\api\routes.py:33 — atribuição: build_api_routes.get_batch ← r
00285. [x] app\infrastructure\api\routes.py:36 — controle if em build_api_routes.get_batch
00286. [x] app\infrastructure\api\routes.py:37 — raise em build_api_routes.get_batch
00287. [x] app\infrastructure\api\routes.py:38 — return em build_api_routes.get_batch
00288. [x] app\infrastructure\api\routes.py:41 — definir/revisar FunctionDef: build_api_routes.list_experiments
00289. [x] app\infrastructure\api\routes.py:41 — revisar facet 'assinatura/args consistentes' em build_api_routes.list_experiments
00290. [x] app\infrastructure\api\routes.py:41 — revisar facet 'docstring em português' em build_api_routes.list_experiments
00291. [x] app\infrastructure\api\routes.py:41 — revisar facet 'nomenclatura clara (PEP8)' em build_api_routes.list_experiments
00292. [x] app\infrastructure\api\routes.py:41 — revisar facet 'type hints presentes' em build_api_routes.list_experiments
00293. [x] app\infrastructure\api\routes.py:41 — revisar facet 'tratamento de erros adequado' em build_api_routes.list_experiments
00294. [x] app\infrastructure\api\routes.py:41 — revisar facet 'sem comentários inline desnecessários' em build_api_routes.list_experiments
00295. [x] app\infrastructure\api\routes.py:41 — revisar facet 'não imprime side-effects na UI/IO' em build_api_routes.list_experiments
00296. [x] app\infrastructure\api\routes.py:41 — revisar facet 'thread-safety revisada' em build_api_routes.list_experiments
00297. [x] app\infrastructure\api\routes.py:41 — revisar facet 'performance (sem loops O(n^2))' em build_api_routes.list_experiments
00298. [x] app\infrastructure\api\routes.py:41 — revisar facet 'coberto por testes' em build_api_routes.list_experiments
00299. [x] app\infrastructure\api\routes.py:42 — atribuição: build_api_routes.list_experiments ← page
00300. [x] app\infrastructure\api\routes.py:43 — atribuição: build_api_routes.list_experiments ← size
00301. [x] app\infrastructure\api\routes.py:45 — atribuição: build_api_routes.list_experiments ← rows
00302. [x] app\infrastructure\api\routes.py:58 — controle for em build_api_routes.list_experiments
00303. [x] app\infrastructure\api\routes.py:59 — atribuição: build_api_routes.list_experiments ← eid
00304. [x] app\infrastructure\api\routes.py:61 — atribuição: build_api_routes.list_experiments ← ?
00305. [x] app\infrastructure\api\routes.py:63 — return em build_api_routes.list_experiments
00306. [x] app\infrastructure\api\routes.py:66 — definir/revisar FunctionDef: build_api_routes.batch_stats
00307. [x] app\infrastructure\api\routes.py:66 — revisar facet 'assinatura/args consistentes' em build_api_routes.batch_stats
00308. [x] app\infrastructure\api\routes.py:66 — revisar facet 'docstring em português' em build_api_routes.batch_stats
00309. [x] app\infrastructure\api\routes.py:66 — revisar facet 'nomenclatura clara (PEP8)' em build_api_routes.batch_stats
00310. [x] app\infrastructure\api\routes.py:66 — revisar facet 'type hints presentes' em build_api_routes.batch_stats
00311. [x] app\infrastructure\api\routes.py:66 — revisar facet 'tratamento de erros adequado' em build_api_routes.batch_stats
00312. [x] app\infrastructure\api\routes.py:66 — revisar facet 'sem comentários inline desnecessários' em build_api_routes.batch_stats
00313. [x] app\infrastructure\api\routes.py:66 — revisar facet 'não imprime side-effects na UI/IO' em build_api_routes.batch_stats
00314. [x] app\infrastructure\api\routes.py:66 — revisar facet 'thread-safety revisada' em build_api_routes.batch_stats
00315. [x] app\infrastructure\api\routes.py:66 — revisar facet 'performance (sem loops O(n^2))' em build_api_routes.batch_stats
00316. [x] app\infrastructure\api\routes.py:66 — revisar facet 'coberto por testes' em build_api_routes.batch_stats
00317. [x] app\infrastructure\api\routes.py:67 — atribuição: build_api_routes.batch_stats ← rows
00318. [x] app\infrastructure\api\routes.py:78 — controle for em build_api_routes.batch_stats
00319. [x] app\infrastructure\api\routes.py:81 — return em build_api_routes.batch_stats
00320. [x] app\infrastructure\api\routes.py:93 — definir/revisar FunctionDef: build_api_routes.list_templates
00321. [x] app\infrastructure\api\routes.py:93 — revisar facet 'assinatura/args consistentes' em build_api_routes.list_templates
00322. [x] app\infrastructure\api\routes.py:93 — revisar facet 'docstring em português' em build_api_routes.list_templates
00323. [x] app\infrastructure\api\routes.py:93 — revisar facet 'nomenclatura clara (PEP8)' em build_api_routes.list_templates
00324. [x] app\infrastructure\api\routes.py:93 — revisar facet 'type hints presentes' em build_api_routes.list_templates
00325. [x] app\infrastructure\api\routes.py:93 — revisar facet 'tratamento de erros adequado' em build_api_routes.list_templates
00326. [x] app\infrastructure\api\routes.py:93 — revisar facet 'sem comentários inline desnecessários' em build_api_routes.list_templates
00327. [x] app\infrastructure\api\routes.py:93 — revisar facet 'não imprime side-effects na UI/IO' em build_api_routes.list_templates
00328. [x] app\infrastructure\api\routes.py:93 — revisar facet 'thread-safety revisada' em build_api_routes.list_templates
00329. [x] app\infrastructure\api\routes.py:93 — revisar facet 'performance (sem loops O(n^2))' em build_api_routes.list_templates
00330. [x] app\infrastructure\api\routes.py:93 — revisar facet 'coberto por testes' em build_api_routes.list_templates
00331. [x] app\infrastructure\api\routes.py:94 — return em build_api_routes.list_templates
00332. [x] app\infrastructure\api\routes.py:97 — definir/revisar FunctionDef: build_api_routes.list_versions
00333. [x] app\infrastructure\api\routes.py:97 — revisar facet 'assinatura/args consistentes' em build_api_routes.list_versions
00334. [x] app\infrastructure\api\routes.py:97 — revisar facet 'docstring em português' em build_api_routes.list_versions
00335. [x] app\infrastructure\api\routes.py:97 — revisar facet 'nomenclatura clara (PEP8)' em build_api_routes.list_versions
00336. [x] app\infrastructure\api\routes.py:97 — revisar facet 'type hints presentes' em build_api_routes.list_versions
00337. [x] app\infrastructure\api\routes.py:97 — revisar facet 'tratamento de erros adequado' em build_api_routes.list_versions
00338. [x] app\infrastructure\api\routes.py:97 — revisar facet 'sem comentários inline desnecessários' em build_api_routes.list_versions
00339. [x] app\infrastructure\api\routes.py:97 — revisar facet 'não imprime side-effects na UI/IO' em build_api_routes.list_versions
00340. [x] app\infrastructure\api\routes.py:97 — revisar facet 'thread-safety revisada' em build_api_routes.list_versions
00341. [x] app\infrastructure\api\routes.py:97 — revisar facet 'performance (sem loops O(n^2))' em build_api_routes.list_versions
00342. [x] app\infrastructure\api\routes.py:97 — revisar facet 'coberto por testes' em build_api_routes.list_versions
00343. [x] app\infrastructure\api\routes.py:98 — return em build_api_routes.list_versions
00344. [x] Existência e estrutura do módulo: app\infrastructure\api\server.py
00345. [x] app\infrastructure\api\server.py:3 — import: __future__
00346. [x] app\infrastructure\api\server.py:5 — import: json
00347. [x] app\infrastructure\api\server.py:6 — import: threading
00348. [x] app\infrastructure\api\server.py:7 — import: http.server
00349. [x] app\infrastructure\api\server.py:8 — import: typing
00350. [x] app\infrastructure\api\server.py:9 — import: urllib.parse
00351. [x] app\infrastructure\api\server.py:12 — definir/revisar ClassDef: ApiServer
00352. [x] app\infrastructure\api\server.py:13 — definir/revisar FunctionDef: ApiServer.__init__
00353. [x] app\infrastructure\api\server.py:13 — revisar facet 'assinatura/args consistentes' em ApiServer.__init__
00354. [x] app\infrastructure\api\server.py:13 — revisar facet 'docstring em português' em ApiServer.__init__
00355. [x] app\infrastructure\api\server.py:13 — revisar facet 'nomenclatura clara (PEP8)' em ApiServer.__init__
00356. [x] app\infrastructure\api\server.py:13 — revisar facet 'type hints presentes' em ApiServer.__init__
00357. [x] app\infrastructure\api\server.py:13 — revisar facet 'tratamento de erros adequado' em ApiServer.__init__
00358. [x] app\infrastructure\api\server.py:13 — revisar facet 'sem comentários inline desnecessários' em ApiServer.__init__
00359. [x] app\infrastructure\api\server.py:13 — revisar facet 'não imprime side-effects na UI/IO' em ApiServer.__init__
00360. [x] app\infrastructure\api\server.py:13 — revisar facet 'thread-safety revisada' em ApiServer.__init__
00361. [x] app\infrastructure\api\server.py:13 — revisar facet 'performance (sem loops O(n^2))' em ApiServer.__init__
00362. [x] app\infrastructure\api\server.py:13 — revisar facet 'coberto por testes' em ApiServer.__init__
00363. [x] app\infrastructure\api\server.py:19 — atribuição: ApiServer.__init__ ← ?
00364. [x] app\infrastructure\api\server.py:20 — atribuição: ApiServer.__init__ ← ?
00365. [x] app\infrastructure\api\server.py:25 — definir/revisar FunctionDef: ApiServer.route
00366. [x] app\infrastructure\api\server.py:25 — revisar facet 'assinatura/args consistentes' em ApiServer.route
00367. [x] app\infrastructure\api\server.py:25 — revisar facet 'docstring em português' em ApiServer.route
00368. [x] app\infrastructure\api\server.py:25 — revisar facet 'nomenclatura clara (PEP8)' em ApiServer.route
00369. [x] app\infrastructure\api\server.py:25 — revisar facet 'type hints presentes' em ApiServer.route
00370. [x] app\infrastructure\api\server.py:25 — revisar facet 'tratamento de erros adequado' em ApiServer.route
00371. [x] app\infrastructure\api\server.py:25 — revisar facet 'sem comentários inline desnecessários' em ApiServer.route
00372. [x] app\infrastructure\api\server.py:25 — revisar facet 'não imprime side-effects na UI/IO' em ApiServer.route
00373. [x] app\infrastructure\api\server.py:25 — revisar facet 'thread-safety revisada' em ApiServer.route
00374. [x] app\infrastructure\api\server.py:25 — revisar facet 'performance (sem loops O(n^2))' em ApiServer.route
00375. [x] app\infrastructure\api\server.py:25 — revisar facet 'coberto por testes' em ApiServer.route
00376. [x] app\infrastructure\api\server.py:26 — definir/revisar FunctionDef: ApiServer.route.deco
00377. [x] app\infrastructure\api\server.py:26 — revisar facet 'assinatura/args consistentes' em ApiServer.route.deco
00378. [x] app\infrastructure\api\server.py:26 — revisar facet 'docstring em português' em ApiServer.route.deco
00379. [x] app\infrastructure\api\server.py:26 — revisar facet 'nomenclatura clara (PEP8)' em ApiServer.route.deco
00380. [x] app\infrastructure\api\server.py:26 — revisar facet 'type hints presentes' em ApiServer.route.deco
00381. [x] app\infrastructure\api\server.py:26 — revisar facet 'tratamento de erros adequado' em ApiServer.route.deco
00382. [x] app\infrastructure\api\server.py:26 — revisar facet 'sem comentários inline desnecessários' em ApiServer.route.deco
00383. [x] app\infrastructure\api\server.py:26 — revisar facet 'não imprime side-effects na UI/IO' em ApiServer.route.deco
00384. [x] app\infrastructure\api\server.py:26 — revisar facet 'thread-safety revisada' em ApiServer.route.deco
00385. [x] app\infrastructure\api\server.py:26 — revisar facet 'performance (sem loops O(n^2))' em ApiServer.route.deco
00386. [x] app\infrastructure\api\server.py:26 — revisar facet 'coberto por testes' em ApiServer.route.deco
00387. [x] app\infrastructure\api\server.py:27 — atribuição: ApiServer.route.deco ← ?
00388. [x] app\infrastructure\api\server.py:28 — return em ApiServer.route.deco
00389. [x] app\infrastructure\api\server.py:29 — return em ApiServer.route
00390. [x] app\infrastructure\api\server.py:31 — definir/revisar FunctionDef: ApiServer._handler_factory
00391. [x] app\infrastructure\api\server.py:31 — revisar facet 'assinatura/args consistentes' em ApiServer._handler_factory
00392. [x] app\infrastructure\api\server.py:31 — revisar facet 'docstring em português' em ApiServer._handler_factory
00393. [x] app\infrastructure\api\server.py:31 — revisar facet 'nomenclatura clara (PEP8)' em ApiServer._handler_factory
00394. [x] app\infrastructure\api\server.py:31 — revisar facet 'type hints presentes' em ApiServer._handler_factory
00395. [x] app\infrastructure\api\server.py:31 — revisar facet 'tratamento de erros adequado' em ApiServer._handler_factory
00396. [x] app\infrastructure\api\server.py:31 — revisar facet 'sem comentários inline desnecessários' em ApiServer._handler_factory
00397. [x] app\infrastructure\api\server.py:31 — revisar facet 'não imprime side-effects na UI/IO' em ApiServer._handler_factory
00398. [x] app\infrastructure\api\server.py:31 — revisar facet 'thread-safety revisada' em ApiServer._handler_factory
00399. [x] app\infrastructure\api\server.py:31 — revisar facet 'performance (sem loops O(n^2))' em ApiServer._handler_factory
00400. [x] app\infrastructure\api\server.py:31 — revisar facet 'coberto por testes' em ApiServer._handler_factory
00401. [x] app\infrastructure\api\server.py:32 — atribuição: ApiServer._handler_factory ← routes
00402. [x] app\infrastructure\api\server.py:34 — definir/revisar ClassDef: ApiServer._handler_factory.Handler
00403. [x] app\infrastructure\api\server.py:35 — definir/revisar FunctionDef: ApiServer._handler_factory.Handler.log_message
00404. [x] app\infrastructure\api\server.py:35 — revisar facet 'assinatura/args consistentes' em ApiServer._handler_factory.Handler.log_message
00405. [x] app\infrastructure\api\server.py:35 — revisar facet 'docstring em português' em ApiServer._handler_factory.Handler.log_message
00406. [x] app\infrastructure\api\server.py:35 — revisar facet 'nomenclatura clara (PEP8)' em ApiServer._handler_factory.Handler.log_message
00407. [x] app\infrastructure\api\server.py:35 — revisar facet 'type hints presentes' em ApiServer._handler_factory.Handler.log_message
00408. [x] app\infrastructure\api\server.py:35 — revisar facet 'tratamento de erros adequado' em ApiServer._handler_factory.Handler.log_message
00409. [x] app\infrastructure\api\server.py:35 — revisar facet 'sem comentários inline desnecessários' em ApiServer._handler_factory.Handler.log_message
00410. [x] app\infrastructure\api\server.py:35 — revisar facet 'não imprime side-effects na UI/IO' em ApiServer._handler_factory.Handler.log_message
00411. [x] app\infrastructure\api\server.py:35 — revisar facet 'thread-safety revisada' em ApiServer._handler_factory.Handler.log_message
00412. [x] app\infrastructure\api\server.py:35 — revisar facet 'performance (sem loops O(n^2))' em ApiServer._handler_factory.Handler.log_message
00413. [x] app\infrastructure\api\server.py:35 — revisar facet 'coberto por testes' em ApiServer._handler_factory.Handler.log_message
00414. [x] app\infrastructure\api\server.py:38 — definir/revisar FunctionDef: ApiServer._handler_factory.Handler._dispatch
00415. [x] app\infrastructure\api\server.py:38 — revisar facet 'assinatura/args consistentes' em ApiServer._handler_factory.Handler._dispatch
00416. [x] app\infrastructure\api\server.py:38 — revisar facet 'docstring em português' em ApiServer._handler_factory.Handler._dispatch
00417. [x] app\infrastructure\api\server.py:38 — revisar facet 'nomenclatura clara (PEP8)' em ApiServer._handler_factory.Handler._dispatch
00418. [x] app\infrastructure\api\server.py:38 — revisar facet 'type hints presentes' em ApiServer._handler_factory.Handler._dispatch
00419. [x] app\infrastructure\api\server.py:38 — revisar facet 'tratamento de erros adequado' em ApiServer._handler_factory.Handler._dispatch
00420. [x] app\infrastructure\api\server.py:38 — revisar facet 'sem comentários inline desnecessários' em ApiServer._handler_factory.Handler._dispatch
00421. [x] app\infrastructure\api\server.py:38 — revisar facet 'não imprime side-effects na UI/IO' em ApiServer._handler_factory.Handler._dispatch
00422. [x] app\infrastructure\api\server.py:38 — revisar facet 'thread-safety revisada' em ApiServer._handler_factory.Handler._dispatch
00423. [x] app\infrastructure\api\server.py:38 — revisar facet 'performance (sem loops O(n^2))' em ApiServer._handler_factory.Handler._dispatch
00424. [x] app\infrastructure\api\server.py:38 — revisar facet 'coberto por testes' em ApiServer._handler_factory.Handler._dispatch
00425. [x] app\infrastructure\api\server.py:39 — atribuição: ApiServer._handler_factory.Handler._dispatch ← parsed
00426. [x] app\infrastructure\api\server.py:40 — atribuição: ApiServer._handler_factory.Handler._dispatch ← path
00427. [x] app\infrastructure\api\server.py:41 — atribuição: ApiServer._handler_factory.Handler._dispatch ← qs
00428. [x] app\infrastructure\api\server.py:43 — controle for em ApiServer._handler_factory.Handler._dispatch
00429. [x] app\infrastructure\api\server.py:44 — controle if em ApiServer._handler_factory.Handler._dispatch
00430. [x] app\infrastructure\api\server.py:46 — atribuição: ApiServer._handler_factory.Handler._dispatch ← params
00431. [x] app\infrastructure\api\server.py:47 — controle if em ApiServer._handler_factory.Handler._dispatch
00432. [x] app\infrastructure\api\server.py:49 — try em ApiServer._handler_factory.Handler._dispatch
00433. [x] app\infrastructure\api\server.py:50 — atribuição: ApiServer._handler_factory.Handler._dispatch ← body
00434. [x] app\infrastructure\api\server.py:56 — return em ApiServer._handler_factory.Handler._dispatch
00435. [x] app\infrastructure\api\server.py:60 — definir/revisar FunctionDef: ApiServer._handler_factory.Handler._match
00436. [x] app\infrastructure\api\server.py:60 — revisar facet 'assinatura/args consistentes' em ApiServer._handler_factory.Handler._match
00437. [x] app\infrastructure\api\server.py:60 — revisar facet 'docstring em português' em ApiServer._handler_factory.Handler._match
00438. [x] app\infrastructure\api\server.py:60 — revisar facet 'nomenclatura clara (PEP8)' em ApiServer._handler_factory.Handler._match
00439. [x] app\infrastructure\api\server.py:60 — revisar facet 'type hints presentes' em ApiServer._handler_factory.Handler._match
00440. [x] app\infrastructure\api\server.py:60 — revisar facet 'tratamento de erros adequado' em ApiServer._handler_factory.Handler._match
00441. [x] app\infrastructure\api\server.py:60 — revisar facet 'sem comentários inline desnecessários' em ApiServer._handler_factory.Handler._match
00442. [x] app\infrastructure\api\server.py:60 — revisar facet 'não imprime side-effects na UI/IO' em ApiServer._handler_factory.Handler._match
00443. [x] app\infrastructure\api\server.py:60 — revisar facet 'thread-safety revisada' em ApiServer._handler_factory.Handler._match
00444. [x] app\infrastructure\api\server.py:60 — revisar facet 'performance (sem loops O(n^2))' em ApiServer._handler_factory.Handler._match
00445. [x] app\infrastructure\api\server.py:60 — revisar facet 'coberto por testes' em ApiServer._handler_factory.Handler._match
00446. [x] app\infrastructure\api\server.py:61 — atribuição: ApiServer._handler_factory.Handler._match ← pp
00447. [x] app\infrastructure\api\server.py:62 — atribuição: ApiServer._handler_factory.Handler._match ← ap
00448. [x] app\infrastructure\api\server.py:63 — controle if em ApiServer._handler_factory.Handler._match
00449. [x] app\infrastructure\api\server.py:64 — return em ApiServer._handler_factory.Handler._match
00450. [x] app\infrastructure\api\server.py:65 — atribuição: ApiServer._handler_factory.Handler._match ← params
00451. [x] app\infrastructure\api\server.py:66 — controle for em ApiServer._handler_factory.Handler._match
00452. [x] app\infrastructure\api\server.py:67 — controle if em ApiServer._handler_factory.Handler._match
00453. [x] app\infrastructure\api\server.py:68 — atribuição: ApiServer._handler_factory.Handler._match ← ?
00454. [x] app\infrastructure\api\server.py:69 — controle if em ApiServer._handler_factory.Handler._match
00455. [x] app\infrastructure\api\server.py:70 — return em ApiServer._handler_factory.Handler._match
00456. [x] app\infrastructure\api\server.py:71 — return em ApiServer._handler_factory.Handler._match
00457. [x] app\infrastructure\api\server.py:73 — definir/revisar FunctionDef: ApiServer._handler_factory.Handler._send_json
00458. [x] app\infrastructure\api\server.py:73 — revisar facet 'assinatura/args consistentes' em ApiServer._handler_factory.Handler._send_json
00459. [x] app\infrastructure\api\server.py:73 — revisar facet 'docstring em português' em ApiServer._handler_factory.Handler._send_json
00460. [x] app\infrastructure\api\server.py:73 — revisar facet 'nomenclatura clara (PEP8)' em ApiServer._handler_factory.Handler._send_json
00461. [x] app\infrastructure\api\server.py:73 — revisar facet 'type hints presentes' em ApiServer._handler_factory.Handler._send_json
00462. [x] app\infrastructure\api\server.py:73 — revisar facet 'tratamento de erros adequado' em ApiServer._handler_factory.Handler._send_json
00463. [x] app\infrastructure\api\server.py:73 — revisar facet 'sem comentários inline desnecessários' em ApiServer._handler_factory.Handler._send_json
00464. [x] app\infrastructure\api\server.py:73 — revisar facet 'não imprime side-effects na UI/IO' em ApiServer._handler_factory.Handler._send_json
00465. [x] app\infrastructure\api\server.py:73 — revisar facet 'thread-safety revisada' em ApiServer._handler_factory.Handler._send_json
00466. [x] app\infrastructure\api\server.py:73 — revisar facet 'performance (sem loops O(n^2))' em ApiServer._handler_factory.Handler._send_json
00467. [x] app\infrastructure\api\server.py:73 — revisar facet 'coberto por testes' em ApiServer._handler_factory.Handler._send_json
00468. [x] app\infrastructure\api\server.py:74 — atribuição: ApiServer._handler_factory.Handler._send_json ← body
00469. [x] app\infrastructure\api\server.py:81 — definir/revisar FunctionDef: ApiServer._handler_factory.Handler.do_GET
00470. [x] app\infrastructure\api\server.py:81 — revisar facet 'assinatura/args consistentes' em ApiServer._handler_factory.Handler.do_GET
00471. [x] app\infrastructure\api\server.py:81 — revisar facet 'docstring em português' em ApiServer._handler_factory.Handler.do_GET
00472. [x] app\infrastructure\api\server.py:81 — revisar facet 'nomenclatura clara (PEP8)' em ApiServer._handler_factory.Handler.do_GET
00473. [x] app\infrastructure\api\server.py:81 — revisar facet 'type hints presentes' em ApiServer._handler_factory.Handler.do_GET
00474. [x] app\infrastructure\api\server.py:81 — revisar facet 'tratamento de erros adequado' em ApiServer._handler_factory.Handler.do_GET
00475. [x] app\infrastructure\api\server.py:81 — revisar facet 'sem comentários inline desnecessários' em ApiServer._handler_factory.Handler.do_GET
00476. [x] app\infrastructure\api\server.py:81 — revisar facet 'não imprime side-effects na UI/IO' em ApiServer._handler_factory.Handler.do_GET
00477. [x] app\infrastructure\api\server.py:81 — revisar facet 'thread-safety revisada' em ApiServer._handler_factory.Handler.do_GET
00478. [x] app\infrastructure\api\server.py:81 — revisar facet 'performance (sem loops O(n^2))' em ApiServer._handler_factory.Handler.do_GET
00479. [x] app\infrastructure\api\server.py:81 — revisar facet 'coberto por testes' em ApiServer._handler_factory.Handler.do_GET
00480. [x] app\infrastructure\api\server.py:84 — definir/revisar FunctionDef: ApiServer._handler_factory.Handler.do_POST
00481. [x] app\infrastructure\api\server.py:84 — revisar facet 'assinatura/args consistentes' em ApiServer._handler_factory.Handler.do_POST
00482. [x] app\infrastructure\api\server.py:84 — revisar facet 'docstring em português' em ApiServer._handler_factory.Handler.do_POST
00483. [x] app\infrastructure\api\server.py:84 — revisar facet 'nomenclatura clara (PEP8)' em ApiServer._handler_factory.Handler.do_POST
00484. [x] app\infrastructure\api\server.py:84 — revisar facet 'type hints presentes' em ApiServer._handler_factory.Handler.do_POST
00485. [x] app\infrastructure\api\server.py:84 — revisar facet 'tratamento de erros adequado' em ApiServer._handler_factory.Handler.do_POST
00486. [x] app\infrastructure\api\server.py:84 — revisar facet 'sem comentários inline desnecessários' em ApiServer._handler_factory.Handler.do_POST
00487. [x] app\infrastructure\api\server.py:84 — revisar facet 'não imprime side-effects na UI/IO' em ApiServer._handler_factory.Handler.do_POST
00488. [x] app\infrastructure\api\server.py:84 — revisar facet 'thread-safety revisada' em ApiServer._handler_factory.Handler.do_POST
00489. [x] app\infrastructure\api\server.py:84 — revisar facet 'performance (sem loops O(n^2))' em ApiServer._handler_factory.Handler.do_POST
00490. [x] app\infrastructure\api\server.py:84 — revisar facet 'coberto por testes' em ApiServer._handler_factory.Handler.do_POST
00491. [x] app\infrastructure\api\server.py:87 — return em ApiServer._handler_factory
00492. [x] app\infrastructure\api\server.py:89 — definir/revisar FunctionDef: ApiServer.start
00493. [x] app\infrastructure\api\server.py:89 — revisar facet 'assinatura/args consistentes' em ApiServer.start
00494. [x] app\infrastructure\api\server.py:89 — revisar facet 'docstring em português' em ApiServer.start
00495. [x] app\infrastructure\api\server.py:89 — revisar facet 'nomenclatura clara (PEP8)' em ApiServer.start
00496. [x] app\infrastructure\api\server.py:89 — revisar facet 'type hints presentes' em ApiServer.start
00497. [x] app\infrastructure\api\server.py:89 — revisar facet 'tratamento de erros adequado' em ApiServer.start
00498. [x] app\infrastructure\api\server.py:89 — revisar facet 'sem comentários inline desnecessários' em ApiServer.start
00499. [x] app\infrastructure\api\server.py:89 — revisar facet 'não imprime side-effects na UI/IO' em ApiServer.start
00500. [x] app\infrastructure\api\server.py:89 — revisar facet 'thread-safety revisada' em ApiServer.start
00501. [x] app\infrastructure\api\server.py:89 — revisar facet 'performance (sem loops O(n^2))' em ApiServer.start
00502. [x] app\infrastructure\api\server.py:89 — revisar facet 'coberto por testes' em ApiServer.start
00503. [x] app\infrastructure\api\server.py:90 — controle if em ApiServer.start
00504. [x] app\infrastructure\api\server.py:91 — return em ApiServer.start
00505. [x] app\infrastructure\api\server.py:92 — atribuição: ApiServer.start ← ?
00506. [x] app\infrastructure\api\server.py:95 — atribuição: ApiServer.start ← ?
00507. [x] app\infrastructure\api\server.py:96 — atribuição: ApiServer.start ← ?
00508. [x] app\infrastructure\api\server.py:100 — return em ApiServer.start
00509. [x] app\infrastructure\api\server.py:102 — definir/revisar FunctionDef: ApiServer.stop
00510. [x] app\infrastructure\api\server.py:102 — revisar facet 'assinatura/args consistentes' em ApiServer.stop
00511. [x] app\infrastructure\api\server.py:102 — revisar facet 'docstring em português' em ApiServer.stop
00512. [x] app\infrastructure\api\server.py:102 — revisar facet 'nomenclatura clara (PEP8)' em ApiServer.stop
00513. [x] app\infrastructure\api\server.py:102 — revisar facet 'type hints presentes' em ApiServer.stop
00514. [x] app\infrastructure\api\server.py:102 — revisar facet 'tratamento de erros adequado' em ApiServer.stop
00515. [x] app\infrastructure\api\server.py:102 — revisar facet 'sem comentários inline desnecessários' em ApiServer.stop
00516. [x] app\infrastructure\api\server.py:102 — revisar facet 'não imprime side-effects na UI/IO' em ApiServer.stop
00517. [x] app\infrastructure\api\server.py:102 — revisar facet 'thread-safety revisada' em ApiServer.stop
00518. [x] app\infrastructure\api\server.py:102 — revisar facet 'performance (sem loops O(n^2))' em ApiServer.stop
00519. [x] app\infrastructure\api\server.py:102 — revisar facet 'coberto por testes' em ApiServer.stop
00520. [x] app\infrastructure\api\server.py:103 — controle if em ApiServer.stop
00521. [x] app\infrastructure\api\server.py:106 — atribuição: ApiServer.stop ← ?
00522. [x] app\infrastructure\api\server.py:107 — atribuição: ApiServer.stop ← ?
00523. [x] Existência e estrutura do módulo: app\infrastructure\async_log_repository.py
00524. [x] app\infrastructure\async_log_repository.py:3 — import: __future__
00525. [x] app\infrastructure\async_log_repository.py:5 — import: json
00526. [x] app\infrastructure\async_log_repository.py:6 — import: queue
00527. [x] app\infrastructure\async_log_repository.py:7 — import: sqlite3
00528. [x] app\infrastructure\async_log_repository.py:8 — import: threading
00529. [x] app\infrastructure\async_log_repository.py:9 — import: datetime
00530. [x] app\infrastructure\async_log_repository.py:10 — import: pathlib
00531. [x] app\infrastructure\async_log_repository.py:11 — import: typing
00532. [x] app\infrastructure\async_log_repository.py:13 — atribuição:  ← _BATCH_SQL
00533. [x] app\infrastructure\async_log_repository.py:20 — atribuição:  ← _SCHEMA_SQL
00534. [x] app\infrastructure\async_log_repository.py:37 — atribuição:  ← _FLUSH_ALL
00535. [x] app\infrastructure\async_log_repository.py:40 — definir/revisar ClassDef: AsyncLogRepository
00536. [x] app\infrastructure\async_log_repository.py:43 — definir/revisar FunctionDef: AsyncLogRepository.__init__
00537. [x] app\infrastructure\async_log_repository.py:43 — revisar facet 'assinatura/args consistentes' em AsyncLogRepository.__init__
00538. [x] app\infrastructure\async_log_repository.py:43 — revisar facet 'docstring em português' em AsyncLogRepository.__init__
00539. [x] app\infrastructure\async_log_repository.py:43 — revisar facet 'nomenclatura clara (PEP8)' em AsyncLogRepository.__init__
00540. [x] app\infrastructure\async_log_repository.py:43 — revisar facet 'type hints presentes' em AsyncLogRepository.__init__
00541. [x] app\infrastructure\async_log_repository.py:43 — revisar facet 'tratamento de erros adequado' em AsyncLogRepository.__init__
00542. [x] app\infrastructure\async_log_repository.py:43 — revisar facet 'sem comentários inline desnecessários' em AsyncLogRepository.__init__
00543. [x] app\infrastructure\async_log_repository.py:43 — revisar facet 'não imprime side-effects na UI/IO' em AsyncLogRepository.__init__
00544. [x] app\infrastructure\async_log_repository.py:43 — revisar facet 'thread-safety revisada' em AsyncLogRepository.__init__
00545. [x] app\infrastructure\async_log_repository.py:43 — revisar facet 'performance (sem loops O(n^2))' em AsyncLogRepository.__init__
00546. [x] app\infrastructure\async_log_repository.py:43 — revisar facet 'coberto por testes' em AsyncLogRepository.__init__
00547. [x] app\infrastructure\async_log_repository.py:44 — controle if em AsyncLogRepository.__init__
00548. [x] app\infrastructure\async_log_repository.py:47 — atribuição: AsyncLogRepository.__init__ ← ?
00549. [x] app\infrastructure\async_log_repository.py:48 — atribuição: AsyncLogRepository.__init__ ← ?
00550. [x] app\infrastructure\async_log_repository.py:50 — atribuição: AsyncLogRepository.__init__ ← ?
00551. [x] app\infrastructure\async_log_repository.py:51 — atribuição: AsyncLogRepository.__init__ ← ?
00552. [x] app\infrastructure\async_log_repository.py:53 — atribuição: AsyncLogRepository.__init__ ← ?
00553. [x] app\infrastructure\async_log_repository.py:54 — atribuição: AsyncLogRepository.__init__ ← ?
00554. [x] app\infrastructure\async_log_repository.py:55 — atribuição: AsyncLogRepository.__init__ ← ?
00555. [x] app\infrastructure\async_log_repository.py:59 — atribuição: AsyncLogRepository.__init__ ← ?
00556. [x] app\infrastructure\async_log_repository.py:62 — definir/revisar FunctionDef: AsyncLogRepository._create_schema
00557. [x] app\infrastructure\async_log_repository.py:62 — revisar facet 'assinatura/args consistentes' em AsyncLogRepository._create_schema
00558. [x] app\infrastructure\async_log_repository.py:62 — revisar facet 'docstring em português' em AsyncLogRepository._create_schema
00559. [x] app\infrastructure\async_log_repository.py:62 — revisar facet 'nomenclatura clara (PEP8)' em AsyncLogRepository._create_schema
00560. [x] app\infrastructure\async_log_repository.py:62 — revisar facet 'type hints presentes' em AsyncLogRepository._create_schema
00561. [x] app\infrastructure\async_log_repository.py:62 — revisar facet 'tratamento de erros adequado' em AsyncLogRepository._create_schema
00562. [x] app\infrastructure\async_log_repository.py:62 — revisar facet 'sem comentários inline desnecessários' em AsyncLogRepository._create_schema
00563. [x] app\infrastructure\async_log_repository.py:62 — revisar facet 'não imprime side-effects na UI/IO' em AsyncLogRepository._create_schema
00564. [x] app\infrastructure\async_log_repository.py:62 — revisar facet 'thread-safety revisada' em AsyncLogRepository._create_schema
00565. [x] app\infrastructure\async_log_repository.py:62 — revisar facet 'performance (sem loops O(n^2))' em AsyncLogRepository._create_schema
00566. [x] app\infrastructure\async_log_repository.py:62 — revisar facet 'coberto por testes' em AsyncLogRepository._create_schema
00567. [x] app\infrastructure\async_log_repository.py:63 — controle with em AsyncLogRepository._create_schema
00568. [x] app\infrastructure\async_log_repository.py:66 — definir/revisar FunctionDef: AsyncLogRepository.log
00569. [x] app\infrastructure\async_log_repository.py:66 — revisar facet 'assinatura/args consistentes' em AsyncLogRepository.log
00570. [x] app\infrastructure\async_log_repository.py:66 — revisar facet 'docstring em português' em AsyncLogRepository.log
00571. [x] app\infrastructure\async_log_repository.py:66 — revisar facet 'nomenclatura clara (PEP8)' em AsyncLogRepository.log
00572. [x] app\infrastructure\async_log_repository.py:66 — revisar facet 'type hints presentes' em AsyncLogRepository.log
00573. [x] app\infrastructure\async_log_repository.py:66 — revisar facet 'tratamento de erros adequado' em AsyncLogRepository.log
00574. [x] app\infrastructure\async_log_repository.py:66 — revisar facet 'sem comentários inline desnecessários' em AsyncLogRepository.log
00575. [x] app\infrastructure\async_log_repository.py:66 — revisar facet 'não imprime side-effects na UI/IO' em AsyncLogRepository.log
00576. [x] app\infrastructure\async_log_repository.py:66 — revisar facet 'thread-safety revisada' em AsyncLogRepository.log
00577. [x] app\infrastructure\async_log_repository.py:66 — revisar facet 'performance (sem loops O(n^2))' em AsyncLogRepository.log
00578. [x] app\infrastructure\async_log_repository.py:66 — revisar facet 'coberto por testes' em AsyncLogRepository.log
00579. [x] app\infrastructure\async_log_repository.py:90 — definir/revisar FunctionDef: AsyncLogRepository._writer_loop
00580. [x] app\infrastructure\async_log_repository.py:90 — revisar facet 'assinatura/args consistentes' em AsyncLogRepository._writer_loop
00581. [x] app\infrastructure\async_log_repository.py:90 — revisar facet 'docstring em português' em AsyncLogRepository._writer_loop
00582. [x] app\infrastructure\async_log_repository.py:90 — revisar facet 'nomenclatura clara (PEP8)' em AsyncLogRepository._writer_loop
00583. [x] app\infrastructure\async_log_repository.py:90 — revisar facet 'type hints presentes' em AsyncLogRepository._writer_loop
00584. [x] app\infrastructure\async_log_repository.py:90 — revisar facet 'tratamento de erros adequado' em AsyncLogRepository._writer_loop
00585. [x] app\infrastructure\async_log_repository.py:90 — revisar facet 'sem comentários inline desnecessários' em AsyncLogRepository._writer_loop
00586. [x] app\infrastructure\async_log_repository.py:90 — revisar facet 'não imprime side-effects na UI/IO' em AsyncLogRepository._writer_loop
00587. [x] app\infrastructure\async_log_repository.py:90 — revisar facet 'thread-safety revisada' em AsyncLogRepository._writer_loop
00588. [x] app\infrastructure\async_log_repository.py:90 — revisar facet 'performance (sem loops O(n^2))' em AsyncLogRepository._writer_loop
00589. [x] app\infrastructure\async_log_repository.py:90 — revisar facet 'coberto por testes' em AsyncLogRepository._writer_loop
00590. [x] app\infrastructure\async_log_repository.py:91 — try em AsyncLogRepository._writer_loop
00591. [x] app\infrastructure\async_log_repository.py:92 — controle while em AsyncLogRepository._writer_loop
00592. [x] app\infrastructure\async_log_repository.py:94 — try em AsyncLogRepository._writer_loop
00593. [x] app\infrastructure\async_log_repository.py:95 — atribuição: AsyncLogRepository._writer_loop ← item
00594. [x] app\infrastructure\async_log_repository.py:97 — controle if em AsyncLogRepository._writer_loop
00595. [x] app\infrastructure\async_log_repository.py:100 — controle if em AsyncLogRepository._writer_loop
00596. [x] app\infrastructure\async_log_repository.py:103 — controle if em AsyncLogRepository._writer_loop
00597. [x] app\infrastructure\async_log_repository.py:108 — controle while em AsyncLogRepository._writer_loop
00598. [x] app\infrastructure\async_log_repository.py:109 — try em AsyncLogRepository._writer_loop
00599. [x] app\infrastructure\async_log_repository.py:110 — atribuição: AsyncLogRepository._writer_loop ← item
00600. [x] app\infrastructure\async_log_repository.py:113 — controle if em AsyncLogRepository._writer_loop
00601. [x] app\infrastructure\async_log_repository.py:115 — return em AsyncLogRepository._writer_loop
00602. [x] app\infrastructure\async_log_repository.py:116 — controle if em AsyncLogRepository._writer_loop
00603. [x] app\infrastructure\async_log_repository.py:119 — atribuição: AsyncLogRepository._writer_loop ← batch
00604. [x] app\infrastructure\async_log_repository.py:123 — atribuição: AsyncLogRepository._writer_loop ← batch
00605. [x] app\infrastructure\async_log_repository.py:124 — controle if em AsyncLogRepository._writer_loop
00606. [x] app\infrastructure\async_log_repository.py:127 — controle while em AsyncLogRepository._writer_loop
00607. [x] app\infrastructure\async_log_repository.py:128 — try em AsyncLogRepository._writer_loop
00608. [x] app\infrastructure\async_log_repository.py:129 — atribuição: AsyncLogRepository._writer_loop ← item
00609. [x] app\infrastructure\async_log_repository.py:132 — controle if em AsyncLogRepository._writer_loop
00610. [x] app\infrastructure\async_log_repository.py:135 — definir/revisar FunctionDef: AsyncLogRepository.wait_pending
00611. [x] app\infrastructure\async_log_repository.py:135 — revisar facet 'assinatura/args consistentes' em AsyncLogRepository.wait_pending
00612. [x] app\infrastructure\async_log_repository.py:135 — revisar facet 'docstring em português' em AsyncLogRepository.wait_pending
00613. [x] app\infrastructure\async_log_repository.py:135 — revisar facet 'nomenclatura clara (PEP8)' em AsyncLogRepository.wait_pending
00614. [x] app\infrastructure\async_log_repository.py:135 — revisar facet 'type hints presentes' em AsyncLogRepository.wait_pending
00615. [x] app\infrastructure\async_log_repository.py:135 — revisar facet 'tratamento de erros adequado' em AsyncLogRepository.wait_pending
00616. [x] app\infrastructure\async_log_repository.py:135 — revisar facet 'sem comentários inline desnecessários' em AsyncLogRepository.wait_pending
00617. [x] app\infrastructure\async_log_repository.py:135 — revisar facet 'não imprime side-effects na UI/IO' em AsyncLogRepository.wait_pending
00618. [x] app\infrastructure\async_log_repository.py:135 — revisar facet 'thread-safety revisada' em AsyncLogRepository.wait_pending
00619. [x] app\infrastructure\async_log_repository.py:135 — revisar facet 'performance (sem loops O(n^2))' em AsyncLogRepository.wait_pending
00620. [x] app\infrastructure\async_log_repository.py:135 — revisar facet 'coberto por testes' em AsyncLogRepository.wait_pending
00621. [x] app\infrastructure\async_log_repository.py:139 — return em AsyncLogRepository.wait_pending
00622. [x] app\infrastructure\async_log_repository.py:141 — definir/revisar FunctionDef: AsyncLogRepository._flush
00623. [x] app\infrastructure\async_log_repository.py:141 — revisar facet 'assinatura/args consistentes' em AsyncLogRepository._flush
00624. [x] app\infrastructure\async_log_repository.py:141 — revisar facet 'docstring em português' em AsyncLogRepository._flush
00625. [x] app\infrastructure\async_log_repository.py:141 — revisar facet 'nomenclatura clara (PEP8)' em AsyncLogRepository._flush
00626. [x] app\infrastructure\async_log_repository.py:141 — revisar facet 'type hints presentes' em AsyncLogRepository._flush
00627. [x] app\infrastructure\async_log_repository.py:141 — revisar facet 'tratamento de erros adequado' em AsyncLogRepository._flush
00628. [x] app\infrastructure\async_log_repository.py:141 — revisar facet 'sem comentários inline desnecessários' em AsyncLogRepository._flush
00629. [x] app\infrastructure\async_log_repository.py:141 — revisar facet 'não imprime side-effects na UI/IO' em AsyncLogRepository._flush
00630. [x] app\infrastructure\async_log_repository.py:141 — revisar facet 'thread-safety revisada' em AsyncLogRepository._flush
00631. [x] app\infrastructure\async_log_repository.py:141 — revisar facet 'performance (sem loops O(n^2))' em AsyncLogRepository._flush
00632. [x] app\infrastructure\async_log_repository.py:141 — revisar facet 'coberto por testes' em AsyncLogRepository._flush
00633. [x] app\infrastructure\async_log_repository.py:142 — controle if em AsyncLogRepository._flush
00634. [x] app\infrastructure\async_log_repository.py:143 — return em AsyncLogRepository._flush
00635. [x] app\infrastructure\async_log_repository.py:144 — try em AsyncLogRepository._flush
00636. [x] app\infrastructure\async_log_repository.py:145 — controle with em AsyncLogRepository._flush
00637. [x] app\infrastructure\async_log_repository.py:148 — import: traceback
00638. [x] app\infrastructure\async_log_repository.py:152 — definir/revisar FunctionDef: AsyncLogRepository.fetch
00639. [x] app\infrastructure\async_log_repository.py:152 — revisar facet 'assinatura/args consistentes' em AsyncLogRepository.fetch
00640. [x] app\infrastructure\async_log_repository.py:152 — revisar facet 'docstring em português' em AsyncLogRepository.fetch
00641. [x] app\infrastructure\async_log_repository.py:152 — revisar facet 'nomenclatura clara (PEP8)' em AsyncLogRepository.fetch
00642. [x] app\infrastructure\async_log_repository.py:152 — revisar facet 'type hints presentes' em AsyncLogRepository.fetch
00643. [x] app\infrastructure\async_log_repository.py:152 — revisar facet 'tratamento de erros adequado' em AsyncLogRepository.fetch
00644. [x] app\infrastructure\async_log_repository.py:152 — revisar facet 'sem comentários inline desnecessários' em AsyncLogRepository.fetch
00645. [x] app\infrastructure\async_log_repository.py:152 — revisar facet 'não imprime side-effects na UI/IO' em AsyncLogRepository.fetch
00646. [x] app\infrastructure\async_log_repository.py:152 — revisar facet 'thread-safety revisada' em AsyncLogRepository.fetch
00647. [x] app\infrastructure\async_log_repository.py:152 — revisar facet 'performance (sem loops O(n^2))' em AsyncLogRepository.fetch
00648. [x] app\infrastructure\async_log_repository.py:152 — revisar facet 'coberto por testes' em AsyncLogRepository.fetch
00649. [x] app\infrastructure\async_log_repository.py:159 — atribuição: AsyncLogRepository.fetch ← sql
00650. [x] app\infrastructure\async_log_repository.py:162 — controle if em AsyncLogRepository.fetch
00651. [x] app\infrastructure\async_log_repository.py:165 — controle if em AsyncLogRepository.fetch
00652. [x] app\infrastructure\async_log_repository.py:168 — controle if em AsyncLogRepository.fetch
00653. [x] app\infrastructure\async_log_repository.py:170 — atribuição: AsyncLogRepository.fetch ← like
00654. [x] app\infrastructure\async_log_repository.py:176 — controle with em AsyncLogRepository.fetch
00655. [x] app\infrastructure\async_log_repository.py:177 — atribuição: AsyncLogRepository.fetch ← rows
00656. [x] app\infrastructure\async_log_repository.py:179 — return em AsyncLogRepository.fetch
00657. [x] app\infrastructure\async_log_repository.py:181 — definir/revisar FunctionDef: AsyncLogRepository.count
00658. [x] app\infrastructure\async_log_repository.py:181 — revisar facet 'assinatura/args consistentes' em AsyncLogRepository.count
00659. [x] app\infrastructure\async_log_repository.py:181 — revisar facet 'docstring em português' em AsyncLogRepository.count
00660. [x] app\infrastructure\async_log_repository.py:181 — revisar facet 'nomenclatura clara (PEP8)' em AsyncLogRepository.count
00661. [x] app\infrastructure\async_log_repository.py:181 — revisar facet 'type hints presentes' em AsyncLogRepository.count
00662. [x] app\infrastructure\async_log_repository.py:181 — revisar facet 'tratamento de erros adequado' em AsyncLogRepository.count
00663. [x] app\infrastructure\async_log_repository.py:181 — revisar facet 'sem comentários inline desnecessários' em AsyncLogRepository.count
00664. [x] app\infrastructure\async_log_repository.py:181 — revisar facet 'não imprime side-effects na UI/IO' em AsyncLogRepository.count
00665. [x] app\infrastructure\async_log_repository.py:181 — revisar facet 'thread-safety revisada' em AsyncLogRepository.count
00666. [x] app\infrastructure\async_log_repository.py:181 — revisar facet 'performance (sem loops O(n^2))' em AsyncLogRepository.count
00667. [x] app\infrastructure\async_log_repository.py:181 — revisar facet 'coberto por testes' em AsyncLogRepository.count
00668. [x] app\infrastructure\async_log_repository.py:182 — controle with em AsyncLogRepository.count
00669. [x] app\infrastructure\async_log_repository.py:183 — atribuição: AsyncLogRepository.count ← row
00670. [x] app\infrastructure\async_log_repository.py:184 — return em AsyncLogRepository.count
00671. [x] app\infrastructure\async_log_repository.py:186 — definir/revisar FunctionDef: AsyncLogRepository.close
00672. [x] app\infrastructure\async_log_repository.py:186 — revisar facet 'assinatura/args consistentes' em AsyncLogRepository.close
00673. [x] app\infrastructure\async_log_repository.py:186 — revisar facet 'docstring em português' em AsyncLogRepository.close
00674. [x] app\infrastructure\async_log_repository.py:186 — revisar facet 'nomenclatura clara (PEP8)' em AsyncLogRepository.close
00675. [x] app\infrastructure\async_log_repository.py:186 — revisar facet 'type hints presentes' em AsyncLogRepository.close
00676. [x] app\infrastructure\async_log_repository.py:186 — revisar facet 'tratamento de erros adequado' em AsyncLogRepository.close
00677. [x] app\infrastructure\async_log_repository.py:186 — revisar facet 'sem comentários inline desnecessários' em AsyncLogRepository.close
00678. [x] app\infrastructure\async_log_repository.py:186 — revisar facet 'não imprime side-effects na UI/IO' em AsyncLogRepository.close
00679. [x] app\infrastructure\async_log_repository.py:186 — revisar facet 'thread-safety revisada' em AsyncLogRepository.close
00680. [x] app\infrastructure\async_log_repository.py:186 — revisar facet 'performance (sem loops O(n^2))' em AsyncLogRepository.close
00681. [x] app\infrastructure\async_log_repository.py:186 — revisar facet 'coberto por testes' em AsyncLogRepository.close
00682. [x] app\infrastructure\async_log_repository.py:190 — controle with em AsyncLogRepository.close
00683. [x] Existência e estrutura do módulo: app\infrastructure\distribution_registry.py
00684. [x] app\infrastructure\distribution_registry.py:1 — import: __future__
00685. [x] app\infrastructure\distribution_registry.py:3 — import: typing
00686. [x] app\infrastructure\distribution_registry.py:5 — import: app.domain.entities
00687. [x] app\infrastructure\distribution_registry.py:6 — import: app.infrastructure.providers.base
00688. [x] app\infrastructure\distribution_registry.py:7 — import: app.infrastructure.providers.fixed_provider
00689. [x] app\infrastructure\distribution_registry.py:8 — import: app.infrastructure.providers.scipy_provider
00690. [x] app\infrastructure\distribution_registry.py:11 — definir/revisar ClassDef: DistributionRegistry
00691. [x] app\infrastructure\distribution_registry.py:14 — definir/revisar FunctionDef: DistributionRegistry.__init__
00692. [x] app\infrastructure\distribution_registry.py:14 — revisar facet 'assinatura/args consistentes' em DistributionRegistry.__init__
00693. [x] app\infrastructure\distribution_registry.py:14 — revisar facet 'docstring em português' em DistributionRegistry.__init__
00694. [x] app\infrastructure\distribution_registry.py:14 — revisar facet 'nomenclatura clara (PEP8)' em DistributionRegistry.__init__
00695. [x] app\infrastructure\distribution_registry.py:14 — revisar facet 'type hints presentes' em DistributionRegistry.__init__
00696. [x] app\infrastructure\distribution_registry.py:14 — revisar facet 'tratamento de erros adequado' em DistributionRegistry.__init__
00697. [x] app\infrastructure\distribution_registry.py:14 — revisar facet 'sem comentários inline desnecessários' em DistributionRegistry.__init__
00698. [x] app\infrastructure\distribution_registry.py:14 — revisar facet 'não imprime side-effects na UI/IO' em DistributionRegistry.__init__
00699. [x] app\infrastructure\distribution_registry.py:14 — revisar facet 'thread-safety revisada' em DistributionRegistry.__init__
00700. [x] app\infrastructure\distribution_registry.py:14 — revisar facet 'performance (sem loops O(n^2))' em DistributionRegistry.__init__
00701. [x] app\infrastructure\distribution_registry.py:14 — revisar facet 'coberto por testes' em DistributionRegistry.__init__
00702. [x] app\infrastructure\distribution_registry.py:17 — definir/revisar FunctionDef: DistributionRegistry.register
00703. [x] app\infrastructure\distribution_registry.py:17 — revisar facet 'assinatura/args consistentes' em DistributionRegistry.register
00704. [x] app\infrastructure\distribution_registry.py:17 — revisar facet 'docstring em português' em DistributionRegistry.register
00705. [x] app\infrastructure\distribution_registry.py:17 — revisar facet 'nomenclatura clara (PEP8)' em DistributionRegistry.register
00706. [x] app\infrastructure\distribution_registry.py:17 — revisar facet 'type hints presentes' em DistributionRegistry.register
00707. [x] app\infrastructure\distribution_registry.py:17 — revisar facet 'tratamento de erros adequado' em DistributionRegistry.register
00708. [x] app\infrastructure\distribution_registry.py:17 — revisar facet 'sem comentários inline desnecessários' em DistributionRegistry.register
00709. [x] app\infrastructure\distribution_registry.py:17 — revisar facet 'não imprime side-effects na UI/IO' em DistributionRegistry.register
00710. [x] app\infrastructure\distribution_registry.py:17 — revisar facet 'thread-safety revisada' em DistributionRegistry.register
00711. [x] app\infrastructure\distribution_registry.py:17 — revisar facet 'performance (sem loops O(n^2))' em DistributionRegistry.register
00712. [x] app\infrastructure\distribution_registry.py:17 — revisar facet 'coberto por testes' em DistributionRegistry.register
00713. [x] app\infrastructure\distribution_registry.py:18 — atribuição: DistributionRegistry.register ← ?
00714. [x] app\infrastructure\distribution_registry.py:20 — definir/revisar FunctionDef: DistributionRegistry.remove
00715. [x] app\infrastructure\distribution_registry.py:20 — revisar facet 'assinatura/args consistentes' em DistributionRegistry.remove
00716. [x] app\infrastructure\distribution_registry.py:20 — revisar facet 'docstring em português' em DistributionRegistry.remove
00717. [x] app\infrastructure\distribution_registry.py:20 — revisar facet 'nomenclatura clara (PEP8)' em DistributionRegistry.remove
00718. [x] app\infrastructure\distribution_registry.py:20 — revisar facet 'type hints presentes' em DistributionRegistry.remove
00719. [x] app\infrastructure\distribution_registry.py:20 — revisar facet 'tratamento de erros adequado' em DistributionRegistry.remove
00720. [x] app\infrastructure\distribution_registry.py:20 — revisar facet 'sem comentários inline desnecessários' em DistributionRegistry.remove
00721. [x] app\infrastructure\distribution_registry.py:20 — revisar facet 'não imprime side-effects na UI/IO' em DistributionRegistry.remove
00722. [x] app\infrastructure\distribution_registry.py:20 — revisar facet 'thread-safety revisada' em DistributionRegistry.remove
00723. [x] app\infrastructure\distribution_registry.py:20 — revisar facet 'performance (sem loops O(n^2))' em DistributionRegistry.remove
00724. [x] app\infrastructure\distribution_registry.py:20 — revisar facet 'coberto por testes' em DistributionRegistry.remove
00725. [x] app\infrastructure\distribution_registry.py:23 — definir/revisar FunctionDef: DistributionRegistry.get_provider
00726. [x] app\infrastructure\distribution_registry.py:23 — revisar facet 'assinatura/args consistentes' em DistributionRegistry.get_provider
00727. [x] app\infrastructure\distribution_registry.py:23 — revisar facet 'docstring em português' em DistributionRegistry.get_provider
00728. [x] app\infrastructure\distribution_registry.py:23 — revisar facet 'nomenclatura clara (PEP8)' em DistributionRegistry.get_provider
00729. [x] app\infrastructure\distribution_registry.py:23 — revisar facet 'type hints presentes' em DistributionRegistry.get_provider
00730. [x] app\infrastructure\distribution_registry.py:23 — revisar facet 'tratamento de erros adequado' em DistributionRegistry.get_provider
00731. [x] app\infrastructure\distribution_registry.py:23 — revisar facet 'sem comentários inline desnecessários' em DistributionRegistry.get_provider
00732. [x] app\infrastructure\distribution_registry.py:23 — revisar facet 'não imprime side-effects na UI/IO' em DistributionRegistry.get_provider
00733. [x] app\infrastructure\distribution_registry.py:23 — revisar facet 'thread-safety revisada' em DistributionRegistry.get_provider
00734. [x] app\infrastructure\distribution_registry.py:23 — revisar facet 'performance (sem loops O(n^2))' em DistributionRegistry.get_provider
00735. [x] app\infrastructure\distribution_registry.py:23 — revisar facet 'coberto por testes' em DistributionRegistry.get_provider
00736. [x] app\infrastructure\distribution_registry.py:24 — controle if em DistributionRegistry.get_provider
00737. [x] app\infrastructure\distribution_registry.py:25 — raise em DistributionRegistry.get_provider
00738. [x] app\infrastructure\distribution_registry.py:26 — return em DistributionRegistry.get_provider
00739. [x] app\infrastructure\distribution_registry.py:28 — definir/revisar FunctionDef: DistributionRegistry.get
00740. [x] app\infrastructure\distribution_registry.py:28 — revisar facet 'assinatura/args consistentes' em DistributionRegistry.get
00741. [x] app\infrastructure\distribution_registry.py:28 — revisar facet 'docstring em português' em DistributionRegistry.get
00742. [x] app\infrastructure\distribution_registry.py:28 — revisar facet 'nomenclatura clara (PEP8)' em DistributionRegistry.get
00743. [x] app\infrastructure\distribution_registry.py:28 — revisar facet 'type hints presentes' em DistributionRegistry.get
00744. [x] app\infrastructure\distribution_registry.py:28 — revisar facet 'tratamento de erros adequado' em DistributionRegistry.get
00745. [x] app\infrastructure\distribution_registry.py:28 — revisar facet 'sem comentários inline desnecessários' em DistributionRegistry.get
00746. [x] app\infrastructure\distribution_registry.py:28 — revisar facet 'não imprime side-effects na UI/IO' em DistributionRegistry.get
00747. [x] app\infrastructure\distribution_registry.py:28 — revisar facet 'thread-safety revisada' em DistributionRegistry.get
00748. [x] app\infrastructure\distribution_registry.py:28 — revisar facet 'performance (sem loops O(n^2))' em DistributionRegistry.get
00749. [x] app\infrastructure\distribution_registry.py:28 — revisar facet 'coberto por testes' em DistributionRegistry.get
00750. [x] app\infrastructure\distribution_registry.py:30 — return em DistributionRegistry.get
00751. [x] app\infrastructure\distribution_registry.py:32 — definir/revisar FunctionDef: DistributionRegistry.provider_names
00752. [x] app\infrastructure\distribution_registry.py:32 — revisar facet 'assinatura/args consistentes' em DistributionRegistry.provider_names
00753. [x] app\infrastructure\distribution_registry.py:32 — revisar facet 'docstring em português' em DistributionRegistry.provider_names
00754. [x] app\infrastructure\distribution_registry.py:32 — revisar facet 'nomenclatura clara (PEP8)' em DistributionRegistry.provider_names
00755. [x] app\infrastructure\distribution_registry.py:32 — revisar facet 'type hints presentes' em DistributionRegistry.provider_names
00756. [x] app\infrastructure\distribution_registry.py:32 — revisar facet 'tratamento de erros adequado' em DistributionRegistry.provider_names
00757. [x] app\infrastructure\distribution_registry.py:32 — revisar facet 'sem comentários inline desnecessários' em DistributionRegistry.provider_names
00758. [x] app\infrastructure\distribution_registry.py:32 — revisar facet 'não imprime side-effects na UI/IO' em DistributionRegistry.provider_names
00759. [x] app\infrastructure\distribution_registry.py:32 — revisar facet 'thread-safety revisada' em DistributionRegistry.provider_names
00760. [x] app\infrastructure\distribution_registry.py:32 — revisar facet 'performance (sem loops O(n^2))' em DistributionRegistry.provider_names
00761. [x] app\infrastructure\distribution_registry.py:32 — revisar facet 'coberto por testes' em DistributionRegistry.provider_names
00762. [x] app\infrastructure\distribution_registry.py:33 — return em DistributionRegistry.provider_names
00763. [x] app\infrastructure\distribution_registry.py:35 — definir/revisar FunctionDef: DistributionRegistry.list_all
00764. [x] app\infrastructure\distribution_registry.py:35 — revisar facet 'assinatura/args consistentes' em DistributionRegistry.list_all
00765. [x] app\infrastructure\distribution_registry.py:35 — revisar facet 'docstring em português' em DistributionRegistry.list_all
00766. [x] app\infrastructure\distribution_registry.py:35 — revisar facet 'nomenclatura clara (PEP8)' em DistributionRegistry.list_all
00767. [x] app\infrastructure\distribution_registry.py:35 — revisar facet 'type hints presentes' em DistributionRegistry.list_all
00768. [x] app\infrastructure\distribution_registry.py:35 — revisar facet 'tratamento de erros adequado' em DistributionRegistry.list_all
00769. [x] app\infrastructure\distribution_registry.py:35 — revisar facet 'sem comentários inline desnecessários' em DistributionRegistry.list_all
00770. [x] app\infrastructure\distribution_registry.py:35 — revisar facet 'não imprime side-effects na UI/IO' em DistributionRegistry.list_all
00771. [x] app\infrastructure\distribution_registry.py:35 — revisar facet 'thread-safety revisada' em DistributionRegistry.list_all
00772. [x] app\infrastructure\distribution_registry.py:35 — revisar facet 'performance (sem loops O(n^2))' em DistributionRegistry.list_all
00773. [x] app\infrastructure\distribution_registry.py:35 — revisar facet 'coberto por testes' em DistributionRegistry.list_all
00774. [x] app\infrastructure\distribution_registry.py:37 — controle for em DistributionRegistry.list_all
00775. [x] app\infrastructure\distribution_registry.py:38 — controle for em DistributionRegistry.list_all
00776. [x] app\infrastructure\distribution_registry.py:40 — return em DistributionRegistry.list_all
00777. [x] app\infrastructure\distribution_registry.py:43 — definir/revisar FunctionDef: DistributionRegistry.get_spec_code
00778. [x] app\infrastructure\distribution_registry.py:43 — revisar facet 'assinatura/args consistentes' em DistributionRegistry.get_spec_code
00779. [x] app\infrastructure\distribution_registry.py:43 — revisar facet 'docstring em português' em DistributionRegistry.get_spec_code
00780. [x] app\infrastructure\distribution_registry.py:43 — revisar facet 'nomenclatura clara (PEP8)' em DistributionRegistry.get_spec_code
00781. [x] app\infrastructure\distribution_registry.py:43 — revisar facet 'type hints presentes' em DistributionRegistry.get_spec_code
00782. [x] app\infrastructure\distribution_registry.py:43 — revisar facet 'tratamento de erros adequado' em DistributionRegistry.get_spec_code
00783. [x] app\infrastructure\distribution_registry.py:43 — revisar facet 'sem comentários inline desnecessários' em DistributionRegistry.get_spec_code
00784. [x] app\infrastructure\distribution_registry.py:43 — revisar facet 'não imprime side-effects na UI/IO' em DistributionRegistry.get_spec_code
00785. [x] app\infrastructure\distribution_registry.py:43 — revisar facet 'thread-safety revisada' em DistributionRegistry.get_spec_code
00786. [x] app\infrastructure\distribution_registry.py:43 — revisar facet 'performance (sem loops O(n^2))' em DistributionRegistry.get_spec_code
00787. [x] app\infrastructure\distribution_registry.py:43 — revisar facet 'coberto por testes' em DistributionRegistry.get_spec_code
00788. [x] app\infrastructure\distribution_registry.py:44 — return em DistributionRegistry.get_spec_code
00789. [x] app\infrastructure\distribution_registry.py:47 — definir/revisar FunctionDef: DistributionRegistry.parse_code
00790. [x] app\infrastructure\distribution_registry.py:47 — revisar facet 'assinatura/args consistentes' em DistributionRegistry.parse_code
00791. [x] app\infrastructure\distribution_registry.py:47 — revisar facet 'docstring em português' em DistributionRegistry.parse_code
00792. [x] app\infrastructure\distribution_registry.py:47 — revisar facet 'nomenclatura clara (PEP8)' em DistributionRegistry.parse_code
00793. [x] app\infrastructure\distribution_registry.py:47 — revisar facet 'type hints presentes' em DistributionRegistry.parse_code
00794. [x] app\infrastructure\distribution_registry.py:47 — revisar facet 'tratamento de erros adequado' em DistributionRegistry.parse_code
00795. [x] app\infrastructure\distribution_registry.py:47 — revisar facet 'sem comentários inline desnecessários' em DistributionRegistry.parse_code
00796. [x] app\infrastructure\distribution_registry.py:47 — revisar facet 'não imprime side-effects na UI/IO' em DistributionRegistry.parse_code
00797. [x] app\infrastructure\distribution_registry.py:47 — revisar facet 'thread-safety revisada' em DistributionRegistry.parse_code
00798. [x] app\infrastructure\distribution_registry.py:47 — revisar facet 'performance (sem loops O(n^2))' em DistributionRegistry.parse_code
00799. [x] app\infrastructure\distribution_registry.py:47 — revisar facet 'coberto por testes' em DistributionRegistry.parse_code
00800. [x] app\infrastructure\distribution_registry.py:48 — atribuição: DistributionRegistry.parse_code ← ?
00801. [x] app\infrastructure\distribution_registry.py:49 — return em DistributionRegistry.parse_code
00802. [x] app\infrastructure\distribution_registry.py:51 — definir/revisar FunctionDef: DistributionRegistry.sample
00803. [x] app\infrastructure\distribution_registry.py:51 — revisar facet 'assinatura/args consistentes' em DistributionRegistry.sample
00804. [x] app\infrastructure\distribution_registry.py:51 — revisar facet 'docstring em português' em DistributionRegistry.sample
00805. [x] app\infrastructure\distribution_registry.py:51 — revisar facet 'nomenclatura clara (PEP8)' em DistributionRegistry.sample
00806. [x] app\infrastructure\distribution_registry.py:51 — revisar facet 'type hints presentes' em DistributionRegistry.sample
00807. [x] app\infrastructure\distribution_registry.py:51 — revisar facet 'tratamento de erros adequado' em DistributionRegistry.sample
00808. [x] app\infrastructure\distribution_registry.py:51 — revisar facet 'sem comentários inline desnecessários' em DistributionRegistry.sample
00809. [x] app\infrastructure\distribution_registry.py:51 — revisar facet 'não imprime side-effects na UI/IO' em DistributionRegistry.sample
00810. [x] app\infrastructure\distribution_registry.py:51 — revisar facet 'thread-safety revisada' em DistributionRegistry.sample
00811. [x] app\infrastructure\distribution_registry.py:51 — revisar facet 'performance (sem loops O(n^2))' em DistributionRegistry.sample
00812. [x] app\infrastructure\distribution_registry.py:51 — revisar facet 'coberto por testes' em DistributionRegistry.sample
00813. [x] app\infrastructure\distribution_registry.py:52 — return em DistributionRegistry.sample
00814. [x] app\infrastructure\distribution_registry.py:54 — definir/revisar FunctionDef: DistributionRegistry.ppf
00815. [x] app\infrastructure\distribution_registry.py:54 — revisar facet 'assinatura/args consistentes' em DistributionRegistry.ppf
00816. [x] app\infrastructure\distribution_registry.py:54 — revisar facet 'docstring em português' em DistributionRegistry.ppf
00817. [x] app\infrastructure\distribution_registry.py:54 — revisar facet 'nomenclatura clara (PEP8)' em DistributionRegistry.ppf
00818. [x] app\infrastructure\distribution_registry.py:54 — revisar facet 'type hints presentes' em DistributionRegistry.ppf
00819. [x] app\infrastructure\distribution_registry.py:54 — revisar facet 'tratamento de erros adequado' em DistributionRegistry.ppf
00820. [x] app\infrastructure\distribution_registry.py:54 — revisar facet 'sem comentários inline desnecessários' em DistributionRegistry.ppf
00821. [x] app\infrastructure\distribution_registry.py:54 — revisar facet 'não imprime side-effects na UI/IO' em DistributionRegistry.ppf
00822. [x] app\infrastructure\distribution_registry.py:54 — revisar facet 'thread-safety revisada' em DistributionRegistry.ppf
00823. [x] app\infrastructure\distribution_registry.py:54 — revisar facet 'performance (sem loops O(n^2))' em DistributionRegistry.ppf
00824. [x] app\infrastructure\distribution_registry.py:54 — revisar facet 'coberto por testes' em DistributionRegistry.ppf
00825. [x] app\infrastructure\distribution_registry.py:55 — return em DistributionRegistry.ppf
00826. [x] app\infrastructure\distribution_registry.py:57 — definir/revisar FunctionDef: DistributionRegistry.validate
00827. [x] app\infrastructure\distribution_registry.py:57 — revisar facet 'assinatura/args consistentes' em DistributionRegistry.validate
00828. [x] app\infrastructure\distribution_registry.py:57 — revisar facet 'docstring em português' em DistributionRegistry.validate
00829. [x] app\infrastructure\distribution_registry.py:57 — revisar facet 'nomenclatura clara (PEP8)' em DistributionRegistry.validate
00830. [x] app\infrastructure\distribution_registry.py:57 — revisar facet 'type hints presentes' em DistributionRegistry.validate
00831. [x] app\infrastructure\distribution_registry.py:57 — revisar facet 'tratamento de erros adequado' em DistributionRegistry.validate
00832. [x] app\infrastructure\distribution_registry.py:57 — revisar facet 'sem comentários inline desnecessários' em DistributionRegistry.validate
00833. [x] app\infrastructure\distribution_registry.py:57 — revisar facet 'não imprime side-effects na UI/IO' em DistributionRegistry.validate
00834. [x] app\infrastructure\distribution_registry.py:57 — revisar facet 'thread-safety revisada' em DistributionRegistry.validate
00835. [x] app\infrastructure\distribution_registry.py:57 — revisar facet 'performance (sem loops O(n^2))' em DistributionRegistry.validate
00836. [x] app\infrastructure\distribution_registry.py:57 — revisar facet 'coberto por testes' em DistributionRegistry.validate
00837. [x] app\infrastructure\distribution_registry.py:58 — return em DistributionRegistry.validate
00838. [x] app\infrastructure\distribution_registry.py:61 — definir/revisar FunctionDef: build_default_registry
00839. [x] app\infrastructure\distribution_registry.py:61 — revisar facet 'assinatura/args consistentes' em build_default_registry
00840. [x] app\infrastructure\distribution_registry.py:61 — revisar facet 'docstring em português' em build_default_registry
00841. [x] app\infrastructure\distribution_registry.py:61 — revisar facet 'nomenclatura clara (PEP8)' em build_default_registry
00842. [x] app\infrastructure\distribution_registry.py:61 — revisar facet 'type hints presentes' em build_default_registry
00843. [x] app\infrastructure\distribution_registry.py:61 — revisar facet 'tratamento de erros adequado' em build_default_registry
00844. [x] app\infrastructure\distribution_registry.py:61 — revisar facet 'sem comentários inline desnecessários' em build_default_registry
00845. [x] app\infrastructure\distribution_registry.py:61 — revisar facet 'não imprime side-effects na UI/IO' em build_default_registry
00846. [x] app\infrastructure\distribution_registry.py:61 — revisar facet 'thread-safety revisada' em build_default_registry
00847. [x] app\infrastructure\distribution_registry.py:61 — revisar facet 'performance (sem loops O(n^2))' em build_default_registry
00848. [x] app\infrastructure\distribution_registry.py:61 — revisar facet 'coberto por testes' em build_default_registry
00849. [x] app\infrastructure\distribution_registry.py:62 — atribuição: build_default_registry ← reg
00850. [x] app\infrastructure\distribution_registry.py:65 — return em build_default_registry
00851. [x] Existência e estrutura do módulo: app\infrastructure\event_bus.py
00852. [x] app\infrastructure\event_bus.py:3 — import: __future__
00853. [x] app\infrastructure\event_bus.py:5 — import: threading
00854. [x] app\infrastructure\event_bus.py:6 — import: traceback
00855. [x] app\infrastructure\event_bus.py:7 — import: collections
00856. [x] app\infrastructure\event_bus.py:8 — import: typing
00857. [x] app\infrastructure\event_bus.py:10 — import: app.domain.events
00858. [x] app\infrastructure\event_bus.py:12 — atribuição:  ← E
00859. [x] app\infrastructure\event_bus.py:15 — definir/revisar ClassDef: EventBus
00860. [x] app\infrastructure\event_bus.py:16 — definir/revisar FunctionDef: EventBus.__init__
00861. [x] app\infrastructure\event_bus.py:16 — revisar facet 'assinatura/args consistentes' em EventBus.__init__
00862. [x] app\infrastructure\event_bus.py:16 — revisar facet 'docstring em português' em EventBus.__init__
00863. [x] app\infrastructure\event_bus.py:16 — revisar facet 'nomenclatura clara (PEP8)' em EventBus.__init__
00864. [x] app\infrastructure\event_bus.py:16 — revisar facet 'type hints presentes' em EventBus.__init__
00865. [x] app\infrastructure\event_bus.py:16 — revisar facet 'tratamento de erros adequado' em EventBus.__init__
00866. [x] app\infrastructure\event_bus.py:16 — revisar facet 'sem comentários inline desnecessários' em EventBus.__init__
00867. [x] app\infrastructure\event_bus.py:16 — revisar facet 'não imprime side-effects na UI/IO' em EventBus.__init__
00868. [x] app\infrastructure\event_bus.py:16 — revisar facet 'thread-safety revisada' em EventBus.__init__
00869. [x] app\infrastructure\event_bus.py:16 — revisar facet 'performance (sem loops O(n^2))' em EventBus.__init__
00870. [x] app\infrastructure\event_bus.py:16 — revisar facet 'coberto por testes' em EventBus.__init__
00871. [x] app\infrastructure\event_bus.py:18 — atribuição: EventBus.__init__ ← ?
00872. [x] app\infrastructure\event_bus.py:20 — definir/revisar FunctionDef: EventBus.subscribe
00873. [x] app\infrastructure\event_bus.py:20 — revisar facet 'assinatura/args consistentes' em EventBus.subscribe
00874. [x] app\infrastructure\event_bus.py:20 — revisar facet 'docstring em português' em EventBus.subscribe
00875. [x] app\infrastructure\event_bus.py:20 — revisar facet 'nomenclatura clara (PEP8)' em EventBus.subscribe
00876. [x] app\infrastructure\event_bus.py:20 — revisar facet 'type hints presentes' em EventBus.subscribe
00877. [x] app\infrastructure\event_bus.py:20 — revisar facet 'tratamento de erros adequado' em EventBus.subscribe
00878. [x] app\infrastructure\event_bus.py:20 — revisar facet 'sem comentários inline desnecessários' em EventBus.subscribe
00879. [x] app\infrastructure\event_bus.py:20 — revisar facet 'não imprime side-effects na UI/IO' em EventBus.subscribe
00880. [x] app\infrastructure\event_bus.py:20 — revisar facet 'thread-safety revisada' em EventBus.subscribe
00881. [x] app\infrastructure\event_bus.py:20 — revisar facet 'performance (sem loops O(n^2))' em EventBus.subscribe
00882. [x] app\infrastructure\event_bus.py:20 — revisar facet 'coberto por testes' em EventBus.subscribe
00883. [x] app\infrastructure\event_bus.py:21 — controle with em EventBus.subscribe
00884. [x] app\infrastructure\event_bus.py:24 — definir/revisar FunctionDef: EventBus.unsubscribe
00885. [x] app\infrastructure\event_bus.py:24 — revisar facet 'assinatura/args consistentes' em EventBus.unsubscribe
00886. [x] app\infrastructure\event_bus.py:24 — revisar facet 'docstring em português' em EventBus.unsubscribe
00887. [x] app\infrastructure\event_bus.py:24 — revisar facet 'nomenclatura clara (PEP8)' em EventBus.unsubscribe
00888. [x] app\infrastructure\event_bus.py:24 — revisar facet 'type hints presentes' em EventBus.unsubscribe
00889. [x] app\infrastructure\event_bus.py:24 — revisar facet 'tratamento de erros adequado' em EventBus.unsubscribe
00890. [x] app\infrastructure\event_bus.py:24 — revisar facet 'sem comentários inline desnecessários' em EventBus.unsubscribe
00891. [x] app\infrastructure\event_bus.py:24 — revisar facet 'não imprime side-effects na UI/IO' em EventBus.unsubscribe
00892. [x] app\infrastructure\event_bus.py:24 — revisar facet 'thread-safety revisada' em EventBus.unsubscribe
00893. [x] app\infrastructure\event_bus.py:24 — revisar facet 'performance (sem loops O(n^2))' em EventBus.unsubscribe
00894. [x] app\infrastructure\event_bus.py:24 — revisar facet 'coberto por testes' em EventBus.unsubscribe
00895. [x] app\infrastructure\event_bus.py:25 — controle with em EventBus.unsubscribe
00896. [x] app\infrastructure\event_bus.py:26 — controle if em EventBus.unsubscribe
00897. [x] app\infrastructure\event_bus.py:29 — definir/revisar FunctionDef: EventBus.publish
00898. [x] app\infrastructure\event_bus.py:29 — revisar facet 'assinatura/args consistentes' em EventBus.publish
00899. [x] app\infrastructure\event_bus.py:29 — revisar facet 'docstring em português' em EventBus.publish
00900. [x] app\infrastructure\event_bus.py:29 — revisar facet 'nomenclatura clara (PEP8)' em EventBus.publish
00901. [x] app\infrastructure\event_bus.py:29 — revisar facet 'type hints presentes' em EventBus.publish
00902. [x] app\infrastructure\event_bus.py:29 — revisar facet 'tratamento de erros adequado' em EventBus.publish
00903. [x] app\infrastructure\event_bus.py:29 — revisar facet 'sem comentários inline desnecessários' em EventBus.publish
00904. [x] app\infrastructure\event_bus.py:29 — revisar facet 'não imprime side-effects na UI/IO' em EventBus.publish
00905. [x] app\infrastructure\event_bus.py:29 — revisar facet 'thread-safety revisada' em EventBus.publish
00906. [x] app\infrastructure\event_bus.py:29 — revisar facet 'performance (sem loops O(n^2))' em EventBus.publish
00907. [x] app\infrastructure\event_bus.py:29 — revisar facet 'coberto por testes' em EventBus.publish
00908. [x] app\infrastructure\event_bus.py:30 — atribuição: EventBus.publish ← handlers
00909. [x] app\infrastructure\event_bus.py:31 — controle for em EventBus.publish
00910. [x] app\infrastructure\event_bus.py:32 — try em EventBus.publish
00911. [x] Existência e estrutura do módulo: app\infrastructure\experiment_repository.py
00912. [x] app\infrastructure\experiment_repository.py:3 — import: __future__
00913. [x] app\infrastructure\experiment_repository.py:5 — import: json
00914. [x] app\infrastructure\experiment_repository.py:6 — import: sqlite3
00915. [x] app\infrastructure\experiment_repository.py:7 — import: datetime
00916. [x] app\infrastructure\experiment_repository.py:8 — import: pathlib
00917. [x] app\infrastructure\experiment_repository.py:9 — import: typing
00918. [x] app\infrastructure\experiment_repository.py:12 — definir/revisar ClassDef: ExperimentRepository
00919. [x] app\infrastructure\experiment_repository.py:13 — definir/revisar FunctionDef: ExperimentRepository.__init__
00920. [x] app\infrastructure\experiment_repository.py:13 — revisar facet 'assinatura/args consistentes' em ExperimentRepository.__init__
00921. [x] app\infrastructure\experiment_repository.py:13 — revisar facet 'docstring em português' em ExperimentRepository.__init__
00922. [x] app\infrastructure\experiment_repository.py:13 — revisar facet 'nomenclatura clara (PEP8)' em ExperimentRepository.__init__
00923. [x] app\infrastructure\experiment_repository.py:13 — revisar facet 'type hints presentes' em ExperimentRepository.__init__
00924. [x] app\infrastructure\experiment_repository.py:13 — revisar facet 'tratamento de erros adequado' em ExperimentRepository.__init__
00925. [x] app\infrastructure\experiment_repository.py:13 — revisar facet 'sem comentários inline desnecessários' em ExperimentRepository.__init__
00926. [x] app\infrastructure\experiment_repository.py:13 — revisar facet 'não imprime side-effects na UI/IO' em ExperimentRepository.__init__
00927. [x] app\infrastructure\experiment_repository.py:13 — revisar facet 'thread-safety revisada' em ExperimentRepository.__init__
00928. [x] app\infrastructure\experiment_repository.py:13 — revisar facet 'performance (sem loops O(n^2))' em ExperimentRepository.__init__
00929. [x] app\infrastructure\experiment_repository.py:13 — revisar facet 'coberto por testes' em ExperimentRepository.__init__
00930. [x] app\infrastructure\experiment_repository.py:14 — controle if em ExperimentRepository.__init__
00931. [x] app\infrastructure\experiment_repository.py:16 — atribuição: ExperimentRepository.__init__ ← ?
00932. [x] app\infrastructure\experiment_repository.py:17 — atribuição: ExperimentRepository.__init__ ← ?
00933. [x] app\infrastructure\experiment_repository.py:20 — definir/revisar FunctionDef: ExperimentRepository._create_schema
00934. [x] app\infrastructure\experiment_repository.py:20 — revisar facet 'assinatura/args consistentes' em ExperimentRepository._create_schema
00935. [x] app\infrastructure\experiment_repository.py:20 — revisar facet 'docstring em português' em ExperimentRepository._create_schema
00936. [x] app\infrastructure\experiment_repository.py:20 — revisar facet 'nomenclatura clara (PEP8)' em ExperimentRepository._create_schema
00937. [x] app\infrastructure\experiment_repository.py:20 — revisar facet 'type hints presentes' em ExperimentRepository._create_schema
00938. [x] app\infrastructure\experiment_repository.py:20 — revisar facet 'tratamento de erros adequado' em ExperimentRepository._create_schema
00939. [x] app\infrastructure\experiment_repository.py:20 — revisar facet 'sem comentários inline desnecessários' em ExperimentRepository._create_schema
00940. [x] app\infrastructure\experiment_repository.py:20 — revisar facet 'não imprime side-effects na UI/IO' em ExperimentRepository._create_schema
00941. [x] app\infrastructure\experiment_repository.py:20 — revisar facet 'thread-safety revisada' em ExperimentRepository._create_schema
00942. [x] app\infrastructure\experiment_repository.py:20 — revisar facet 'performance (sem loops O(n^2))' em ExperimentRepository._create_schema
00943. [x] app\infrastructure\experiment_repository.py:20 — revisar facet 'coberto por testes' em ExperimentRepository._create_schema
00944. [x] app\infrastructure\experiment_repository.py:21 — controle with em ExperimentRepository._create_schema
00945. [x] app\infrastructure\experiment_repository.py:59 — definir/revisar FunctionDef: ExperimentRepository.create_batch
00946. [x] app\infrastructure\experiment_repository.py:59 — revisar facet 'assinatura/args consistentes' em ExperimentRepository.create_batch
00947. [x] app\infrastructure\experiment_repository.py:59 — revisar facet 'docstring em português' em ExperimentRepository.create_batch
00948. [x] app\infrastructure\experiment_repository.py:59 — revisar facet 'nomenclatura clara (PEP8)' em ExperimentRepository.create_batch
00949. [x] app\infrastructure\experiment_repository.py:59 — revisar facet 'type hints presentes' em ExperimentRepository.create_batch
00950. [x] app\infrastructure\experiment_repository.py:59 — revisar facet 'tratamento de erros adequado' em ExperimentRepository.create_batch
00951. [x] app\infrastructure\experiment_repository.py:59 — revisar facet 'sem comentários inline desnecessários' em ExperimentRepository.create_batch
00952. [x] app\infrastructure\experiment_repository.py:59 — revisar facet 'não imprime side-effects na UI/IO' em ExperimentRepository.create_batch
00953. [x] app\infrastructure\experiment_repository.py:59 — revisar facet 'thread-safety revisada' em ExperimentRepository.create_batch
00954. [x] app\infrastructure\experiment_repository.py:59 — revisar facet 'performance (sem loops O(n^2))' em ExperimentRepository.create_batch
00955. [x] app\infrastructure\experiment_repository.py:59 — revisar facet 'coberto por testes' em ExperimentRepository.create_batch
00956. [x] app\infrastructure\experiment_repository.py:68 — controle with em ExperimentRepository.create_batch
00957. [x] app\infrastructure\experiment_repository.py:86 — definir/revisar FunctionDef: ExperimentRepository.list_batches
00958. [x] app\infrastructure\experiment_repository.py:86 — revisar facet 'assinatura/args consistentes' em ExperimentRepository.list_batches
00959. [x] app\infrastructure\experiment_repository.py:86 — revisar facet 'docstring em português' em ExperimentRepository.list_batches
00960. [x] app\infrastructure\experiment_repository.py:86 — revisar facet 'nomenclatura clara (PEP8)' em ExperimentRepository.list_batches
00961. [x] app\infrastructure\experiment_repository.py:86 — revisar facet 'type hints presentes' em ExperimentRepository.list_batches
00962. [x] app\infrastructure\experiment_repository.py:86 — revisar facet 'tratamento de erros adequado' em ExperimentRepository.list_batches
00963. [x] app\infrastructure\experiment_repository.py:86 — revisar facet 'sem comentários inline desnecessários' em ExperimentRepository.list_batches
00964. [x] app\infrastructure\experiment_repository.py:86 — revisar facet 'não imprime side-effects na UI/IO' em ExperimentRepository.list_batches
00965. [x] app\infrastructure\experiment_repository.py:86 — revisar facet 'thread-safety revisada' em ExperimentRepository.list_batches
00966. [x] app\infrastructure\experiment_repository.py:86 — revisar facet 'performance (sem loops O(n^2))' em ExperimentRepository.list_batches
00967. [x] app\infrastructure\experiment_repository.py:86 — revisar facet 'coberto por testes' em ExperimentRepository.list_batches
00968. [x] app\infrastructure\experiment_repository.py:87 — atribuição: ExperimentRepository.list_batches ← rows
00969. [x] app\infrastructure\experiment_repository.py:94 — return em ExperimentRepository.list_batches
00970. [x] app\infrastructure\experiment_repository.py:96 — definir/revisar FunctionDef: ExperimentRepository.insert_result
00971. [x] app\infrastructure\experiment_repository.py:96 — revisar facet 'assinatura/args consistentes' em ExperimentRepository.insert_result
00972. [x] app\infrastructure\experiment_repository.py:96 — revisar facet 'docstring em português' em ExperimentRepository.insert_result
00973. [x] app\infrastructure\experiment_repository.py:96 — revisar facet 'nomenclatura clara (PEP8)' em ExperimentRepository.insert_result
00974. [x] app\infrastructure\experiment_repository.py:96 — revisar facet 'type hints presentes' em ExperimentRepository.insert_result
00975. [x] app\infrastructure\experiment_repository.py:96 — revisar facet 'tratamento de erros adequado' em ExperimentRepository.insert_result
00976. [x] app\infrastructure\experiment_repository.py:96 — revisar facet 'sem comentários inline desnecessários' em ExperimentRepository.insert_result
00977. [x] app\infrastructure\experiment_repository.py:96 — revisar facet 'não imprime side-effects na UI/IO' em ExperimentRepository.insert_result
00978. [x] app\infrastructure\experiment_repository.py:96 — revisar facet 'thread-safety revisada' em ExperimentRepository.insert_result
00979. [x] app\infrastructure\experiment_repository.py:96 — revisar facet 'performance (sem loops O(n^2))' em ExperimentRepository.insert_result
00980. [x] app\infrastructure\experiment_repository.py:96 — revisar facet 'coberto por testes' em ExperimentRepository.insert_result
00981. [x] app\infrastructure\experiment_repository.py:103 — controle with em ExperimentRepository.insert_result
00982. [x] app\infrastructure\experiment_repository.py:104 — atribuição: ExperimentRepository.insert_result ← cur
00983. [x] app\infrastructure\experiment_repository.py:105 — controle for em ExperimentRepository.insert_result
00984. [x] app\infrastructure\experiment_repository.py:110 — atribuição: ExperimentRepository.insert_result ← exp_id
00985. [x] app\infrastructure\experiment_repository.py:119 — definir/revisar FunctionDef: ExperimentRepository.count
00986. [x] app\infrastructure\experiment_repository.py:119 — revisar facet 'assinatura/args consistentes' em ExperimentRepository.count
00987. [x] app\infrastructure\experiment_repository.py:119 — revisar facet 'docstring em português' em ExperimentRepository.count
00988. [x] app\infrastructure\experiment_repository.py:119 — revisar facet 'nomenclatura clara (PEP8)' em ExperimentRepository.count
00989. [x] app\infrastructure\experiment_repository.py:119 — revisar facet 'type hints presentes' em ExperimentRepository.count
00990. [x] app\infrastructure\experiment_repository.py:119 — revisar facet 'tratamento de erros adequado' em ExperimentRepository.count
00991. [x] app\infrastructure\experiment_repository.py:119 — revisar facet 'sem comentários inline desnecessários' em ExperimentRepository.count
00992. [x] app\infrastructure\experiment_repository.py:119 — revisar facet 'não imprime side-effects na UI/IO' em ExperimentRepository.count
00993. [x] app\infrastructure\experiment_repository.py:119 — revisar facet 'thread-safety revisada' em ExperimentRepository.count
00994. [x] app\infrastructure\experiment_repository.py:119 — revisar facet 'performance (sem loops O(n^2))' em ExperimentRepository.count
00995. [x] app\infrastructure\experiment_repository.py:119 — revisar facet 'coberto por testes' em ExperimentRepository.count
00996. [x] app\infrastructure\experiment_repository.py:120 — atribuição: ExperimentRepository.count ← row
00997. [x] app\infrastructure\experiment_repository.py:121 — return em ExperimentRepository.count
00998. [x] app\infrastructure\experiment_repository.py:123 — definir/revisar FunctionDef: ExperimentRepository.var_ids
00999. [x] app\infrastructure\experiment_repository.py:123 — revisar facet 'assinatura/args consistentes' em ExperimentRepository.var_ids
01000. [x] app\infrastructure\experiment_repository.py:123 — revisar facet 'docstring em português' em ExperimentRepository.var_ids
01001. [x] app\infrastructure\experiment_repository.py:123 — revisar facet 'nomenclatura clara (PEP8)' em ExperimentRepository.var_ids
01002. [x] app\infrastructure\experiment_repository.py:123 — revisar facet 'type hints presentes' em ExperimentRepository.var_ids
01003. [x] app\infrastructure\experiment_repository.py:123 — revisar facet 'tratamento de erros adequado' em ExperimentRepository.var_ids
01004. [x] app\infrastructure\experiment_repository.py:123 — revisar facet 'sem comentários inline desnecessários' em ExperimentRepository.var_ids
01005. [x] app\infrastructure\experiment_repository.py:123 — revisar facet 'não imprime side-effects na UI/IO' em ExperimentRepository.var_ids
01006. [x] app\infrastructure\experiment_repository.py:123 — revisar facet 'thread-safety revisada' em ExperimentRepository.var_ids
01007. [x] app\infrastructure\experiment_repository.py:123 — revisar facet 'performance (sem loops O(n^2))' em ExperimentRepository.var_ids
01008. [x] app\infrastructure\experiment_repository.py:123 — revisar facet 'coberto por testes' em ExperimentRepository.var_ids
01009. [x] app\infrastructure\experiment_repository.py:124 — atribuição: ExperimentRepository.var_ids ← rows
01010. [x] app\infrastructure\experiment_repository.py:127 — return em ExperimentRepository.var_ids
01011. [x] app\infrastructure\experiment_repository.py:129 — definir/revisar FunctionDef: ExperimentRepository.fetch_page
01012. [x] app\infrastructure\experiment_repository.py:129 — revisar facet 'assinatura/args consistentes' em ExperimentRepository.fetch_page
01013. [x] app\infrastructure\experiment_repository.py:129 — revisar facet 'docstring em português' em ExperimentRepository.fetch_page
01014. [x] app\infrastructure\experiment_repository.py:129 — revisar facet 'nomenclatura clara (PEP8)' em ExperimentRepository.fetch_page
01015. [x] app\infrastructure\experiment_repository.py:129 — revisar facet 'type hints presentes' em ExperimentRepository.fetch_page
01016. [x] app\infrastructure\experiment_repository.py:129 — revisar facet 'tratamento de erros adequado' em ExperimentRepository.fetch_page
01017. [x] app\infrastructure\experiment_repository.py:129 — revisar facet 'sem comentários inline desnecessários' em ExperimentRepository.fetch_page
01018. [x] app\infrastructure\experiment_repository.py:129 — revisar facet 'não imprime side-effects na UI/IO' em ExperimentRepository.fetch_page
01019. [x] app\infrastructure\experiment_repository.py:129 — revisar facet 'thread-safety revisada' em ExperimentRepository.fetch_page
01020. [x] app\infrastructure\experiment_repository.py:129 — revisar facet 'performance (sem loops O(n^2))' em ExperimentRepository.fetch_page
01021. [x] app\infrastructure\experiment_repository.py:129 — revisar facet 'coberto por testes' em ExperimentRepository.fetch_page
01022. [x] app\infrastructure\experiment_repository.py:135 — atribuição: ExperimentRepository.fetch_page ← offset
01023. [x] app\infrastructure\experiment_repository.py:136 — atribuição: ExperimentRepository.fetch_page ← rows
01024. [x] app\infrastructure\experiment_repository.py:146 — controle if em ExperimentRepository.fetch_page
01025. [x] app\infrastructure\experiment_repository.py:147 — return em ExperimentRepository.fetch_page
01026. [x] app\infrastructure\experiment_repository.py:149 — atribuição: ExperimentRepository.fetch_page ← ids
01027. [x] app\infrastructure\experiment_repository.py:150 — atribuição: ExperimentRepository.fetch_page ← ph
01028. [x] app\infrastructure\experiment_repository.py:152 — controle if em ExperimentRepository.fetch_page
01029. [x] app\infrastructure\experiment_repository.py:153 — atribuição: ExperimentRepository.fetch_page ← vph
01030. [x] app\infrastructure\experiment_repository.py:154 — atribuição: ExperimentRepository.fetch_page ← sql
01031. [x] app\infrastructure\experiment_repository.py:161 — atribuição: ExperimentRepository.fetch_page ← sql
01032. [x] app\infrastructure\experiment_repository.py:166 — atribuição: ExperimentRepository.fetch_page ← params
01033. [x] app\infrastructure\experiment_repository.py:168 — atribuição: ExperimentRepository.fetch_page ← vrows
01034. [x] app\infrastructure\experiment_repository.py:171 — controle for em ExperimentRepository.fetch_page
01035. [x] app\infrastructure\experiment_repository.py:172 — atribuição: ExperimentRepository.fetch_page ← ?
01036. [x] app\infrastructure\experiment_repository.py:174 — return em ExperimentRepository.fetch_page
01037. [x] app\infrastructure\experiment_repository.py:183 — definir/revisar FunctionDef: ExperimentRepository.get_variable_values
01038. [x] app\infrastructure\experiment_repository.py:183 — revisar facet 'assinatura/args consistentes' em ExperimentRepository.get_variable_values
01039. [x] app\infrastructure\experiment_repository.py:183 — revisar facet 'docstring em português' em ExperimentRepository.get_variable_values
01040. [x] app\infrastructure\experiment_repository.py:183 — revisar facet 'nomenclatura clara (PEP8)' em ExperimentRepository.get_variable_values
01041. [x] app\infrastructure\experiment_repository.py:183 — revisar facet 'type hints presentes' em ExperimentRepository.get_variable_values
01042. [x] app\infrastructure\experiment_repository.py:183 — revisar facet 'tratamento de erros adequado' em ExperimentRepository.get_variable_values
01043. [x] app\infrastructure\experiment_repository.py:183 — revisar facet 'sem comentários inline desnecessários' em ExperimentRepository.get_variable_values
01044. [x] app\infrastructure\experiment_repository.py:183 — revisar facet 'não imprime side-effects na UI/IO' em ExperimentRepository.get_variable_values
01045. [x] app\infrastructure\experiment_repository.py:183 — revisar facet 'thread-safety revisada' em ExperimentRepository.get_variable_values
01046. [x] app\infrastructure\experiment_repository.py:183 — revisar facet 'performance (sem loops O(n^2))' em ExperimentRepository.get_variable_values
01047. [x] app\infrastructure\experiment_repository.py:183 — revisar facet 'coberto por testes' em ExperimentRepository.get_variable_values
01048. [x] app\infrastructure\experiment_repository.py:184 — atribuição: ExperimentRepository.get_variable_values ← sql
01049. [x] app\infrastructure\experiment_repository.py:190 — controle if em ExperimentRepository.get_variable_values
01050. [x] app\infrastructure\experiment_repository.py:193 — return em ExperimentRepository.get_variable_values
01051. [x] app\infrastructure\experiment_repository.py:195 — definir/revisar FunctionDef: ExperimentRepository.get_experiment_values
01052. [x] app\infrastructure\experiment_repository.py:195 — revisar facet 'assinatura/args consistentes' em ExperimentRepository.get_experiment_values
01053. [x] app\infrastructure\experiment_repository.py:195 — revisar facet 'docstring em português' em ExperimentRepository.get_experiment_values
01054. [x] app\infrastructure\experiment_repository.py:195 — revisar facet 'nomenclatura clara (PEP8)' em ExperimentRepository.get_experiment_values
01055. [x] app\infrastructure\experiment_repository.py:195 — revisar facet 'type hints presentes' em ExperimentRepository.get_experiment_values
01056. [x] app\infrastructure\experiment_repository.py:195 — revisar facet 'tratamento de erros adequado' em ExperimentRepository.get_experiment_values
01057. [x] app\infrastructure\experiment_repository.py:195 — revisar facet 'sem comentários inline desnecessários' em ExperimentRepository.get_experiment_values
01058. [x] app\infrastructure\experiment_repository.py:195 — revisar facet 'não imprime side-effects na UI/IO' em ExperimentRepository.get_experiment_values
01059. [x] app\infrastructure\experiment_repository.py:195 — revisar facet 'thread-safety revisada' em ExperimentRepository.get_experiment_values
01060. [x] app\infrastructure\experiment_repository.py:195 — revisar facet 'performance (sem loops O(n^2))' em ExperimentRepository.get_experiment_values
01061. [x] app\infrastructure\experiment_repository.py:195 — revisar facet 'coberto por testes' em ExperimentRepository.get_experiment_values
01062. [x] app\infrastructure\experiment_repository.py:196 — atribuição: ExperimentRepository.get_experiment_values ← row
01063. [x] app\infrastructure\experiment_repository.py:199 — controle if em ExperimentRepository.get_experiment_values
01064. [x] app\infrastructure\experiment_repository.py:200 — raise em ExperimentRepository.get_experiment_values
01065. [x] app\infrastructure\experiment_repository.py:201 — atribuição: ExperimentRepository.get_experiment_values ← vrows
01066. [x] app\infrastructure\experiment_repository.py:205 — return em ExperimentRepository.get_experiment_values
01067. [x] app\infrastructure\experiment_repository.py:207 — definir/revisar FunctionDef: ExperimentRepository.list_experiment_ids
01068. [x] app\infrastructure\experiment_repository.py:207 — revisar facet 'assinatura/args consistentes' em ExperimentRepository.list_experiment_ids
01069. [x] app\infrastructure\experiment_repository.py:207 — revisar facet 'docstring em português' em ExperimentRepository.list_experiment_ids
01070. [x] app\infrastructure\experiment_repository.py:207 — revisar facet 'nomenclatura clara (PEP8)' em ExperimentRepository.list_experiment_ids
01071. [x] app\infrastructure\experiment_repository.py:207 — revisar facet 'type hints presentes' em ExperimentRepository.list_experiment_ids
01072. [x] app\infrastructure\experiment_repository.py:207 — revisar facet 'tratamento de erros adequado' em ExperimentRepository.list_experiment_ids
01073. [x] app\infrastructure\experiment_repository.py:207 — revisar facet 'sem comentários inline desnecessários' em ExperimentRepository.list_experiment_ids
01074. [x] app\infrastructure\experiment_repository.py:207 — revisar facet 'não imprime side-effects na UI/IO' em ExperimentRepository.list_experiment_ids
01075. [x] app\infrastructure\experiment_repository.py:207 — revisar facet 'thread-safety revisada' em ExperimentRepository.list_experiment_ids
01076. [x] app\infrastructure\experiment_repository.py:207 — revisar facet 'performance (sem loops O(n^2))' em ExperimentRepository.list_experiment_ids
01077. [x] app\infrastructure\experiment_repository.py:207 — revisar facet 'coberto por testes' em ExperimentRepository.list_experiment_ids
01078. [x] app\infrastructure\experiment_repository.py:208 — atribuição: ExperimentRepository.list_experiment_ids ← rows
01079. [x] app\infrastructure\experiment_repository.py:211 — return em ExperimentRepository.list_experiment_ids
01080. [x] app\infrastructure\experiment_repository.py:213 — definir/revisar FunctionDef: ExperimentRepository.close
01081. [x] app\infrastructure\experiment_repository.py:213 — revisar facet 'assinatura/args consistentes' em ExperimentRepository.close
01082. [x] app\infrastructure\experiment_repository.py:213 — revisar facet 'docstring em português' em ExperimentRepository.close
01083. [x] app\infrastructure\experiment_repository.py:213 — revisar facet 'nomenclatura clara (PEP8)' em ExperimentRepository.close
01084. [x] app\infrastructure\experiment_repository.py:213 — revisar facet 'type hints presentes' em ExperimentRepository.close
01085. [x] app\infrastructure\experiment_repository.py:213 — revisar facet 'tratamento de erros adequado' em ExperimentRepository.close
01086. [x] app\infrastructure\experiment_repository.py:213 — revisar facet 'sem comentários inline desnecessários' em ExperimentRepository.close
01087. [x] app\infrastructure\experiment_repository.py:213 — revisar facet 'não imprime side-effects na UI/IO' em ExperimentRepository.close
01088. [x] app\infrastructure\experiment_repository.py:213 — revisar facet 'thread-safety revisada' em ExperimentRepository.close
01089. [x] app\infrastructure\experiment_repository.py:213 — revisar facet 'performance (sem loops O(n^2))' em ExperimentRepository.close
01090. [x] app\infrastructure\experiment_repository.py:213 — revisar facet 'coberto por testes' em ExperimentRepository.close
01091. [x] Existência e estrutura do módulo: app\infrastructure\plugins\__init__.py
01092. [x] app\infrastructure\plugins\__init__.py:3 — import: app.infrastructure.plugins.loader
01093. [x] app\infrastructure\plugins\__init__.py:5 — atribuição:  ← __all__
01094. [x] Existência e estrutura do módulo: app\infrastructure\plugins\loader.py
01095. [x] app\infrastructure\plugins\loader.py:3 — import: __future__
01096. [x] app\infrastructure\plugins\loader.py:5 — import: importlib.util
01097. [x] app\infrastructure\plugins\loader.py:6 — import: sys
01098. [x] app\infrastructure\plugins\loader.py:7 — import: traceback
01099. [x] app\infrastructure\plugins\loader.py:8 — import: dataclasses
01100. [x] app\infrastructure\plugins\loader.py:9 — import: pathlib
01101. [x] app\infrastructure\plugins\loader.py:10 — import: typing
01102. [x] app\infrastructure\plugins\loader.py:12 — import: app.infrastructure.providers.base
01103. [x] app\infrastructure\plugins\loader.py:16 — definir/revisar ClassDef: LoadedPlugin
01104. [x] app\infrastructure\plugins\loader.py:24 — definir/revisar ClassDef: PluginLoadReport
01105. [x] app\infrastructure\plugins\loader.py:28 — definir/revisar FunctionDef: PluginLoadReport.all
01106. [x] app\infrastructure\plugins\loader.py:28 — revisar facet 'assinatura/args consistentes' em PluginLoadReport.all
01107. [x] app\infrastructure\plugins\loader.py:28 — revisar facet 'docstring em português' em PluginLoadReport.all
01108. [x] app\infrastructure\plugins\loader.py:28 — revisar facet 'nomenclatura clara (PEP8)' em PluginLoadReport.all
01109. [x] app\infrastructure\plugins\loader.py:28 — revisar facet 'type hints presentes' em PluginLoadReport.all
01110. [x] app\infrastructure\plugins\loader.py:28 — revisar facet 'tratamento de erros adequado' em PluginLoadReport.all
01111. [x] app\infrastructure\plugins\loader.py:28 — revisar facet 'sem comentários inline desnecessários' em PluginLoadReport.all
01112. [x] app\infrastructure\plugins\loader.py:28 — revisar facet 'não imprime side-effects na UI/IO' em PluginLoadReport.all
01113. [x] app\infrastructure\plugins\loader.py:28 — revisar facet 'thread-safety revisada' em PluginLoadReport.all
01114. [x] app\infrastructure\plugins\loader.py:28 — revisar facet 'performance (sem loops O(n^2))' em PluginLoadReport.all
01115. [x] app\infrastructure\plugins\loader.py:28 — revisar facet 'coberto por testes' em PluginLoadReport.all
01116. [x] app\infrastructure\plugins\loader.py:29 — return em PluginLoadReport.all
01117. [x] app\infrastructure\plugins\loader.py:32 — definir/revisar ClassDef: PluginLoader
01118. [x] app\infrastructure\plugins\loader.py:35 — definir/revisar FunctionDef: PluginLoader.__init__
01119. [x] app\infrastructure\plugins\loader.py:35 — revisar facet 'assinatura/args consistentes' em PluginLoader.__init__
01120. [x] app\infrastructure\plugins\loader.py:35 — revisar facet 'docstring em português' em PluginLoader.__init__
01121. [x] app\infrastructure\plugins\loader.py:35 — revisar facet 'nomenclatura clara (PEP8)' em PluginLoader.__init__
01122. [x] app\infrastructure\plugins\loader.py:35 — revisar facet 'type hints presentes' em PluginLoader.__init__
01123. [x] app\infrastructure\plugins\loader.py:35 — revisar facet 'tratamento de erros adequado' em PluginLoader.__init__
01124. [x] app\infrastructure\plugins\loader.py:35 — revisar facet 'sem comentários inline desnecessários' em PluginLoader.__init__
01125. [x] app\infrastructure\plugins\loader.py:35 — revisar facet 'não imprime side-effects na UI/IO' em PluginLoader.__init__
01126. [x] app\infrastructure\plugins\loader.py:35 — revisar facet 'thread-safety revisada' em PluginLoader.__init__
01127. [x] app\infrastructure\plugins\loader.py:35 — revisar facet 'performance (sem loops O(n^2))' em PluginLoader.__init__
01128. [x] app\infrastructure\plugins\loader.py:35 — revisar facet 'coberto por testes' em PluginLoader.__init__
01129. [x] app\infrastructure\plugins\loader.py:36 — atribuição: PluginLoader.__init__ ← ?
01130. [x] app\infrastructure\plugins\loader.py:37 — atribuição: PluginLoader.__init__ ← ?
01131. [x] app\infrastructure\plugins\loader.py:39 — definir/revisar FunctionDef: PluginLoader.discover
01132. [x] app\infrastructure\plugins\loader.py:39 — revisar facet 'assinatura/args consistentes' em PluginLoader.discover
01133. [x] app\infrastructure\plugins\loader.py:39 — revisar facet 'docstring em português' em PluginLoader.discover
01134. [x] app\infrastructure\plugins\loader.py:39 — revisar facet 'nomenclatura clara (PEP8)' em PluginLoader.discover
01135. [x] app\infrastructure\plugins\loader.py:39 — revisar facet 'type hints presentes' em PluginLoader.discover
01136. [x] app\infrastructure\plugins\loader.py:39 — revisar facet 'tratamento de erros adequado' em PluginLoader.discover
01137. [x] app\infrastructure\plugins\loader.py:39 — revisar facet 'sem comentários inline desnecessários' em PluginLoader.discover
01138. [x] app\infrastructure\plugins\loader.py:39 — revisar facet 'não imprime side-effects na UI/IO' em PluginLoader.discover
01139. [x] app\infrastructure\plugins\loader.py:39 — revisar facet 'thread-safety revisada' em PluginLoader.discover
01140. [x] app\infrastructure\plugins\loader.py:39 — revisar facet 'performance (sem loops O(n^2))' em PluginLoader.discover
01141. [x] app\infrastructure\plugins\loader.py:39 — revisar facet 'coberto por testes' em PluginLoader.discover
01142. [x] app\infrastructure\plugins\loader.py:40 — atribuição: PluginLoader.discover ← report
01143. [x] app\infrastructure\plugins\loader.py:41 — controle if em PluginLoader.discover
01144. [x] app\infrastructure\plugins\loader.py:42 — return em PluginLoader.discover
01145. [x] app\infrastructure\plugins\loader.py:44 — controle for em PluginLoader.discover
01146. [x] app\infrastructure\plugins\loader.py:45 — controle if em PluginLoader.discover
01147. [x] app\infrastructure\plugins\loader.py:48 — controle for em PluginLoader.discover
01148. [x] app\infrastructure\plugins\loader.py:49 — atribuição: PluginLoader.discover ← plugin
01149. [x] app\infrastructure\plugins\loader.py:50 — controle if em PluginLoader.discover
01150. [x] app\infrastructure\plugins\loader.py:56 — return em PluginLoader.discover
01151. [x] app\infrastructure\plugins\loader.py:58 — definir/revisar FunctionDef: PluginLoader._load_file
01152. [x] app\infrastructure\plugins\loader.py:58 — revisar facet 'assinatura/args consistentes' em PluginLoader._load_file
01153. [x] app\infrastructure\plugins\loader.py:58 — revisar facet 'docstring em português' em PluginLoader._load_file
01154. [x] app\infrastructure\plugins\loader.py:58 — revisar facet 'nomenclatura clara (PEP8)' em PluginLoader._load_file
01155. [x] app\infrastructure\plugins\loader.py:58 — revisar facet 'type hints presentes' em PluginLoader._load_file
01156. [x] app\infrastructure\plugins\loader.py:58 — revisar facet 'tratamento de erros adequado' em PluginLoader._load_file
01157. [x] app\infrastructure\plugins\loader.py:58 — revisar facet 'sem comentários inline desnecessários' em PluginLoader._load_file
01158. [x] app\infrastructure\plugins\loader.py:58 — revisar facet 'não imprime side-effects na UI/IO' em PluginLoader._load_file
01159. [x] app\infrastructure\plugins\loader.py:58 — revisar facet 'thread-safety revisada' em PluginLoader._load_file
01160. [x] app\infrastructure\plugins\loader.py:58 — revisar facet 'performance (sem loops O(n^2))' em PluginLoader._load_file
01161. [x] app\infrastructure\plugins\loader.py:58 — revisar facet 'coberto por testes' em PluginLoader._load_file
01162. [x] app\infrastructure\plugins\loader.py:59 — atribuição: PluginLoader._load_file ← module_name
01163. [x] app\infrastructure\plugins\loader.py:62 — try em PluginLoader._load_file
01164. [x] app\infrastructure\plugins\loader.py:63 — atribuição: PluginLoader._load_file ← spec
01165. [x] app\infrastructure\plugins\loader.py:64 — controle if em PluginLoader._load_file
01166. [x] app\infrastructure\plugins\loader.py:66 — return em PluginLoader._load_file
01167. [x] app\infrastructure\plugins\loader.py:68 — atribuição: PluginLoader._load_file ← module
01168. [x] app\infrastructure\plugins\loader.py:69 — atribuição: PluginLoader._load_file ← ?
01169. [x] app\infrastructure\plugins\loader.py:74 — return em PluginLoader._load_file
01170. [x] app\infrastructure\plugins\loader.py:76 — atribuição: PluginLoader._load_file ← found
01171. [x] app\infrastructure\plugins\loader.py:77 — controle for em PluginLoader._load_file
01172. [x] app\infrastructure\plugins\loader.py:78 — atribuição: PluginLoader._load_file ← attr
01173. [x] app\infrastructure\plugins\loader.py:79 — controle if em PluginLoader._load_file
01174. [x] app\infrastructure\plugins\loader.py:86 — atribuição: PluginLoader._load_file ← found
01175. [x] app\infrastructure\plugins\loader.py:88 — controle if em PluginLoader._load_file
01176. [x] app\infrastructure\plugins\loader.py:91 — return em PluginLoader._load_file
01177. [x] app\infrastructure\plugins\loader.py:93 — definir/revisar FunctionDef: PluginLoader.register_all
01178. [x] app\infrastructure\plugins\loader.py:93 — revisar facet 'assinatura/args consistentes' em PluginLoader.register_all
01179. [x] app\infrastructure\plugins\loader.py:93 — revisar facet 'docstring em português' em PluginLoader.register_all
01180. [x] app\infrastructure\plugins\loader.py:93 — revisar facet 'nomenclatura clara (PEP8)' em PluginLoader.register_all
01181. [x] app\infrastructure\plugins\loader.py:93 — revisar facet 'type hints presentes' em PluginLoader.register_all
01182. [x] app\infrastructure\plugins\loader.py:93 — revisar facet 'tratamento de erros adequado' em PluginLoader.register_all
01183. [x] app\infrastructure\plugins\loader.py:93 — revisar facet 'sem comentários inline desnecessários' em PluginLoader.register_all
01184. [x] app\infrastructure\plugins\loader.py:93 — revisar facet 'não imprime side-effects na UI/IO' em PluginLoader.register_all
01185. [x] app\infrastructure\plugins\loader.py:93 — revisar facet 'thread-safety revisada' em PluginLoader.register_all
01186. [x] app\infrastructure\plugins\loader.py:93 — revisar facet 'performance (sem loops O(n^2))' em PluginLoader.register_all
01187. [x] app\infrastructure\plugins\loader.py:93 — revisar facet 'coberto por testes' em PluginLoader.register_all
01188. [x] app\infrastructure\plugins\loader.py:94 — atribuição: PluginLoader.register_all ← report
01189. [x] app\infrastructure\plugins\loader.py:96 — controle for em PluginLoader.register_all
01190. [x] app\infrastructure\plugins\loader.py:97 — try em PluginLoader.register_all
01191. [x] app\infrastructure\plugins\loader.py:105 — atribuição: PluginLoader.register_all ← ?
01192. [x] app\infrastructure\plugins\loader.py:106 — return em PluginLoader.register_all
01193. [x] Existência e estrutura do módulo: app\infrastructure\protocols.py
01194. [x] app\infrastructure\protocols.py:3 — import: __future__
01195. [x] app\infrastructure\protocols.py:5 — import: typing
01196. [x] app\infrastructure\protocols.py:7 — import: numpy
01197. [x] app\infrastructure\protocols.py:9 — import: app.domain.entities
01198. [x] app\infrastructure\protocols.py:12 — definir/revisar ClassDef: DistributionProvider
01199. [x] app\infrastructure\protocols.py:17 — definir/revisar FunctionDef: DistributionProvider.list_distributions
01200. [x] app\infrastructure\protocols.py:17 — revisar facet 'assinatura/args consistentes' em DistributionProvider.list_distributions
01201. [x] app\infrastructure\protocols.py:17 — revisar facet 'docstring em português' em DistributionProvider.list_distributions
01202. [x] app\infrastructure\protocols.py:17 — revisar facet 'nomenclatura clara (PEP8)' em DistributionProvider.list_distributions
01203. [x] app\infrastructure\protocols.py:17 — revisar facet 'type hints presentes' em DistributionProvider.list_distributions
01204. [x] app\infrastructure\protocols.py:17 — revisar facet 'tratamento de erros adequado' em DistributionProvider.list_distributions
01205. [x] app\infrastructure\protocols.py:17 — revisar facet 'sem comentários inline desnecessários' em DistributionProvider.list_distributions
01206. [x] app\infrastructure\protocols.py:17 — revisar facet 'não imprime side-effects na UI/IO' em DistributionProvider.list_distributions
01207. [x] app\infrastructure\protocols.py:17 — revisar facet 'thread-safety revisada' em DistributionProvider.list_distributions
01208. [x] app\infrastructure\protocols.py:17 — revisar facet 'performance (sem loops O(n^2))' em DistributionProvider.list_distributions
01209. [x] app\infrastructure\protocols.py:17 — revisar facet 'coberto por testes' em DistributionProvider.list_distributions
01210. [x] app\infrastructure\protocols.py:19 — definir/revisar FunctionDef: DistributionProvider.parameter_names
01211. [x] app\infrastructure\protocols.py:19 — revisar facet 'assinatura/args consistentes' em DistributionProvider.parameter_names
01212. [x] app\infrastructure\protocols.py:19 — revisar facet 'docstring em português' em DistributionProvider.parameter_names
01213. [x] app\infrastructure\protocols.py:19 — revisar facet 'nomenclatura clara (PEP8)' em DistributionProvider.parameter_names
01214. [x] app\infrastructure\protocols.py:19 — revisar facet 'type hints presentes' em DistributionProvider.parameter_names
01215. [x] app\infrastructure\protocols.py:19 — revisar facet 'tratamento de erros adequado' em DistributionProvider.parameter_names
01216. [x] app\infrastructure\protocols.py:19 — revisar facet 'sem comentários inline desnecessários' em DistributionProvider.parameter_names
01217. [x] app\infrastructure\protocols.py:19 — revisar facet 'não imprime side-effects na UI/IO' em DistributionProvider.parameter_names
01218. [x] app\infrastructure\protocols.py:19 — revisar facet 'thread-safety revisada' em DistributionProvider.parameter_names
01219. [x] app\infrastructure\protocols.py:19 — revisar facet 'performance (sem loops O(n^2))' em DistributionProvider.parameter_names
01220. [x] app\infrastructure\protocols.py:19 — revisar facet 'coberto por testes' em DistributionProvider.parameter_names
01221. [x] app\infrastructure\protocols.py:21 — definir/revisar FunctionDef: DistributionProvider.sample
01222. [x] app\infrastructure\protocols.py:21 — revisar facet 'assinatura/args consistentes' em DistributionProvider.sample
01223. [x] app\infrastructure\protocols.py:21 — revisar facet 'docstring em português' em DistributionProvider.sample
01224. [x] app\infrastructure\protocols.py:21 — revisar facet 'nomenclatura clara (PEP8)' em DistributionProvider.sample
01225. [x] app\infrastructure\protocols.py:21 — revisar facet 'type hints presentes' em DistributionProvider.sample
01226. [x] app\infrastructure\protocols.py:21 — revisar facet 'tratamento de erros adequado' em DistributionProvider.sample
01227. [x] app\infrastructure\protocols.py:21 — revisar facet 'sem comentários inline desnecessários' em DistributionProvider.sample
01228. [x] app\infrastructure\protocols.py:21 — revisar facet 'não imprime side-effects na UI/IO' em DistributionProvider.sample
01229. [x] app\infrastructure\protocols.py:21 — revisar facet 'thread-safety revisada' em DistributionProvider.sample
01230. [x] app\infrastructure\protocols.py:21 — revisar facet 'performance (sem loops O(n^2))' em DistributionProvider.sample
01231. [x] app\infrastructure\protocols.py:21 — revisar facet 'coberto por testes' em DistributionProvider.sample
01232. [x] app\infrastructure\protocols.py:28 — definir/revisar FunctionDef: DistributionProvider.ppf
01233. [x] app\infrastructure\protocols.py:28 — revisar facet 'assinatura/args consistentes' em DistributionProvider.ppf
01234. [x] app\infrastructure\protocols.py:28 — revisar facet 'docstring em português' em DistributionProvider.ppf
01235. [x] app\infrastructure\protocols.py:28 — revisar facet 'nomenclatura clara (PEP8)' em DistributionProvider.ppf
01236. [x] app\infrastructure\protocols.py:28 — revisar facet 'type hints presentes' em DistributionProvider.ppf
01237. [x] app\infrastructure\protocols.py:28 — revisar facet 'tratamento de erros adequado' em DistributionProvider.ppf
01238. [x] app\infrastructure\protocols.py:28 — revisar facet 'sem comentários inline desnecessários' em DistributionProvider.ppf
01239. [x] app\infrastructure\protocols.py:28 — revisar facet 'não imprime side-effects na UI/IO' em DistributionProvider.ppf
01240. [x] app\infrastructure\protocols.py:28 — revisar facet 'thread-safety revisada' em DistributionProvider.ppf
01241. [x] app\infrastructure\protocols.py:28 — revisar facet 'performance (sem loops O(n^2))' em DistributionProvider.ppf
01242. [x] app\infrastructure\protocols.py:28 — revisar facet 'coberto por testes' em DistributionProvider.ppf
01243. [x] app\infrastructure\protocols.py:30 — definir/revisar FunctionDef: DistributionProvider.validate
01244. [x] app\infrastructure\protocols.py:30 — revisar facet 'assinatura/args consistentes' em DistributionProvider.validate
01245. [x] app\infrastructure\protocols.py:30 — revisar facet 'docstring em português' em DistributionProvider.validate
01246. [x] app\infrastructure\protocols.py:30 — revisar facet 'nomenclatura clara (PEP8)' em DistributionProvider.validate
01247. [x] app\infrastructure\protocols.py:30 — revisar facet 'type hints presentes' em DistributionProvider.validate
01248. [x] app\infrastructure\protocols.py:30 — revisar facet 'tratamento de erros adequado' em DistributionProvider.validate
01249. [x] app\infrastructure\protocols.py:30 — revisar facet 'sem comentários inline desnecessários' em DistributionProvider.validate
01250. [x] app\infrastructure\protocols.py:30 — revisar facet 'não imprime side-effects na UI/IO' em DistributionProvider.validate
01251. [x] app\infrastructure\protocols.py:30 — revisar facet 'thread-safety revisada' em DistributionProvider.validate
01252. [x] app\infrastructure\protocols.py:30 — revisar facet 'performance (sem loops O(n^2))' em DistributionProvider.validate
01253. [x] app\infrastructure\protocols.py:30 — revisar facet 'coberto por testes' em DistributionProvider.validate
01254. [x] app\infrastructure\protocols.py:33 — definir/revisar ClassDef: LogRepository
01255. [x] app\infrastructure\protocols.py:34 — definir/revisar FunctionDef: LogRepository.log
01256. [x] app\infrastructure\protocols.py:34 — revisar facet 'assinatura/args consistentes' em LogRepository.log
01257. [x] app\infrastructure\protocols.py:34 — revisar facet 'docstring em português' em LogRepository.log
01258. [x] app\infrastructure\protocols.py:34 — revisar facet 'nomenclatura clara (PEP8)' em LogRepository.log
01259. [x] app\infrastructure\protocols.py:34 — revisar facet 'type hints presentes' em LogRepository.log
01260. [x] app\infrastructure\protocols.py:34 — revisar facet 'tratamento de erros adequado' em LogRepository.log
01261. [x] app\infrastructure\protocols.py:34 — revisar facet 'sem comentários inline desnecessários' em LogRepository.log
01262. [x] app\infrastructure\protocols.py:34 — revisar facet 'não imprime side-effects na UI/IO' em LogRepository.log
01263. [x] app\infrastructure\protocols.py:34 — revisar facet 'thread-safety revisada' em LogRepository.log
01264. [x] app\infrastructure\protocols.py:34 — revisar facet 'performance (sem loops O(n^2))' em LogRepository.log
01265. [x] app\infrastructure\protocols.py:34 — revisar facet 'coberto por testes' em LogRepository.log
01266. [x] app\infrastructure\protocols.py:45 — definir/revisar FunctionDef: LogRepository.fetch
01267. [x] app\infrastructure\protocols.py:45 — revisar facet 'assinatura/args consistentes' em LogRepository.fetch
01268. [x] app\infrastructure\protocols.py:45 — revisar facet 'docstring em português' em LogRepository.fetch
01269. [x] app\infrastructure\protocols.py:45 — revisar facet 'nomenclatura clara (PEP8)' em LogRepository.fetch
01270. [x] app\infrastructure\protocols.py:45 — revisar facet 'type hints presentes' em LogRepository.fetch
01271. [x] app\infrastructure\protocols.py:45 — revisar facet 'tratamento de erros adequado' em LogRepository.fetch
01272. [x] app\infrastructure\protocols.py:45 — revisar facet 'sem comentários inline desnecessários' em LogRepository.fetch
01273. [x] app\infrastructure\protocols.py:45 — revisar facet 'não imprime side-effects na UI/IO' em LogRepository.fetch
01274. [x] app\infrastructure\protocols.py:45 — revisar facet 'thread-safety revisada' em LogRepository.fetch
01275. [x] app\infrastructure\protocols.py:45 — revisar facet 'performance (sem loops O(n^2))' em LogRepository.fetch
01276. [x] app\infrastructure\protocols.py:45 — revisar facet 'coberto por testes' em LogRepository.fetch
01277. [x] app\infrastructure\protocols.py:54 — definir/revisar ClassDef: SamplingStrategy
01278. [x] app\infrastructure\protocols.py:57 — definir/revisar FunctionDef: SamplingStrategy.generate_uniforms
01279. [x] app\infrastructure\protocols.py:57 — revisar facet 'assinatura/args consistentes' em SamplingStrategy.generate_uniforms
01280. [x] app\infrastructure\protocols.py:57 — revisar facet 'docstring em português' em SamplingStrategy.generate_uniforms
01281. [x] app\infrastructure\protocols.py:57 — revisar facet 'nomenclatura clara (PEP8)' em SamplingStrategy.generate_uniforms
01282. [x] app\infrastructure\protocols.py:57 — revisar facet 'type hints presentes' em SamplingStrategy.generate_uniforms
01283. [x] app\infrastructure\protocols.py:57 — revisar facet 'tratamento de erros adequado' em SamplingStrategy.generate_uniforms
01284. [x] app\infrastructure\protocols.py:57 — revisar facet 'sem comentários inline desnecessários' em SamplingStrategy.generate_uniforms
01285. [x] app\infrastructure\protocols.py:57 — revisar facet 'não imprime side-effects na UI/IO' em SamplingStrategy.generate_uniforms
01286. [x] app\infrastructure\protocols.py:57 — revisar facet 'thread-safety revisada' em SamplingStrategy.generate_uniforms
01287. [x] app\infrastructure\protocols.py:57 — revisar facet 'performance (sem loops O(n^2))' em SamplingStrategy.generate_uniforms
01288. [x] app\infrastructure\protocols.py:57 — revisar facet 'coberto por testes' em SamplingStrategy.generate_uniforms
01289. [x] Existência e estrutura do módulo: app\infrastructure\providers\__init__.py
01290. [x] app\infrastructure\providers\__init__.py:3 — import: app.infrastructure.providers.base
01291. [x] app\infrastructure\providers\__init__.py:4 — import: app.infrastructure.providers.fixed_provider
01292. [x] app\infrastructure\providers\__init__.py:5 — import: app.infrastructure.providers.scipy_provider
01293. [x] app\infrastructure\providers\__init__.py:7 — atribuição:  ← __all__
01294. [x] Existência e estrutura do módulo: app\infrastructure\providers\base.py
01295. [x] app\infrastructure\providers\base.py:1 — import: __future__
01296. [x] app\infrastructure\providers\base.py:3 — import: abc
01297. [x] app\infrastructure\providers\base.py:4 — import: typing
01298. [x] app\infrastructure\providers\base.py:6 — import: numpy
01299. [x] app\infrastructure\providers\base.py:8 — import: app.domain.entities
01300. [x] app\infrastructure\providers\base.py:11 — definir/revisar ClassDef: BaseDistributionProvider
01301. [x] app\infrastructure\providers\base.py:18 — definir/revisar FunctionDef: BaseDistributionProvider.list_distributions
01302. [x] app\infrastructure\providers\base.py:18 — revisar facet 'assinatura/args consistentes' em BaseDistributionProvider.list_distributions
01303. [x] app\infrastructure\providers\base.py:18 — revisar facet 'docstring em português' em BaseDistributionProvider.list_distributions
01304. [x] app\infrastructure\providers\base.py:18 — revisar facet 'nomenclatura clara (PEP8)' em BaseDistributionProvider.list_distributions
01305. [x] app\infrastructure\providers\base.py:18 — revisar facet 'type hints presentes' em BaseDistributionProvider.list_distributions
01306. [x] app\infrastructure\providers\base.py:18 — revisar facet 'tratamento de erros adequado' em BaseDistributionProvider.list_distributions
01307. [x] app\infrastructure\providers\base.py:18 — revisar facet 'sem comentários inline desnecessários' em BaseDistributionProvider.list_distributions
01308. [x] app\infrastructure\providers\base.py:18 — revisar facet 'não imprime side-effects na UI/IO' em BaseDistributionProvider.list_distributions
01309. [x] app\infrastructure\providers\base.py:18 — revisar facet 'thread-safety revisada' em BaseDistributionProvider.list_distributions
01310. [x] app\infrastructure\providers\base.py:18 — revisar facet 'performance (sem loops O(n^2))' em BaseDistributionProvider.list_distributions
01311. [x] app\infrastructure\providers\base.py:18 — revisar facet 'coberto por testes' em BaseDistributionProvider.list_distributions
01312. [x] app\infrastructure\providers\base.py:21 — definir/revisar FunctionDef: BaseDistributionProvider.parameter_names
01313. [x] app\infrastructure\providers\base.py:21 — revisar facet 'assinatura/args consistentes' em BaseDistributionProvider.parameter_names
01314. [x] app\infrastructure\providers\base.py:21 — revisar facet 'docstring em português' em BaseDistributionProvider.parameter_names
01315. [x] app\infrastructure\providers\base.py:21 — revisar facet 'nomenclatura clara (PEP8)' em BaseDistributionProvider.parameter_names
01316. [x] app\infrastructure\providers\base.py:21 — revisar facet 'type hints presentes' em BaseDistributionProvider.parameter_names
01317. [x] app\infrastructure\providers\base.py:21 — revisar facet 'tratamento de erros adequado' em BaseDistributionProvider.parameter_names
01318. [x] app\infrastructure\providers\base.py:21 — revisar facet 'sem comentários inline desnecessários' em BaseDistributionProvider.parameter_names
01319. [x] app\infrastructure\providers\base.py:21 — revisar facet 'não imprime side-effects na UI/IO' em BaseDistributionProvider.parameter_names
01320. [x] app\infrastructure\providers\base.py:21 — revisar facet 'thread-safety revisada' em BaseDistributionProvider.parameter_names
01321. [x] app\infrastructure\providers\base.py:21 — revisar facet 'performance (sem loops O(n^2))' em BaseDistributionProvider.parameter_names
01322. [x] app\infrastructure\providers\base.py:21 — revisar facet 'coberto por testes' em BaseDistributionProvider.parameter_names
01323. [x] app\infrastructure\providers\base.py:24 — definir/revisar FunctionDef: BaseDistributionProvider.sample
01324. [x] app\infrastructure\providers\base.py:24 — revisar facet 'assinatura/args consistentes' em BaseDistributionProvider.sample
01325. [x] app\infrastructure\providers\base.py:24 — revisar facet 'docstring em português' em BaseDistributionProvider.sample
01326. [x] app\infrastructure\providers\base.py:24 — revisar facet 'nomenclatura clara (PEP8)' em BaseDistributionProvider.sample
01327. [x] app\infrastructure\providers\base.py:24 — revisar facet 'type hints presentes' em BaseDistributionProvider.sample
01328. [x] app\infrastructure\providers\base.py:24 — revisar facet 'tratamento de erros adequado' em BaseDistributionProvider.sample
01329. [x] app\infrastructure\providers\base.py:24 — revisar facet 'sem comentários inline desnecessários' em BaseDistributionProvider.sample
01330. [x] app\infrastructure\providers\base.py:24 — revisar facet 'não imprime side-effects na UI/IO' em BaseDistributionProvider.sample
01331. [x] app\infrastructure\providers\base.py:24 — revisar facet 'thread-safety revisada' em BaseDistributionProvider.sample
01332. [x] app\infrastructure\providers\base.py:24 — revisar facet 'performance (sem loops O(n^2))' em BaseDistributionProvider.sample
01333. [x] app\infrastructure\providers\base.py:24 — revisar facet 'coberto por testes' em BaseDistributionProvider.sample
01334. [x] app\infrastructure\providers\base.py:32 — definir/revisar FunctionDef: BaseDistributionProvider.validate
01335. [x] app\infrastructure\providers\base.py:32 — revisar facet 'assinatura/args consistentes' em BaseDistributionProvider.validate
01336. [x] app\infrastructure\providers\base.py:32 — revisar facet 'docstring em português' em BaseDistributionProvider.validate
01337. [x] app\infrastructure\providers\base.py:32 — revisar facet 'nomenclatura clara (PEP8)' em BaseDistributionProvider.validate
01338. [x] app\infrastructure\providers\base.py:32 — revisar facet 'type hints presentes' em BaseDistributionProvider.validate
01339. [x] app\infrastructure\providers\base.py:32 — revisar facet 'tratamento de erros adequado' em BaseDistributionProvider.validate
01340. [x] app\infrastructure\providers\base.py:32 — revisar facet 'sem comentários inline desnecessários' em BaseDistributionProvider.validate
01341. [x] app\infrastructure\providers\base.py:32 — revisar facet 'não imprime side-effects na UI/IO' em BaseDistributionProvider.validate
01342. [x] app\infrastructure\providers\base.py:32 — revisar facet 'thread-safety revisada' em BaseDistributionProvider.validate
01343. [x] app\infrastructure\providers\base.py:32 — revisar facet 'performance (sem loops O(n^2))' em BaseDistributionProvider.validate
01344. [x] app\infrastructure\providers\base.py:32 — revisar facet 'coberto por testes' em BaseDistributionProvider.validate
01345. [x] app\infrastructure\providers\base.py:34 — definir/revisar FunctionDef: BaseDistributionProvider.ppf
01346. [x] app\infrastructure\providers\base.py:34 — revisar facet 'assinatura/args consistentes' em BaseDistributionProvider.ppf
01347. [x] app\infrastructure\providers\base.py:34 — revisar facet 'docstring em português' em BaseDistributionProvider.ppf
01348. [x] app\infrastructure\providers\base.py:34 — revisar facet 'nomenclatura clara (PEP8)' em BaseDistributionProvider.ppf
01349. [x] app\infrastructure\providers\base.py:34 — revisar facet 'type hints presentes' em BaseDistributionProvider.ppf
01350. [x] app\infrastructure\providers\base.py:34 — revisar facet 'tratamento de erros adequado' em BaseDistributionProvider.ppf
01351. [x] app\infrastructure\providers\base.py:34 — revisar facet 'sem comentários inline desnecessários' em BaseDistributionProvider.ppf
01352. [x] app\infrastructure\providers\base.py:34 — revisar facet 'não imprime side-effects na UI/IO' em BaseDistributionProvider.ppf
01353. [x] app\infrastructure\providers\base.py:34 — revisar facet 'thread-safety revisada' em BaseDistributionProvider.ppf
01354. [x] app\infrastructure\providers\base.py:34 — revisar facet 'performance (sem loops O(n^2))' em BaseDistributionProvider.ppf
01355. [x] app\infrastructure\providers\base.py:34 — revisar facet 'coberto por testes' em BaseDistributionProvider.ppf
01356. [x] app\infrastructure\providers\base.py:35 — raise em BaseDistributionProvider.ppf
01357. [x] app\infrastructure\providers\base.py:37 — definir/revisar FunctionDef: BaseDistributionProvider.param_schema
01358. [x] app\infrastructure\providers\base.py:37 — revisar facet 'assinatura/args consistentes' em BaseDistributionProvider.param_schema
01359. [x] app\infrastructure\providers\base.py:37 — revisar facet 'docstring em português' em BaseDistributionProvider.param_schema
01360. [x] app\infrastructure\providers\base.py:37 — revisar facet 'nomenclatura clara (PEP8)' em BaseDistributionProvider.param_schema
01361. [x] app\infrastructure\providers\base.py:37 — revisar facet 'type hints presentes' em BaseDistributionProvider.param_schema
01362. [x] app\infrastructure\providers\base.py:37 — revisar facet 'tratamento de erros adequado' em BaseDistributionProvider.param_schema
01363. [x] app\infrastructure\providers\base.py:37 — revisar facet 'sem comentários inline desnecessários' em BaseDistributionProvider.param_schema
01364. [x] app\infrastructure\providers\base.py:37 — revisar facet 'não imprime side-effects na UI/IO' em BaseDistributionProvider.param_schema
01365. [x] app\infrastructure\providers\base.py:37 — revisar facet 'thread-safety revisada' em BaseDistributionProvider.param_schema
01366. [x] app\infrastructure\providers\base.py:37 — revisar facet 'performance (sem loops O(n^2))' em BaseDistributionProvider.param_schema
01367. [x] app\infrastructure\providers\base.py:37 — revisar facet 'coberto por testes' em BaseDistributionProvider.param_schema
01368. [x] app\infrastructure\providers\base.py:39 — return em BaseDistributionProvider.param_schema
01369. [x] Existência e estrutura do módulo: app\infrastructure\providers\fixed_provider.py
01370. [x] app\infrastructure\providers\fixed_provider.py:1 — import: __future__
01371. [x] app\infrastructure\providers\fixed_provider.py:3 — import: typing
01372. [x] app\infrastructure\providers\fixed_provider.py:5 — import: numpy
01373. [x] app\infrastructure\providers\fixed_provider.py:7 — import: app.domain.entities
01374. [x] app\infrastructure\providers\fixed_provider.py:8 — import: app.infrastructure.providers.base
01375. [x] app\infrastructure\providers\fixed_provider.py:11 — definir/revisar ClassDef: FixedProvider
01376. [x] app\infrastructure\providers\fixed_provider.py:14 — atribuição: FixedProvider ← provider_name
01377. [x] app\infrastructure\providers\fixed_provider.py:16 — definir/revisar FunctionDef: FixedProvider.list_distributions
01378. [x] app\infrastructure\providers\fixed_provider.py:16 — revisar facet 'assinatura/args consistentes' em FixedProvider.list_distributions
01379. [x] app\infrastructure\providers\fixed_provider.py:16 — revisar facet 'docstring em português' em FixedProvider.list_distributions
01380. [x] app\infrastructure\providers\fixed_provider.py:16 — revisar facet 'nomenclatura clara (PEP8)' em FixedProvider.list_distributions
01381. [x] app\infrastructure\providers\fixed_provider.py:16 — revisar facet 'type hints presentes' em FixedProvider.list_distributions
01382. [x] app\infrastructure\providers\fixed_provider.py:16 — revisar facet 'tratamento de erros adequado' em FixedProvider.list_distributions
01383. [x] app\infrastructure\providers\fixed_provider.py:16 — revisar facet 'sem comentários inline desnecessários' em FixedProvider.list_distributions
01384. [x] app\infrastructure\providers\fixed_provider.py:16 — revisar facet 'não imprime side-effects na UI/IO' em FixedProvider.list_distributions
01385. [x] app\infrastructure\providers\fixed_provider.py:16 — revisar facet 'thread-safety revisada' em FixedProvider.list_distributions
01386. [x] app\infrastructure\providers\fixed_provider.py:16 — revisar facet 'performance (sem loops O(n^2))' em FixedProvider.list_distributions
01387. [x] app\infrastructure\providers\fixed_provider.py:16 — revisar facet 'coberto por testes' em FixedProvider.list_distributions
01388. [x] app\infrastructure\providers\fixed_provider.py:17 — return em FixedProvider.list_distributions
01389. [x] app\infrastructure\providers\fixed_provider.py:19 — definir/revisar FunctionDef: FixedProvider.parameter_names
01390. [x] app\infrastructure\providers\fixed_provider.py:19 — revisar facet 'assinatura/args consistentes' em FixedProvider.parameter_names
01391. [x] app\infrastructure\providers\fixed_provider.py:19 — revisar facet 'docstring em português' em FixedProvider.parameter_names
01392. [x] app\infrastructure\providers\fixed_provider.py:19 — revisar facet 'nomenclatura clara (PEP8)' em FixedProvider.parameter_names
01393. [x] app\infrastructure\providers\fixed_provider.py:19 — revisar facet 'type hints presentes' em FixedProvider.parameter_names
01394. [x] app\infrastructure\providers\fixed_provider.py:19 — revisar facet 'tratamento de erros adequado' em FixedProvider.parameter_names
01395. [x] app\infrastructure\providers\fixed_provider.py:19 — revisar facet 'sem comentários inline desnecessários' em FixedProvider.parameter_names
01396. [x] app\infrastructure\providers\fixed_provider.py:19 — revisar facet 'não imprime side-effects na UI/IO' em FixedProvider.parameter_names
01397. [x] app\infrastructure\providers\fixed_provider.py:19 — revisar facet 'thread-safety revisada' em FixedProvider.parameter_names
01398. [x] app\infrastructure\providers\fixed_provider.py:19 — revisar facet 'performance (sem loops O(n^2))' em FixedProvider.parameter_names
01399. [x] app\infrastructure\providers\fixed_provider.py:19 — revisar facet 'coberto por testes' em FixedProvider.parameter_names
01400. [x] app\infrastructure\providers\fixed_provider.py:20 — return em FixedProvider.parameter_names
01401. [x] app\infrastructure\providers\fixed_provider.py:22 — definir/revisar FunctionDef: FixedProvider.sample
01402. [x] app\infrastructure\providers\fixed_provider.py:22 — revisar facet 'assinatura/args consistentes' em FixedProvider.sample
01403. [x] app\infrastructure\providers\fixed_provider.py:22 — revisar facet 'docstring em português' em FixedProvider.sample
01404. [x] app\infrastructure\providers\fixed_provider.py:22 — revisar facet 'nomenclatura clara (PEP8)' em FixedProvider.sample
01405. [x] app\infrastructure\providers\fixed_provider.py:22 — revisar facet 'type hints presentes' em FixedProvider.sample
01406. [x] app\infrastructure\providers\fixed_provider.py:22 — revisar facet 'tratamento de erros adequado' em FixedProvider.sample
01407. [x] app\infrastructure\providers\fixed_provider.py:22 — revisar facet 'sem comentários inline desnecessários' em FixedProvider.sample
01408. [x] app\infrastructure\providers\fixed_provider.py:22 — revisar facet 'não imprime side-effects na UI/IO' em FixedProvider.sample
01409. [x] app\infrastructure\providers\fixed_provider.py:22 — revisar facet 'thread-safety revisada' em FixedProvider.sample
01410. [x] app\infrastructure\providers\fixed_provider.py:22 — revisar facet 'performance (sem loops O(n^2))' em FixedProvider.sample
01411. [x] app\infrastructure\providers\fixed_provider.py:22 — revisar facet 'coberto por testes' em FixedProvider.sample
01412. [x] app\infrastructure\providers\fixed_provider.py:23 — return em FixedProvider.sample
01413. [x] app\infrastructure\providers\fixed_provider.py:25 — definir/revisar FunctionDef: FixedProvider.ppf
01414. [x] app\infrastructure\providers\fixed_provider.py:25 — revisar facet 'assinatura/args consistentes' em FixedProvider.ppf
01415. [x] app\infrastructure\providers\fixed_provider.py:25 — revisar facet 'docstring em português' em FixedProvider.ppf
01416. [x] app\infrastructure\providers\fixed_provider.py:25 — revisar facet 'nomenclatura clara (PEP8)' em FixedProvider.ppf
01417. [x] app\infrastructure\providers\fixed_provider.py:25 — revisar facet 'type hints presentes' em FixedProvider.ppf
01418. [x] app\infrastructure\providers\fixed_provider.py:25 — revisar facet 'tratamento de erros adequado' em FixedProvider.ppf
01419. [x] app\infrastructure\providers\fixed_provider.py:25 — revisar facet 'sem comentários inline desnecessários' em FixedProvider.ppf
01420. [x] app\infrastructure\providers\fixed_provider.py:25 — revisar facet 'não imprime side-effects na UI/IO' em FixedProvider.ppf
01421. [x] app\infrastructure\providers\fixed_provider.py:25 — revisar facet 'thread-safety revisada' em FixedProvider.ppf
01422. [x] app\infrastructure\providers\fixed_provider.py:25 — revisar facet 'performance (sem loops O(n^2))' em FixedProvider.ppf
01423. [x] app\infrastructure\providers\fixed_provider.py:25 — revisar facet 'coberto por testes' em FixedProvider.ppf
01424. [x] app\infrastructure\providers\fixed_provider.py:26 — return em FixedProvider.ppf
01425. [x] app\infrastructure\providers\fixed_provider.py:28 — definir/revisar FunctionDef: FixedProvider.validate
01426. [x] app\infrastructure\providers\fixed_provider.py:28 — revisar facet 'assinatura/args consistentes' em FixedProvider.validate
01427. [x] app\infrastructure\providers\fixed_provider.py:28 — revisar facet 'docstring em português' em FixedProvider.validate
01428. [x] app\infrastructure\providers\fixed_provider.py:28 — revisar facet 'nomenclatura clara (PEP8)' em FixedProvider.validate
01429. [x] app\infrastructure\providers\fixed_provider.py:28 — revisar facet 'type hints presentes' em FixedProvider.validate
01430. [x] app\infrastructure\providers\fixed_provider.py:28 — revisar facet 'tratamento de erros adequado' em FixedProvider.validate
01431. [x] app\infrastructure\providers\fixed_provider.py:28 — revisar facet 'sem comentários inline desnecessários' em FixedProvider.validate
01432. [x] app\infrastructure\providers\fixed_provider.py:28 — revisar facet 'não imprime side-effects na UI/IO' em FixedProvider.validate
01433. [x] app\infrastructure\providers\fixed_provider.py:28 — revisar facet 'thread-safety revisada' em FixedProvider.validate
01434. [x] app\infrastructure\providers\fixed_provider.py:28 — revisar facet 'performance (sem loops O(n^2))' em FixedProvider.validate
01435. [x] app\infrastructure\providers\fixed_provider.py:28 — revisar facet 'coberto por testes' em FixedProvider.validate
01436. [x] app\infrastructure\providers\fixed_provider.py:29 — return em FixedProvider.validate
01437. [x] Existência e estrutura do módulo: app\infrastructure\providers\scipy_provider.py
01438. [x] app\infrastructure\providers\scipy_provider.py:1 — import: __future__
01439. [x] app\infrastructure\providers\scipy_provider.py:3 — import: functools
01440. [x] app\infrastructure\providers\scipy_provider.py:4 — import: typing
01441. [x] app\infrastructure\providers\scipy_provider.py:6 — import: numpy
01442. [x] app\infrastructure\providers\scipy_provider.py:7 — import: scipy
01443. [x] app\infrastructure\providers\scipy_provider.py:9 — import: app.domain.entities
01444. [x] app\infrastructure\providers\scipy_provider.py:10 — import: app.infrastructure.providers.base
01445. [x] app\infrastructure\providers\scipy_provider.py:13 — definir/revisar ClassDef: ScipyProvider
01446. [x] app\infrastructure\providers\scipy_provider.py:16 — atribuição: ScipyProvider ← provider_name
01447. [x] app\infrastructure\providers\scipy_provider.py:18 — atribuição: ScipyProvider ← _EXCLUDE
01448. [x] app\infrastructure\providers\scipy_provider.py:23 — definir/revisar FunctionDef: ScipyProvider._discover
01449. [x] app\infrastructure\providers\scipy_provider.py:23 — revisar facet 'assinatura/args consistentes' em ScipyProvider._discover
01450. [x] app\infrastructure\providers\scipy_provider.py:23 — revisar facet 'docstring em português' em ScipyProvider._discover
01451. [x] app\infrastructure\providers\scipy_provider.py:23 — revisar facet 'nomenclatura clara (PEP8)' em ScipyProvider._discover
01452. [x] app\infrastructure\providers\scipy_provider.py:23 — revisar facet 'type hints presentes' em ScipyProvider._discover
01453. [x] app\infrastructure\providers\scipy_provider.py:23 — revisar facet 'tratamento de erros adequado' em ScipyProvider._discover
01454. [x] app\infrastructure\providers\scipy_provider.py:23 — revisar facet 'sem comentários inline desnecessários' em ScipyProvider._discover
01455. [x] app\infrastructure\providers\scipy_provider.py:23 — revisar facet 'não imprime side-effects na UI/IO' em ScipyProvider._discover
01456. [x] app\infrastructure\providers\scipy_provider.py:23 — revisar facet 'thread-safety revisada' em ScipyProvider._discover
01457. [x] app\infrastructure\providers\scipy_provider.py:23 — revisar facet 'performance (sem loops O(n^2))' em ScipyProvider._discover
01458. [x] app\infrastructure\providers\scipy_provider.py:23 — revisar facet 'coberto por testes' em ScipyProvider._discover
01459. [x] app\infrastructure\providers\scipy_provider.py:25 — controle for em ScipyProvider._discover
01460. [x] app\infrastructure\providers\scipy_provider.py:26 — controle if em ScipyProvider._discover
01461. [x] app\infrastructure\providers\scipy_provider.py:28 — atribuição: ScipyProvider._discover ← obj
01462. [x] app\infrastructure\providers\scipy_provider.py:29 — controle if em ScipyProvider._discover
01463. [x] app\infrastructure\providers\scipy_provider.py:30 — atribuição: ScipyProvider._discover ← ?
01464. [x] app\infrastructure\providers\scipy_provider.py:31 — return em ScipyProvider._discover
01465. [x] app\infrastructure\providers\scipy_provider.py:33 — definir/revisar FunctionDef: ScipyProvider.list_distributions
01466. [x] app\infrastructure\providers\scipy_provider.py:33 — revisar facet 'assinatura/args consistentes' em ScipyProvider.list_distributions
01467. [x] app\infrastructure\providers\scipy_provider.py:33 — revisar facet 'docstring em português' em ScipyProvider.list_distributions
01468. [x] app\infrastructure\providers\scipy_provider.py:33 — revisar facet 'nomenclatura clara (PEP8)' em ScipyProvider.list_distributions
01469. [x] app\infrastructure\providers\scipy_provider.py:33 — revisar facet 'type hints presentes' em ScipyProvider.list_distributions
01470. [x] app\infrastructure\providers\scipy_provider.py:33 — revisar facet 'tratamento de erros adequado' em ScipyProvider.list_distributions
01471. [x] app\infrastructure\providers\scipy_provider.py:33 — revisar facet 'sem comentários inline desnecessários' em ScipyProvider.list_distributions
01472. [x] app\infrastructure\providers\scipy_provider.py:33 — revisar facet 'não imprime side-effects na UI/IO' em ScipyProvider.list_distributions
01473. [x] app\infrastructure\providers\scipy_provider.py:33 — revisar facet 'thread-safety revisada' em ScipyProvider.list_distributions
01474. [x] app\infrastructure\providers\scipy_provider.py:33 — revisar facet 'performance (sem loops O(n^2))' em ScipyProvider.list_distributions
01475. [x] app\infrastructure\providers\scipy_provider.py:33 — revisar facet 'coberto por testes' em ScipyProvider.list_distributions
01476. [x] app\infrastructure\providers\scipy_provider.py:34 — return em ScipyProvider.list_distributions
01477. [x] app\infrastructure\providers\scipy_provider.py:37 — definir/revisar FunctionDef: ScipyProvider.parameter_names
01478. [x] app\infrastructure\providers\scipy_provider.py:37 — revisar facet 'assinatura/args consistentes' em ScipyProvider.parameter_names
01479. [x] app\infrastructure\providers\scipy_provider.py:37 — revisar facet 'docstring em português' em ScipyProvider.parameter_names
01480. [x] app\infrastructure\providers\scipy_provider.py:37 — revisar facet 'nomenclatura clara (PEP8)' em ScipyProvider.parameter_names
01481. [x] app\infrastructure\providers\scipy_provider.py:37 — revisar facet 'type hints presentes' em ScipyProvider.parameter_names
01482. [x] app\infrastructure\providers\scipy_provider.py:37 — revisar facet 'tratamento de erros adequado' em ScipyProvider.parameter_names
01483. [x] app\infrastructure\providers\scipy_provider.py:37 — revisar facet 'sem comentários inline desnecessários' em ScipyProvider.parameter_names
01484. [x] app\infrastructure\providers\scipy_provider.py:37 — revisar facet 'não imprime side-effects na UI/IO' em ScipyProvider.parameter_names
01485. [x] app\infrastructure\providers\scipy_provider.py:37 — revisar facet 'thread-safety revisada' em ScipyProvider.parameter_names
01486. [x] app\infrastructure\providers\scipy_provider.py:37 — revisar facet 'performance (sem loops O(n^2))' em ScipyProvider.parameter_names
01487. [x] app\infrastructure\providers\scipy_provider.py:37 — revisar facet 'coberto por testes' em ScipyProvider.parameter_names
01488. [x] app\infrastructure\providers\scipy_provider.py:38 — atribuição: ScipyProvider.parameter_names ← dist
01489. [x] app\infrastructure\providers\scipy_provider.py:39 — atribuição: ScipyProvider.parameter_names ← shapes
01490. [x] app\infrastructure\providers\scipy_provider.py:40 — atribuição: ScipyProvider.parameter_names ← names
01491. [x] app\infrastructure\providers\scipy_provider.py:42 — controle if em ScipyProvider.parameter_names
01492. [x] app\infrastructure\providers\scipy_provider.py:44 — return em ScipyProvider.parameter_names
01493. [x] app\infrastructure\providers\scipy_provider.py:46 — definir/revisar FunctionDef: ScipyProvider._build
01494. [x] app\infrastructure\providers\scipy_provider.py:46 — revisar facet 'assinatura/args consistentes' em ScipyProvider._build
01495. [x] app\infrastructure\providers\scipy_provider.py:46 — revisar facet 'docstring em português' em ScipyProvider._build
01496. [x] app\infrastructure\providers\scipy_provider.py:46 — revisar facet 'nomenclatura clara (PEP8)' em ScipyProvider._build
01497. [x] app\infrastructure\providers\scipy_provider.py:46 — revisar facet 'type hints presentes' em ScipyProvider._build
01498. [x] app\infrastructure\providers\scipy_provider.py:46 — revisar facet 'tratamento de erros adequado' em ScipyProvider._build
01499. [x] app\infrastructure\providers\scipy_provider.py:46 — revisar facet 'sem comentários inline desnecessários' em ScipyProvider._build
01500. [x] app\infrastructure\providers\scipy_provider.py:46 — revisar facet 'não imprime side-effects na UI/IO' em ScipyProvider._build
01501. [x] app\infrastructure\providers\scipy_provider.py:46 — revisar facet 'thread-safety revisada' em ScipyProvider._build
01502. [x] app\infrastructure\providers\scipy_provider.py:46 — revisar facet 'performance (sem loops O(n^2))' em ScipyProvider._build
01503. [x] app\infrastructure\providers\scipy_provider.py:46 — revisar facet 'coberto por testes' em ScipyProvider._build
01504. [x] app\infrastructure\providers\scipy_provider.py:47 — atribuição: ScipyProvider._build ← dist
01505. [x] app\infrastructure\providers\scipy_provider.py:48 — controle if em ScipyProvider._build
01506. [x] app\infrastructure\providers\scipy_provider.py:49 — raise em ScipyProvider._build
01507. [x] app\infrastructure\providers\scipy_provider.py:50 — atribuição: ScipyProvider._build ← params
01508. [x] app\infrastructure\providers\scipy_provider.py:51 — atribuição: ScipyProvider._build ← shapes
01509. [x] app\infrastructure\providers\scipy_provider.py:52 — atribuição: ScipyProvider._build ← args
01510. [x] app\infrastructure\providers\scipy_provider.py:53 — atribuição: ScipyProvider._build ← kwargs
01511. [x] app\infrastructure\providers\scipy_provider.py:54 — controle if em ScipyProvider._build
01512. [x] app\infrastructure\providers\scipy_provider.py:55 — atribuição: ScipyProvider._build ← ?
01513. [x] app\infrastructure\providers\scipy_provider.py:56 — return em ScipyProvider._build
01514. [x] app\infrastructure\providers\scipy_provider.py:58 — definir/revisar FunctionDef: ScipyProvider.sample
01515. [x] app\infrastructure\providers\scipy_provider.py:58 — revisar facet 'assinatura/args consistentes' em ScipyProvider.sample
01516. [x] app\infrastructure\providers\scipy_provider.py:58 — revisar facet 'docstring em português' em ScipyProvider.sample
01517. [x] app\infrastructure\providers\scipy_provider.py:58 — revisar facet 'nomenclatura clara (PEP8)' em ScipyProvider.sample
01518. [x] app\infrastructure\providers\scipy_provider.py:58 — revisar facet 'type hints presentes' em ScipyProvider.sample
01519. [x] app\infrastructure\providers\scipy_provider.py:58 — revisar facet 'tratamento de erros adequado' em ScipyProvider.sample
01520. [x] app\infrastructure\providers\scipy_provider.py:58 — revisar facet 'sem comentários inline desnecessários' em ScipyProvider.sample
01521. [x] app\infrastructure\providers\scipy_provider.py:58 — revisar facet 'não imprime side-effects na UI/IO' em ScipyProvider.sample
01522. [x] app\infrastructure\providers\scipy_provider.py:58 — revisar facet 'thread-safety revisada' em ScipyProvider.sample
01523. [x] app\infrastructure\providers\scipy_provider.py:58 — revisar facet 'performance (sem loops O(n^2))' em ScipyProvider.sample
01524. [x] app\infrastructure\providers\scipy_provider.py:58 — revisar facet 'coberto por testes' em ScipyProvider.sample
01525. [x] app\infrastructure\providers\scipy_provider.py:59 — atribuição: ScipyProvider.sample ← ?
01526. [x] app\infrastructure\providers\scipy_provider.py:60 — return em ScipyProvider.sample
01527. [x] app\infrastructure\providers\scipy_provider.py:62 — definir/revisar FunctionDef: ScipyProvider.ppf
01528. [x] app\infrastructure\providers\scipy_provider.py:62 — revisar facet 'assinatura/args consistentes' em ScipyProvider.ppf
01529. [x] app\infrastructure\providers\scipy_provider.py:62 — revisar facet 'docstring em português' em ScipyProvider.ppf
01530. [x] app\infrastructure\providers\scipy_provider.py:62 — revisar facet 'nomenclatura clara (PEP8)' em ScipyProvider.ppf
01531. [x] app\infrastructure\providers\scipy_provider.py:62 — revisar facet 'type hints presentes' em ScipyProvider.ppf
01532. [x] app\infrastructure\providers\scipy_provider.py:62 — revisar facet 'tratamento de erros adequado' em ScipyProvider.ppf
01533. [x] app\infrastructure\providers\scipy_provider.py:62 — revisar facet 'sem comentários inline desnecessários' em ScipyProvider.ppf
01534. [x] app\infrastructure\providers\scipy_provider.py:62 — revisar facet 'não imprime side-effects na UI/IO' em ScipyProvider.ppf
01535. [x] app\infrastructure\providers\scipy_provider.py:62 — revisar facet 'thread-safety revisada' em ScipyProvider.ppf
01536. [x] app\infrastructure\providers\scipy_provider.py:62 — revisar facet 'performance (sem loops O(n^2))' em ScipyProvider.ppf
01537. [x] app\infrastructure\providers\scipy_provider.py:62 — revisar facet 'coberto por testes' em ScipyProvider.ppf
01538. [x] app\infrastructure\providers\scipy_provider.py:63 — atribuição: ScipyProvider.ppf ← ?
01539. [x] app\infrastructure\providers\scipy_provider.py:64 — return em ScipyProvider.ppf
01540. [x] app\infrastructure\providers\scipy_provider.py:66 — definir/revisar FunctionDef: ScipyProvider.validate
01541. [x] app\infrastructure\providers\scipy_provider.py:66 — revisar facet 'assinatura/args consistentes' em ScipyProvider.validate
01542. [x] app\infrastructure\providers\scipy_provider.py:66 — revisar facet 'docstring em português' em ScipyProvider.validate
01543. [x] app\infrastructure\providers\scipy_provider.py:66 — revisar facet 'nomenclatura clara (PEP8)' em ScipyProvider.validate
01544. [x] app\infrastructure\providers\scipy_provider.py:66 — revisar facet 'type hints presentes' em ScipyProvider.validate
01545. [x] app\infrastructure\providers\scipy_provider.py:66 — revisar facet 'tratamento de erros adequado' em ScipyProvider.validate
01546. [x] app\infrastructure\providers\scipy_provider.py:66 — revisar facet 'sem comentários inline desnecessários' em ScipyProvider.validate
01547. [x] app\infrastructure\providers\scipy_provider.py:66 — revisar facet 'não imprime side-effects na UI/IO' em ScipyProvider.validate
01548. [x] app\infrastructure\providers\scipy_provider.py:66 — revisar facet 'thread-safety revisada' em ScipyProvider.validate
01549. [x] app\infrastructure\providers\scipy_provider.py:66 — revisar facet 'performance (sem loops O(n^2))' em ScipyProvider.validate
01550. [x] app\infrastructure\providers\scipy_provider.py:66 — revisar facet 'coberto por testes' em ScipyProvider.validate
01551. [x] app\infrastructure\providers\scipy_provider.py:67 — atribuição: ScipyProvider.validate ← errors
01552. [x] app\infrastructure\providers\scipy_provider.py:68 — controle if em ScipyProvider.validate
01553. [x] app\infrastructure\providers\scipy_provider.py:69 — return em ScipyProvider.validate
01554. [x] app\infrastructure\providers\scipy_provider.py:70 — try em ScipyProvider.validate
01555. [x] app\infrastructure\providers\scipy_provider.py:74 — return em ScipyProvider.validate
01556. [x] Existência e estrutura do módulo: app\infrastructure\task_repository.py
01557. [x] app\infrastructure\task_repository.py:3 — import: __future__
01558. [x] app\infrastructure\task_repository.py:5 — import: json
01559. [x] app\infrastructure\task_repository.py:6 — import: sqlite3
01560. [x] app\infrastructure\task_repository.py:7 — import: datetime
01561. [x] app\infrastructure\task_repository.py:8 — import: pathlib
01562. [x] app\infrastructure\task_repository.py:9 — import: typing
01563. [x] app\infrastructure\task_repository.py:11 — import: app.domain.tasks
01564. [x] app\infrastructure\task_repository.py:14 — definir/revisar ClassDef: TaskRepository
01565. [x] app\infrastructure\task_repository.py:15 — definir/revisar FunctionDef: TaskRepository.__init__
01566. [x] app\infrastructure\task_repository.py:15 — revisar facet 'assinatura/args consistentes' em TaskRepository.__init__
01567. [x] app\infrastructure\task_repository.py:15 — revisar facet 'docstring em português' em TaskRepository.__init__
01568. [x] app\infrastructure\task_repository.py:15 — revisar facet 'nomenclatura clara (PEP8)' em TaskRepository.__init__
01569. [x] app\infrastructure\task_repository.py:15 — revisar facet 'type hints presentes' em TaskRepository.__init__
01570. [x] app\infrastructure\task_repository.py:15 — revisar facet 'tratamento de erros adequado' em TaskRepository.__init__
01571. [x] app\infrastructure\task_repository.py:15 — revisar facet 'sem comentários inline desnecessários' em TaskRepository.__init__
01572. [x] app\infrastructure\task_repository.py:15 — revisar facet 'não imprime side-effects na UI/IO' em TaskRepository.__init__
01573. [x] app\infrastructure\task_repository.py:15 — revisar facet 'thread-safety revisada' em TaskRepository.__init__
01574. [x] app\infrastructure\task_repository.py:15 — revisar facet 'performance (sem loops O(n^2))' em TaskRepository.__init__
01575. [x] app\infrastructure\task_repository.py:15 — revisar facet 'coberto por testes' em TaskRepository.__init__
01576. [x] app\infrastructure\task_repository.py:16 — controle if em TaskRepository.__init__
01577. [x] app\infrastructure\task_repository.py:18 — atribuição: TaskRepository.__init__ ← ?
01578. [x] app\infrastructure\task_repository.py:19 — atribuição: TaskRepository.__init__ ← ?
01579. [x] app\infrastructure\task_repository.py:22 — definir/revisar FunctionDef: TaskRepository._create_schema
01580. [x] app\infrastructure\task_repository.py:22 — revisar facet 'assinatura/args consistentes' em TaskRepository._create_schema
01581. [x] app\infrastructure\task_repository.py:22 — revisar facet 'docstring em português' em TaskRepository._create_schema
01582. [x] app\infrastructure\task_repository.py:22 — revisar facet 'nomenclatura clara (PEP8)' em TaskRepository._create_schema
01583. [x] app\infrastructure\task_repository.py:22 — revisar facet 'type hints presentes' em TaskRepository._create_schema
01584. [x] app\infrastructure\task_repository.py:22 — revisar facet 'tratamento de erros adequado' em TaskRepository._create_schema
01585. [x] app\infrastructure\task_repository.py:22 — revisar facet 'sem comentários inline desnecessários' em TaskRepository._create_schema
01586. [x] app\infrastructure\task_repository.py:22 — revisar facet 'não imprime side-effects na UI/IO' em TaskRepository._create_schema
01587. [x] app\infrastructure\task_repository.py:22 — revisar facet 'thread-safety revisada' em TaskRepository._create_schema
01588. [x] app\infrastructure\task_repository.py:22 — revisar facet 'performance (sem loops O(n^2))' em TaskRepository._create_schema
01589. [x] app\infrastructure\task_repository.py:22 — revisar facet 'coberto por testes' em TaskRepository._create_schema
01590. [x] app\infrastructure\task_repository.py:23 — controle with em TaskRepository._create_schema
01591. [x] app\infrastructure\task_repository.py:42 — definir/revisar FunctionDef: TaskRepository.create
01592. [x] app\infrastructure\task_repository.py:42 — revisar facet 'assinatura/args consistentes' em TaskRepository.create
01593. [x] app\infrastructure\task_repository.py:42 — revisar facet 'docstring em português' em TaskRepository.create
01594. [x] app\infrastructure\task_repository.py:42 — revisar facet 'nomenclatura clara (PEP8)' em TaskRepository.create
01595. [x] app\infrastructure\task_repository.py:42 — revisar facet 'type hints presentes' em TaskRepository.create
01596. [x] app\infrastructure\task_repository.py:42 — revisar facet 'tratamento de erros adequado' em TaskRepository.create
01597. [x] app\infrastructure\task_repository.py:42 — revisar facet 'sem comentários inline desnecessários' em TaskRepository.create
01598. [x] app\infrastructure\task_repository.py:42 — revisar facet 'não imprime side-effects na UI/IO' em TaskRepository.create
01599. [x] app\infrastructure\task_repository.py:42 — revisar facet 'thread-safety revisada' em TaskRepository.create
01600. [x] app\infrastructure\task_repository.py:42 — revisar facet 'performance (sem loops O(n^2))' em TaskRepository.create
01601. [x] app\infrastructure\task_repository.py:42 — revisar facet 'coberto por testes' em TaskRepository.create
01602. [x] app\infrastructure\task_repository.py:43 — atribuição: TaskRepository.create ← now
01603. [x] app\infrastructure\task_repository.py:44 — controle with em TaskRepository.create
01604. [x] app\infrastructure\task_repository.py:45 — atribuição: TaskRepository.create ← cur
01605. [x] app\infrastructure\task_repository.py:54 — return em TaskRepository.create
01606. [x] app\infrastructure\task_repository.py:56 — definir/revisar FunctionDef: TaskRepository.get
01607. [x] app\infrastructure\task_repository.py:56 — revisar facet 'assinatura/args consistentes' em TaskRepository.get
01608. [x] app\infrastructure\task_repository.py:56 — revisar facet 'docstring em português' em TaskRepository.get
01609. [x] app\infrastructure\task_repository.py:56 — revisar facet 'nomenclatura clara (PEP8)' em TaskRepository.get
01610. [x] app\infrastructure\task_repository.py:56 — revisar facet 'type hints presentes' em TaskRepository.get
01611. [x] app\infrastructure\task_repository.py:56 — revisar facet 'tratamento de erros adequado' em TaskRepository.get
01612. [x] app\infrastructure\task_repository.py:56 — revisar facet 'sem comentários inline desnecessários' em TaskRepository.get
01613. [x] app\infrastructure\task_repository.py:56 — revisar facet 'não imprime side-effects na UI/IO' em TaskRepository.get
01614. [x] app\infrastructure\task_repository.py:56 — revisar facet 'thread-safety revisada' em TaskRepository.get
01615. [x] app\infrastructure\task_repository.py:56 — revisar facet 'performance (sem loops O(n^2))' em TaskRepository.get
01616. [x] app\infrastructure\task_repository.py:56 — revisar facet 'coberto por testes' em TaskRepository.get
01617. [x] app\infrastructure\task_repository.py:57 — atribuição: TaskRepository.get ← r
01618. [x] app\infrastructure\task_repository.py:58 — return em TaskRepository.get
01619. [x] app\infrastructure\task_repository.py:60 — definir/revisar FunctionDef: TaskRepository.next_pending
01620. [x] app\infrastructure\task_repository.py:60 — revisar facet 'assinatura/args consistentes' em TaskRepository.next_pending
01621. [x] app\infrastructure\task_repository.py:60 — revisar facet 'docstring em português' em TaskRepository.next_pending
01622. [x] app\infrastructure\task_repository.py:60 — revisar facet 'nomenclatura clara (PEP8)' em TaskRepository.next_pending
01623. [x] app\infrastructure\task_repository.py:60 — revisar facet 'type hints presentes' em TaskRepository.next_pending
01624. [x] app\infrastructure\task_repository.py:60 — revisar facet 'tratamento de erros adequado' em TaskRepository.next_pending
01625. [x] app\infrastructure\task_repository.py:60 — revisar facet 'sem comentários inline desnecessários' em TaskRepository.next_pending
01626. [x] app\infrastructure\task_repository.py:60 — revisar facet 'não imprime side-effects na UI/IO' em TaskRepository.next_pending
01627. [x] app\infrastructure\task_repository.py:60 — revisar facet 'thread-safety revisada' em TaskRepository.next_pending
01628. [x] app\infrastructure\task_repository.py:60 — revisar facet 'performance (sem loops O(n^2))' em TaskRepository.next_pending
01629. [x] app\infrastructure\task_repository.py:60 — revisar facet 'coberto por testes' em TaskRepository.next_pending
01630. [x] app\infrastructure\task_repository.py:61 — atribuição: TaskRepository.next_pending ← r
01631. [x] app\infrastructure\task_repository.py:65 — return em TaskRepository.next_pending
01632. [x] app\infrastructure\task_repository.py:67 — definir/revisar FunctionDef: TaskRepository.list_all
01633. [x] app\infrastructure\task_repository.py:67 — revisar facet 'assinatura/args consistentes' em TaskRepository.list_all
01634. [x] app\infrastructure\task_repository.py:67 — revisar facet 'docstring em português' em TaskRepository.list_all
01635. [x] app\infrastructure\task_repository.py:67 — revisar facet 'nomenclatura clara (PEP8)' em TaskRepository.list_all
01636. [x] app\infrastructure\task_repository.py:67 — revisar facet 'type hints presentes' em TaskRepository.list_all
01637. [x] app\infrastructure\task_repository.py:67 — revisar facet 'tratamento de erros adequado' em TaskRepository.list_all
01638. [x] app\infrastructure\task_repository.py:67 — revisar facet 'sem comentários inline desnecessários' em TaskRepository.list_all
01639. [x] app\infrastructure\task_repository.py:67 — revisar facet 'não imprime side-effects na UI/IO' em TaskRepository.list_all
01640. [x] app\infrastructure\task_repository.py:67 — revisar facet 'thread-safety revisada' em TaskRepository.list_all
01641. [x] app\infrastructure\task_repository.py:67 — revisar facet 'performance (sem loops O(n^2))' em TaskRepository.list_all
01642. [x] app\infrastructure\task_repository.py:67 — revisar facet 'coberto por testes' em TaskRepository.list_all
01643. [x] app\infrastructure\task_repository.py:68 — atribuição: TaskRepository.list_all ← rows
01644. [x] app\infrastructure\task_repository.py:71 — return em TaskRepository.list_all
01645. [x] app\infrastructure\task_repository.py:73 — definir/revisar FunctionDef: TaskRepository.update_progress
01646. [x] app\infrastructure\task_repository.py:73 — revisar facet 'assinatura/args consistentes' em TaskRepository.update_progress
01647. [x] app\infrastructure\task_repository.py:73 — revisar facet 'docstring em português' em TaskRepository.update_progress
01648. [x] app\infrastructure\task_repository.py:73 — revisar facet 'nomenclatura clara (PEP8)' em TaskRepository.update_progress
01649. [x] app\infrastructure\task_repository.py:73 — revisar facet 'type hints presentes' em TaskRepository.update_progress
01650. [x] app\infrastructure\task_repository.py:73 — revisar facet 'tratamento de erros adequado' em TaskRepository.update_progress
01651. [x] app\infrastructure\task_repository.py:73 — revisar facet 'sem comentários inline desnecessários' em TaskRepository.update_progress
01652. [x] app\infrastructure\task_repository.py:73 — revisar facet 'não imprime side-effects na UI/IO' em TaskRepository.update_progress
01653. [x] app\infrastructure\task_repository.py:73 — revisar facet 'thread-safety revisada' em TaskRepository.update_progress
01654. [x] app\infrastructure\task_repository.py:73 — revisar facet 'performance (sem loops O(n^2))' em TaskRepository.update_progress
01655. [x] app\infrastructure\task_repository.py:73 — revisar facet 'coberto por testes' em TaskRepository.update_progress
01656. [x] app\infrastructure\task_repository.py:74 — controle with em TaskRepository.update_progress
01657. [x] app\infrastructure\task_repository.py:85 — definir/revisar FunctionDef: TaskRepository.complete
01658. [x] app\infrastructure\task_repository.py:85 — revisar facet 'assinatura/args consistentes' em TaskRepository.complete
01659. [x] app\infrastructure\task_repository.py:85 — revisar facet 'docstring em português' em TaskRepository.complete
01660. [x] app\infrastructure\task_repository.py:85 — revisar facet 'nomenclatura clara (PEP8)' em TaskRepository.complete
01661. [x] app\infrastructure\task_repository.py:85 — revisar facet 'type hints presentes' em TaskRepository.complete
01662. [x] app\infrastructure\task_repository.py:85 — revisar facet 'tratamento de erros adequado' em TaskRepository.complete
01663. [x] app\infrastructure\task_repository.py:85 — revisar facet 'sem comentários inline desnecessários' em TaskRepository.complete
01664. [x] app\infrastructure\task_repository.py:85 — revisar facet 'não imprime side-effects na UI/IO' em TaskRepository.complete
01665. [x] app\infrastructure\task_repository.py:85 — revisar facet 'thread-safety revisada' em TaskRepository.complete
01666. [x] app\infrastructure\task_repository.py:85 — revisar facet 'performance (sem loops O(n^2))' em TaskRepository.complete
01667. [x] app\infrastructure\task_repository.py:85 — revisar facet 'coberto por testes' em TaskRepository.complete
01668. [x] app\infrastructure\task_repository.py:86 — controle with em TaskRepository.complete
01669. [x] app\infrastructure\task_repository.py:92 — definir/revisar FunctionDef: TaskRepository.fail
01670. [x] app\infrastructure\task_repository.py:92 — revisar facet 'assinatura/args consistentes' em TaskRepository.fail
01671. [x] app\infrastructure\task_repository.py:92 — revisar facet 'docstring em português' em TaskRepository.fail
01672. [x] app\infrastructure\task_repository.py:92 — revisar facet 'nomenclatura clara (PEP8)' em TaskRepository.fail
01673. [x] app\infrastructure\task_repository.py:92 — revisar facet 'type hints presentes' em TaskRepository.fail
01674. [x] app\infrastructure\task_repository.py:92 — revisar facet 'tratamento de erros adequado' em TaskRepository.fail
01675. [x] app\infrastructure\task_repository.py:92 — revisar facet 'sem comentários inline desnecessários' em TaskRepository.fail
01676. [x] app\infrastructure\task_repository.py:92 — revisar facet 'não imprime side-effects na UI/IO' em TaskRepository.fail
01677. [x] app\infrastructure\task_repository.py:92 — revisar facet 'thread-safety revisada' em TaskRepository.fail
01678. [x] app\infrastructure\task_repository.py:92 — revisar facet 'performance (sem loops O(n^2))' em TaskRepository.fail
01679. [x] app\infrastructure\task_repository.py:92 — revisar facet 'coberto por testes' em TaskRepository.fail
01680. [x] app\infrastructure\task_repository.py:93 — controle with em TaskRepository.fail
01681. [x] app\infrastructure\task_repository.py:99 — definir/revisar FunctionDef: TaskRepository.pause
01682. [x] app\infrastructure\task_repository.py:99 — revisar facet 'assinatura/args consistentes' em TaskRepository.pause
01683. [x] app\infrastructure\task_repository.py:99 — revisar facet 'docstring em português' em TaskRepository.pause
01684. [x] app\infrastructure\task_repository.py:99 — revisar facet 'nomenclatura clara (PEP8)' em TaskRepository.pause
01685. [x] app\infrastructure\task_repository.py:99 — revisar facet 'type hints presentes' em TaskRepository.pause
01686. [x] app\infrastructure\task_repository.py:99 — revisar facet 'tratamento de erros adequado' em TaskRepository.pause
01687. [x] app\infrastructure\task_repository.py:99 — revisar facet 'sem comentários inline desnecessários' em TaskRepository.pause
01688. [x] app\infrastructure\task_repository.py:99 — revisar facet 'não imprime side-effects na UI/IO' em TaskRepository.pause
01689. [x] app\infrastructure\task_repository.py:99 — revisar facet 'thread-safety revisada' em TaskRepository.pause
01690. [x] app\infrastructure\task_repository.py:99 — revisar facet 'performance (sem loops O(n^2))' em TaskRepository.pause
01691. [x] app\infrastructure\task_repository.py:99 — revisar facet 'coberto por testes' em TaskRepository.pause
01692. [x] app\infrastructure\task_repository.py:100 — controle with em TaskRepository.pause
01693. [x] app\infrastructure\task_repository.py:106 — definir/revisar FunctionDef: TaskRepository.resume
01694. [x] app\infrastructure\task_repository.py:106 — revisar facet 'assinatura/args consistentes' em TaskRepository.resume
01695. [x] app\infrastructure\task_repository.py:106 — revisar facet 'docstring em português' em TaskRepository.resume
01696. [x] app\infrastructure\task_repository.py:106 — revisar facet 'nomenclatura clara (PEP8)' em TaskRepository.resume
01697. [x] app\infrastructure\task_repository.py:106 — revisar facet 'type hints presentes' em TaskRepository.resume
01698. [x] app\infrastructure\task_repository.py:106 — revisar facet 'tratamento de erros adequado' em TaskRepository.resume
01699. [x] app\infrastructure\task_repository.py:106 — revisar facet 'sem comentários inline desnecessários' em TaskRepository.resume
01700. [x] app\infrastructure\task_repository.py:106 — revisar facet 'não imprime side-effects na UI/IO' em TaskRepository.resume
01701. [x] app\infrastructure\task_repository.py:106 — revisar facet 'thread-safety revisada' em TaskRepository.resume
01702. [x] app\infrastructure\task_repository.py:106 — revisar facet 'performance (sem loops O(n^2))' em TaskRepository.resume
01703. [x] app\infrastructure\task_repository.py:106 — revisar facet 'coberto por testes' em TaskRepository.resume
01704. [x] app\infrastructure\task_repository.py:107 — controle with em TaskRepository.resume
01705. [x] app\infrastructure\task_repository.py:113 — definir/revisar FunctionDef: TaskRepository.recover_interrupted
01706. [x] app\infrastructure\task_repository.py:113 — revisar facet 'assinatura/args consistentes' em TaskRepository.recover_interrupted
01707. [x] app\infrastructure\task_repository.py:113 — revisar facet 'docstring em português' em TaskRepository.recover_interrupted
01708. [x] app\infrastructure\task_repository.py:113 — revisar facet 'nomenclatura clara (PEP8)' em TaskRepository.recover_interrupted
01709. [x] app\infrastructure\task_repository.py:113 — revisar facet 'type hints presentes' em TaskRepository.recover_interrupted
01710. [x] app\infrastructure\task_repository.py:113 — revisar facet 'tratamento de erros adequado' em TaskRepository.recover_interrupted
01711. [x] app\infrastructure\task_repository.py:113 — revisar facet 'sem comentários inline desnecessários' em TaskRepository.recover_interrupted
01712. [x] app\infrastructure\task_repository.py:113 — revisar facet 'não imprime side-effects na UI/IO' em TaskRepository.recover_interrupted
01713. [x] app\infrastructure\task_repository.py:113 — revisar facet 'thread-safety revisada' em TaskRepository.recover_interrupted
01714. [x] app\infrastructure\task_repository.py:113 — revisar facet 'performance (sem loops O(n^2))' em TaskRepository.recover_interrupted
01715. [x] app\infrastructure\task_repository.py:113 — revisar facet 'coberto por testes' em TaskRepository.recover_interrupted
01716. [x] app\infrastructure\task_repository.py:115 — controle with em TaskRepository.recover_interrupted
01717. [x] app\infrastructure\task_repository.py:116 — atribuição: TaskRepository.recover_interrupted ← cur
01718. [x] app\infrastructure\task_repository.py:121 — return em TaskRepository.recover_interrupted
01719. [x] app\infrastructure\task_repository.py:124 — definir/revisar FunctionDef: TaskRepository._to_task
01720. [x] app\infrastructure\task_repository.py:124 — revisar facet 'assinatura/args consistentes' em TaskRepository._to_task
01721. [x] app\infrastructure\task_repository.py:124 — revisar facet 'docstring em português' em TaskRepository._to_task
01722. [x] app\infrastructure\task_repository.py:124 — revisar facet 'nomenclatura clara (PEP8)' em TaskRepository._to_task
01723. [x] app\infrastructure\task_repository.py:124 — revisar facet 'type hints presentes' em TaskRepository._to_task
01724. [x] app\infrastructure\task_repository.py:124 — revisar facet 'tratamento de erros adequado' em TaskRepository._to_task
01725. [x] app\infrastructure\task_repository.py:124 — revisar facet 'sem comentários inline desnecessários' em TaskRepository._to_task
01726. [x] app\infrastructure\task_repository.py:124 — revisar facet 'não imprime side-effects na UI/IO' em TaskRepository._to_task
01727. [x] app\infrastructure\task_repository.py:124 — revisar facet 'thread-safety revisada' em TaskRepository._to_task
01728. [x] app\infrastructure\task_repository.py:124 — revisar facet 'performance (sem loops O(n^2))' em TaskRepository._to_task
01729. [x] app\infrastructure\task_repository.py:124 — revisar facet 'coberto por testes' em TaskRepository._to_task
01730. [x] app\infrastructure\task_repository.py:125 — return em TaskRepository._to_task
01731. [x] app\infrastructure\task_repository.py:137 — definir/revisar FunctionDef: TaskRepository.close
01732. [x] app\infrastructure\task_repository.py:137 — revisar facet 'assinatura/args consistentes' em TaskRepository.close
01733. [x] app\infrastructure\task_repository.py:137 — revisar facet 'docstring em português' em TaskRepository.close
01734. [x] app\infrastructure\task_repository.py:137 — revisar facet 'nomenclatura clara (PEP8)' em TaskRepository.close
01735. [x] app\infrastructure\task_repository.py:137 — revisar facet 'type hints presentes' em TaskRepository.close
01736. [x] app\infrastructure\task_repository.py:137 — revisar facet 'tratamento de erros adequado' em TaskRepository.close
01737. [x] app\infrastructure\task_repository.py:137 — revisar facet 'sem comentários inline desnecessários' em TaskRepository.close
01738. [x] app\infrastructure\task_repository.py:137 — revisar facet 'não imprime side-effects na UI/IO' em TaskRepository.close
01739. [x] app\infrastructure\task_repository.py:137 — revisar facet 'thread-safety revisada' em TaskRepository.close
01740. [x] app\infrastructure\task_repository.py:137 — revisar facet 'performance (sem loops O(n^2))' em TaskRepository.close
01741. [x] app\infrastructure\task_repository.py:137 — revisar facet 'coberto por testes' em TaskRepository.close
01742. [x] Existência e estrutura do módulo: app\infrastructure\template_repository.py
01743. [x] app\infrastructure\template_repository.py:3 — import: __future__
01744. [x] app\infrastructure\template_repository.py:5 — import: hashlib
01745. [x] app\infrastructure\template_repository.py:6 — import: sqlite3
01746. [x] app\infrastructure\template_repository.py:7 — import: datetime
01747. [x] app\infrastructure\template_repository.py:8 — import: pathlib
01748. [x] app\infrastructure\template_repository.py:9 — import: typing
01749. [x] app\infrastructure\template_repository.py:12 — definir/revisar ClassDef: TemplateRepository
01750. [x] app\infrastructure\template_repository.py:13 — definir/revisar FunctionDef: TemplateRepository.__init__
01751. [x] app\infrastructure\template_repository.py:13 — revisar facet 'assinatura/args consistentes' em TemplateRepository.__init__
01752. [x] app\infrastructure\template_repository.py:13 — revisar facet 'docstring em português' em TemplateRepository.__init__
01753. [x] app\infrastructure\template_repository.py:13 — revisar facet 'nomenclatura clara (PEP8)' em TemplateRepository.__init__
01754. [x] app\infrastructure\template_repository.py:13 — revisar facet 'type hints presentes' em TemplateRepository.__init__
01755. [x] app\infrastructure\template_repository.py:13 — revisar facet 'tratamento de erros adequado' em TemplateRepository.__init__
01756. [x] app\infrastructure\template_repository.py:13 — revisar facet 'sem comentários inline desnecessários' em TemplateRepository.__init__
01757. [x] app\infrastructure\template_repository.py:13 — revisar facet 'não imprime side-effects na UI/IO' em TemplateRepository.__init__
01758. [x] app\infrastructure\template_repository.py:13 — revisar facet 'thread-safety revisada' em TemplateRepository.__init__
01759. [x] app\infrastructure\template_repository.py:13 — revisar facet 'performance (sem loops O(n^2))' em TemplateRepository.__init__
01760. [x] app\infrastructure\template_repository.py:13 — revisar facet 'coberto por testes' em TemplateRepository.__init__
01761. [x] app\infrastructure\template_repository.py:14 — controle if em TemplateRepository.__init__
01762. [x] app\infrastructure\template_repository.py:16 — atribuição: TemplateRepository.__init__ ← ?
01763. [x] app\infrastructure\template_repository.py:17 — atribuição: TemplateRepository.__init__ ← ?
01764. [x] app\infrastructure\template_repository.py:20 — definir/revisar FunctionDef: TemplateRepository._create_schema
01765. [x] app\infrastructure\template_repository.py:20 — revisar facet 'assinatura/args consistentes' em TemplateRepository._create_schema
01766. [x] app\infrastructure\template_repository.py:20 — revisar facet 'docstring em português' em TemplateRepository._create_schema
01767. [x] app\infrastructure\template_repository.py:20 — revisar facet 'nomenclatura clara (PEP8)' em TemplateRepository._create_schema
01768. [x] app\infrastructure\template_repository.py:20 — revisar facet 'type hints presentes' em TemplateRepository._create_schema
01769. [x] app\infrastructure\template_repository.py:20 — revisar facet 'tratamento de erros adequado' em TemplateRepository._create_schema
01770. [x] app\infrastructure\template_repository.py:20 — revisar facet 'sem comentários inline desnecessários' em TemplateRepository._create_schema
01771. [x] app\infrastructure\template_repository.py:20 — revisar facet 'não imprime side-effects na UI/IO' em TemplateRepository._create_schema
01772. [x] app\infrastructure\template_repository.py:20 — revisar facet 'thread-safety revisada' em TemplateRepository._create_schema
01773. [x] app\infrastructure\template_repository.py:20 — revisar facet 'performance (sem loops O(n^2))' em TemplateRepository._create_schema
01774. [x] app\infrastructure\template_repository.py:20 — revisar facet 'coberto por testes' em TemplateRepository._create_schema
01775. [x] app\infrastructure\template_repository.py:21 — controle with em TemplateRepository._create_schema
01776. [x] app\infrastructure\template_repository.py:50 — definir/revisar FunctionDef: TemplateRepository.create_template
01777. [x] app\infrastructure\template_repository.py:50 — revisar facet 'assinatura/args consistentes' em TemplateRepository.create_template
01778. [x] app\infrastructure\template_repository.py:50 — revisar facet 'docstring em português' em TemplateRepository.create_template
01779. [x] app\infrastructure\template_repository.py:50 — revisar facet 'nomenclatura clara (PEP8)' em TemplateRepository.create_template
01780. [x] app\infrastructure\template_repository.py:50 — revisar facet 'type hints presentes' em TemplateRepository.create_template
01781. [x] app\infrastructure\template_repository.py:50 — revisar facet 'tratamento de erros adequado' em TemplateRepository.create_template
01782. [x] app\infrastructure\template_repository.py:50 — revisar facet 'sem comentários inline desnecessários' em TemplateRepository.create_template
01783. [x] app\infrastructure\template_repository.py:50 — revisar facet 'não imprime side-effects na UI/IO' em TemplateRepository.create_template
01784. [x] app\infrastructure\template_repository.py:50 — revisar facet 'thread-safety revisada' em TemplateRepository.create_template
01785. [x] app\infrastructure\template_repository.py:50 — revisar facet 'performance (sem loops O(n^2))' em TemplateRepository.create_template
01786. [x] app\infrastructure\template_repository.py:50 — revisar facet 'coberto por testes' em TemplateRepository.create_template
01787. [x] app\infrastructure\template_repository.py:51 — atribuição: TemplateRepository.create_template ← now
01788. [x] app\infrastructure\template_repository.py:52 — controle with em TemplateRepository.create_template
01789. [x] app\infrastructure\template_repository.py:53 — atribuição: TemplateRepository.create_template ← cur
01790. [x] app\infrastructure\template_repository.py:58 — return em TemplateRepository.create_template
01791. [x] app\infrastructure\template_repository.py:60 — definir/revisar FunctionDef: TemplateRepository.list_templates
01792. [x] app\infrastructure\template_repository.py:60 — revisar facet 'assinatura/args consistentes' em TemplateRepository.list_templates
01793. [x] app\infrastructure\template_repository.py:60 — revisar facet 'docstring em português' em TemplateRepository.list_templates
01794. [x] app\infrastructure\template_repository.py:60 — revisar facet 'nomenclatura clara (PEP8)' em TemplateRepository.list_templates
01795. [x] app\infrastructure\template_repository.py:60 — revisar facet 'type hints presentes' em TemplateRepository.list_templates
01796. [x] app\infrastructure\template_repository.py:60 — revisar facet 'tratamento de erros adequado' em TemplateRepository.list_templates
01797. [x] app\infrastructure\template_repository.py:60 — revisar facet 'sem comentários inline desnecessários' em TemplateRepository.list_templates
01798. [x] app\infrastructure\template_repository.py:60 — revisar facet 'não imprime side-effects na UI/IO' em TemplateRepository.list_templates
01799. [x] app\infrastructure\template_repository.py:60 — revisar facet 'thread-safety revisada' em TemplateRepository.list_templates
01800. [x] app\infrastructure\template_repository.py:60 — revisar facet 'performance (sem loops O(n^2))' em TemplateRepository.list_templates
01801. [x] app\infrastructure\template_repository.py:60 — revisar facet 'coberto por testes' em TemplateRepository.list_templates
01802. [x] app\infrastructure\template_repository.py:61 — atribuição: TemplateRepository.list_templates ← rows
01803. [x] app\infrastructure\template_repository.py:69 — return em TemplateRepository.list_templates
01804. [x] app\infrastructure\template_repository.py:71 — definir/revisar FunctionDef: TemplateRepository.save_version
01805. [x] app\infrastructure\template_repository.py:71 — revisar facet 'assinatura/args consistentes' em TemplateRepository.save_version
01806. [x] app\infrastructure\template_repository.py:71 — revisar facet 'docstring em português' em TemplateRepository.save_version
01807. [x] app\infrastructure\template_repository.py:71 — revisar facet 'nomenclatura clara (PEP8)' em TemplateRepository.save_version
01808. [x] app\infrastructure\template_repository.py:71 — revisar facet 'type hints presentes' em TemplateRepository.save_version
01809. [x] app\infrastructure\template_repository.py:71 — revisar facet 'tratamento de erros adequado' em TemplateRepository.save_version
01810. [x] app\infrastructure\template_repository.py:71 — revisar facet 'sem comentários inline desnecessários' em TemplateRepository.save_version
01811. [x] app\infrastructure\template_repository.py:71 — revisar facet 'não imprime side-effects na UI/IO' em TemplateRepository.save_version
01812. [x] app\infrastructure\template_repository.py:71 — revisar facet 'thread-safety revisada' em TemplateRepository.save_version
01813. [x] app\infrastructure\template_repository.py:71 — revisar facet 'performance (sem loops O(n^2))' em TemplateRepository.save_version
01814. [x] app\infrastructure\template_repository.py:71 — revisar facet 'coberto por testes' em TemplateRepository.save_version
01815. [x] app\infrastructure\template_repository.py:78 — atribuição: TemplateRepository.save_version ← chash
01816. [x] app\infrastructure\template_repository.py:80 — atribuição: TemplateRepository.save_version ← row
01817. [x] app\infrastructure\template_repository.py:85 — atribuição: TemplateRepository.save_version ← next_ver
01818. [x] app\infrastructure\template_repository.py:86 — atribuição: TemplateRepository.save_version ← now
01819. [x] app\infrastructure\template_repository.py:88 — controle with em TemplateRepository.save_version
01820. [x] app\infrastructure\template_repository.py:89 — atribuição: TemplateRepository.save_version ← cur
01821. [x] app\infrastructure\template_repository.py:97 — atribuição: TemplateRepository.save_version ← vid
01822. [x] app\infrastructure\template_repository.py:102 — return em TemplateRepository.save_version
01823. [x] app\infrastructure\template_repository.py:104 — definir/revisar FunctionDef: TemplateRepository.list_versions
01824. [x] app\infrastructure\template_repository.py:104 — revisar facet 'assinatura/args consistentes' em TemplateRepository.list_versions
01825. [x] app\infrastructure\template_repository.py:104 — revisar facet 'docstring em português' em TemplateRepository.list_versions
01826. [x] app\infrastructure\template_repository.py:104 — revisar facet 'nomenclatura clara (PEP8)' em TemplateRepository.list_versions
01827. [x] app\infrastructure\template_repository.py:104 — revisar facet 'type hints presentes' em TemplateRepository.list_versions
01828. [x] app\infrastructure\template_repository.py:104 — revisar facet 'tratamento de erros adequado' em TemplateRepository.list_versions
01829. [x] app\infrastructure\template_repository.py:104 — revisar facet 'sem comentários inline desnecessários' em TemplateRepository.list_versions
01830. [x] app\infrastructure\template_repository.py:104 — revisar facet 'não imprime side-effects na UI/IO' em TemplateRepository.list_versions
01831. [x] app\infrastructure\template_repository.py:104 — revisar facet 'thread-safety revisada' em TemplateRepository.list_versions
01832. [x] app\infrastructure\template_repository.py:104 — revisar facet 'performance (sem loops O(n^2))' em TemplateRepository.list_versions
01833. [x] app\infrastructure\template_repository.py:104 — revisar facet 'coberto por testes' em TemplateRepository.list_versions
01834. [x] app\infrastructure\template_repository.py:105 — atribuição: TemplateRepository.list_versions ← rows
01835. [x] app\infrastructure\template_repository.py:110 — return em TemplateRepository.list_versions
01836. [x] app\infrastructure\template_repository.py:112 — definir/revisar FunctionDef: TemplateRepository.get_version
01837. [x] app\infrastructure\template_repository.py:112 — revisar facet 'assinatura/args consistentes' em TemplateRepository.get_version
01838. [x] app\infrastructure\template_repository.py:112 — revisar facet 'docstring em português' em TemplateRepository.get_version
01839. [x] app\infrastructure\template_repository.py:112 — revisar facet 'nomenclatura clara (PEP8)' em TemplateRepository.get_version
01840. [x] app\infrastructure\template_repository.py:112 — revisar facet 'type hints presentes' em TemplateRepository.get_version
01841. [x] app\infrastructure\template_repository.py:112 — revisar facet 'tratamento de erros adequado' em TemplateRepository.get_version
01842. [x] app\infrastructure\template_repository.py:112 — revisar facet 'sem comentários inline desnecessários' em TemplateRepository.get_version
01843. [x] app\infrastructure\template_repository.py:112 — revisar facet 'não imprime side-effects na UI/IO' em TemplateRepository.get_version
01844. [x] app\infrastructure\template_repository.py:112 — revisar facet 'thread-safety revisada' em TemplateRepository.get_version
01845. [x] app\infrastructure\template_repository.py:112 — revisar facet 'performance (sem loops O(n^2))' em TemplateRepository.get_version
01846. [x] app\infrastructure\template_repository.py:112 — revisar facet 'coberto por testes' em TemplateRepository.get_version
01847. [x] app\infrastructure\template_repository.py:113 — atribuição: TemplateRepository.get_version ← r
01848. [x] app\infrastructure\template_repository.py:116 — return em TemplateRepository.get_version
01849. [x] app\infrastructure\template_repository.py:118 — definir/revisar FunctionDef: TemplateRepository.get_current
01850. [x] app\infrastructure\template_repository.py:118 — revisar facet 'assinatura/args consistentes' em TemplateRepository.get_current
01851. [x] app\infrastructure\template_repository.py:118 — revisar facet 'docstring em português' em TemplateRepository.get_current
01852. [x] app\infrastructure\template_repository.py:118 — revisar facet 'nomenclatura clara (PEP8)' em TemplateRepository.get_current
01853. [x] app\infrastructure\template_repository.py:118 — revisar facet 'type hints presentes' em TemplateRepository.get_current
01854. [x] app\infrastructure\template_repository.py:118 — revisar facet 'tratamento de erros adequado' em TemplateRepository.get_current
01855. [x] app\infrastructure\template_repository.py:118 — revisar facet 'sem comentários inline desnecessários' em TemplateRepository.get_current
01856. [x] app\infrastructure\template_repository.py:118 — revisar facet 'não imprime side-effects na UI/IO' em TemplateRepository.get_current
01857. [x] app\infrastructure\template_repository.py:118 — revisar facet 'thread-safety revisada' em TemplateRepository.get_current
01858. [x] app\infrastructure\template_repository.py:118 — revisar facet 'performance (sem loops O(n^2))' em TemplateRepository.get_current
01859. [x] app\infrastructure\template_repository.py:118 — revisar facet 'coberto por testes' em TemplateRepository.get_current
01860. [x] app\infrastructure\template_repository.py:119 — atribuição: TemplateRepository.get_current ← r
01861. [x] app\infrastructure\template_repository.py:128 — return em TemplateRepository.get_current
01862. [x] app\infrastructure\template_repository.py:130 — definir/revisar FunctionDef: TemplateRepository.close
01863. [x] app\infrastructure\template_repository.py:130 — revisar facet 'assinatura/args consistentes' em TemplateRepository.close
01864. [x] app\infrastructure\template_repository.py:130 — revisar facet 'docstring em português' em TemplateRepository.close
01865. [x] app\infrastructure\template_repository.py:130 — revisar facet 'nomenclatura clara (PEP8)' em TemplateRepository.close
01866. [x] app\infrastructure\template_repository.py:130 — revisar facet 'type hints presentes' em TemplateRepository.close
01867. [x] app\infrastructure\template_repository.py:130 — revisar facet 'tratamento de erros adequado' em TemplateRepository.close
01868. [x] app\infrastructure\template_repository.py:130 — revisar facet 'sem comentários inline desnecessários' em TemplateRepository.close
01869. [x] app\infrastructure\template_repository.py:130 — revisar facet 'não imprime side-effects na UI/IO' em TemplateRepository.close
01870. [x] app\infrastructure\template_repository.py:130 — revisar facet 'thread-safety revisada' em TemplateRepository.close
01871. [x] app\infrastructure\template_repository.py:130 — revisar facet 'performance (sem loops O(n^2))' em TemplateRepository.close
01872. [x] app\infrastructure\template_repository.py:130 — revisar facet 'coberto por testes' em TemplateRepository.close
01873. [x] Existência e estrutura do módulo: app\services\__init__.py
01874. [x] app\services\__init__.py:3 — import: app.services.log_service
01875. [x] app\services\__init__.py:4 — import: app.services.sampling_service
01876. [x] app\services\__init__.py:6 — atribuição:  ← __all__
01877. [x] Existência e estrutura do módulo: app\services\batch_comparison_service.py
01878. [x] app\services\batch_comparison_service.py:3 — import: __future__
01879. [x] app\services\batch_comparison_service.py:5 — import: typing
01880. [x] app\services\batch_comparison_service.py:7 — import: numpy
01881. [x] app\services\batch_comparison_service.py:9 — import: app.domain.batch_comparison
01882. [x] app\services\batch_comparison_service.py:13 — import: app.infrastructure.experiment_repository
01883. [x] app\services\batch_comparison_service.py:16 — definir/revisar ClassDef: BatchComparisonService
01884. [x] app\services\batch_comparison_service.py:17 — definir/revisar FunctionDef: BatchComparisonService.__init__
01885. [x] app\services\batch_comparison_service.py:17 — revisar facet 'assinatura/args consistentes' em BatchComparisonService.__init__
01886. [x] app\services\batch_comparison_service.py:17 — revisar facet 'docstring em português' em BatchComparisonService.__init__
01887. [x] app\services\batch_comparison_service.py:17 — revisar facet 'nomenclatura clara (PEP8)' em BatchComparisonService.__init__
01888. [x] app\services\batch_comparison_service.py:17 — revisar facet 'type hints presentes' em BatchComparisonService.__init__
01889. [x] app\services\batch_comparison_service.py:17 — revisar facet 'tratamento de erros adequado' em BatchComparisonService.__init__
01890. [x] app\services\batch_comparison_service.py:17 — revisar facet 'sem comentários inline desnecessários' em BatchComparisonService.__init__
01891. [x] app\services\batch_comparison_service.py:17 — revisar facet 'não imprime side-effects na UI/IO' em BatchComparisonService.__init__
01892. [x] app\services\batch_comparison_service.py:17 — revisar facet 'thread-safety revisada' em BatchComparisonService.__init__
01893. [x] app\services\batch_comparison_service.py:17 — revisar facet 'performance (sem loops O(n^2))' em BatchComparisonService.__init__
01894. [x] app\services\batch_comparison_service.py:17 — revisar facet 'coberto por testes' em BatchComparisonService.__init__
01895. [x] app\services\batch_comparison_service.py:18 — atribuição: BatchComparisonService.__init__ ← ?
01896. [x] app\services\batch_comparison_service.py:20 — definir/revisar FunctionDef: BatchComparisonService.compare
01897. [x] app\services\batch_comparison_service.py:20 — revisar facet 'assinatura/args consistentes' em BatchComparisonService.compare
01898. [x] app\services\batch_comparison_service.py:20 — revisar facet 'docstring em português' em BatchComparisonService.compare
01899. [x] app\services\batch_comparison_service.py:20 — revisar facet 'nomenclatura clara (PEP8)' em BatchComparisonService.compare
01900. [x] app\services\batch_comparison_service.py:20 — revisar facet 'type hints presentes' em BatchComparisonService.compare
01901. [x] app\services\batch_comparison_service.py:20 — revisar facet 'tratamento de erros adequado' em BatchComparisonService.compare
01902. [x] app\services\batch_comparison_service.py:20 — revisar facet 'sem comentários inline desnecessários' em BatchComparisonService.compare
01903. [x] app\services\batch_comparison_service.py:20 — revisar facet 'não imprime side-effects na UI/IO' em BatchComparisonService.compare
01904. [x] app\services\batch_comparison_service.py:20 — revisar facet 'thread-safety revisada' em BatchComparisonService.compare
01905. [x] app\services\batch_comparison_service.py:20 — revisar facet 'performance (sem loops O(n^2))' em BatchComparisonService.compare
01906. [x] app\services\batch_comparison_service.py:20 — revisar facet 'coberto por testes' em BatchComparisonService.compare
01907. [x] app\services\batch_comparison_service.py:21 — atribuição: BatchComparisonService.compare ← values_a
01908. [x] app\services\batch_comparison_service.py:22 — atribuição: BatchComparisonService.compare ← values_b
01909. [x] app\services\batch_comparison_service.py:24 — atribuição: BatchComparisonService.compare ← all_vars
01910. [x] app\services\batch_comparison_service.py:25 — atribuição: BatchComparisonService.compare ← variables
01911. [x] app\services\batch_comparison_service.py:30 — return em BatchComparisonService.compare
01912. [x] app\services\batch_comparison_service.py:38 — definir/revisar FunctionDef: BatchComparisonService._count
01913. [x] app\services\batch_comparison_service.py:38 — revisar facet 'assinatura/args consistentes' em BatchComparisonService._count
01914. [x] app\services\batch_comparison_service.py:38 — revisar facet 'docstring em português' em BatchComparisonService._count
01915. [x] app\services\batch_comparison_service.py:38 — revisar facet 'nomenclatura clara (PEP8)' em BatchComparisonService._count
01916. [x] app\services\batch_comparison_service.py:38 — revisar facet 'type hints presentes' em BatchComparisonService._count
01917. [x] app\services\batch_comparison_service.py:38 — revisar facet 'tratamento de erros adequado' em BatchComparisonService._count
01918. [x] app\services\batch_comparison_service.py:38 — revisar facet 'sem comentários inline desnecessários' em BatchComparisonService._count
01919. [x] app\services\batch_comparison_service.py:38 — revisar facet 'não imprime side-effects na UI/IO' em BatchComparisonService._count
01920. [x] app\services\batch_comparison_service.py:38 — revisar facet 'thread-safety revisada' em BatchComparisonService._count
01921. [x] app\services\batch_comparison_service.py:38 — revisar facet 'performance (sem loops O(n^2))' em BatchComparisonService._count
01922. [x] app\services\batch_comparison_service.py:38 — revisar facet 'coberto por testes' em BatchComparisonService._count
01923. [x] app\services\batch_comparison_service.py:39 — atribuição: BatchComparisonService._count ← r
01924. [x] app\services\batch_comparison_service.py:42 — return em BatchComparisonService._count
01925. [x] app\services\batch_comparison_service.py:44 — definir/revisar FunctionDef: BatchComparisonService._values_by_var
01926. [x] app\services\batch_comparison_service.py:44 — revisar facet 'assinatura/args consistentes' em BatchComparisonService._values_by_var
01927. [x] app\services\batch_comparison_service.py:44 — revisar facet 'docstring em português' em BatchComparisonService._values_by_var
01928. [x] app\services\batch_comparison_service.py:44 — revisar facet 'nomenclatura clara (PEP8)' em BatchComparisonService._values_by_var
01929. [x] app\services\batch_comparison_service.py:44 — revisar facet 'type hints presentes' em BatchComparisonService._values_by_var
01930. [x] app\services\batch_comparison_service.py:44 — revisar facet 'tratamento de erros adequado' em BatchComparisonService._values_by_var
01931. [x] app\services\batch_comparison_service.py:44 — revisar facet 'sem comentários inline desnecessários' em BatchComparisonService._values_by_var
01932. [x] app\services\batch_comparison_service.py:44 — revisar facet 'não imprime side-effects na UI/IO' em BatchComparisonService._values_by_var
01933. [x] app\services\batch_comparison_service.py:44 — revisar facet 'thread-safety revisada' em BatchComparisonService._values_by_var
01934. [x] app\services\batch_comparison_service.py:44 — revisar facet 'performance (sem loops O(n^2))' em BatchComparisonService._values_by_var
01935. [x] app\services\batch_comparison_service.py:44 — revisar facet 'coberto por testes' em BatchComparisonService._values_by_var
01936. [x] app\services\batch_comparison_service.py:45 — atribuição: BatchComparisonService._values_by_var ← rows
01937. [x] app\services\batch_comparison_service.py:56 — controle for em BatchComparisonService._values_by_var
01938. [x] app\services\batch_comparison_service.py:58 — return em BatchComparisonService._values_by_var
01939. [x] app\services\batch_comparison_service.py:61 — definir/revisar FunctionDef: BatchComparisonService._safe_mean
01940. [x] app\services\batch_comparison_service.py:61 — revisar facet 'assinatura/args consistentes' em BatchComparisonService._safe_mean
01941. [x] app\services\batch_comparison_service.py:61 — revisar facet 'docstring em português' em BatchComparisonService._safe_mean
01942. [x] app\services\batch_comparison_service.py:61 — revisar facet 'nomenclatura clara (PEP8)' em BatchComparisonService._safe_mean
01943. [x] app\services\batch_comparison_service.py:61 — revisar facet 'type hints presentes' em BatchComparisonService._safe_mean
01944. [x] app\services\batch_comparison_service.py:61 — revisar facet 'tratamento de erros adequado' em BatchComparisonService._safe_mean
01945. [x] app\services\batch_comparison_service.py:61 — revisar facet 'sem comentários inline desnecessários' em BatchComparisonService._safe_mean
01946. [x] app\services\batch_comparison_service.py:61 — revisar facet 'não imprime side-effects na UI/IO' em BatchComparisonService._safe_mean
01947. [x] app\services\batch_comparison_service.py:61 — revisar facet 'thread-safety revisada' em BatchComparisonService._safe_mean
01948. [x] app\services\batch_comparison_service.py:61 — revisar facet 'performance (sem loops O(n^2))' em BatchComparisonService._safe_mean
01949. [x] app\services\batch_comparison_service.py:61 — revisar facet 'coberto por testes' em BatchComparisonService._safe_mean
01950. [x] app\services\batch_comparison_service.py:62 — return em BatchComparisonService._safe_mean
01951. [x] app\services\batch_comparison_service.py:65 — definir/revisar FunctionDef: BatchComparisonService._safe_q
01952. [x] app\services\batch_comparison_service.py:65 — revisar facet 'assinatura/args consistentes' em BatchComparisonService._safe_q
01953. [x] app\services\batch_comparison_service.py:65 — revisar facet 'docstring em português' em BatchComparisonService._safe_q
01954. [x] app\services\batch_comparison_service.py:65 — revisar facet 'nomenclatura clara (PEP8)' em BatchComparisonService._safe_q
01955. [x] app\services\batch_comparison_service.py:65 — revisar facet 'type hints presentes' em BatchComparisonService._safe_q
01956. [x] app\services\batch_comparison_service.py:65 — revisar facet 'tratamento de erros adequado' em BatchComparisonService._safe_q
01957. [x] app\services\batch_comparison_service.py:65 — revisar facet 'sem comentários inline desnecessários' em BatchComparisonService._safe_q
01958. [x] app\services\batch_comparison_service.py:65 — revisar facet 'não imprime side-effects na UI/IO' em BatchComparisonService._safe_q
01959. [x] app\services\batch_comparison_service.py:65 — revisar facet 'thread-safety revisada' em BatchComparisonService._safe_q
01960. [x] app\services\batch_comparison_service.py:65 — revisar facet 'performance (sem loops O(n^2))' em BatchComparisonService._safe_q
01961. [x] app\services\batch_comparison_service.py:65 — revisar facet 'coberto por testes' em BatchComparisonService._safe_q
01962. [x] app\services\batch_comparison_service.py:66 — return em BatchComparisonService._safe_q
01963. [x] app\services\batch_comparison_service.py:68 — definir/revisar FunctionDef: BatchComparisonService._compute
01964. [x] app\services\batch_comparison_service.py:68 — revisar facet 'assinatura/args consistentes' em BatchComparisonService._compute
01965. [x] app\services\batch_comparison_service.py:68 — revisar facet 'docstring em português' em BatchComparisonService._compute
01966. [x] app\services\batch_comparison_service.py:68 — revisar facet 'nomenclatura clara (PEP8)' em BatchComparisonService._compute
01967. [x] app\services\batch_comparison_service.py:68 — revisar facet 'type hints presentes' em BatchComparisonService._compute
01968. [x] app\services\batch_comparison_service.py:68 — revisar facet 'tratamento de erros adequado' em BatchComparisonService._compute
01969. [x] app\services\batch_comparison_service.py:68 — revisar facet 'sem comentários inline desnecessários' em BatchComparisonService._compute
01970. [x] app\services\batch_comparison_service.py:68 — revisar facet 'não imprime side-effects na UI/IO' em BatchComparisonService._compute
01971. [x] app\services\batch_comparison_service.py:68 — revisar facet 'thread-safety revisada' em BatchComparisonService._compute
01972. [x] app\services\batch_comparison_service.py:68 — revisar facet 'performance (sem loops O(n^2))' em BatchComparisonService._compute
01973. [x] app\services\batch_comparison_service.py:68 — revisar facet 'coberto por testes' em BatchComparisonService._compute
01974. [x] app\services\batch_comparison_service.py:69 — atribuição: BatchComparisonService._compute ← mean_a
01975. [x] app\services\batch_comparison_service.py:70 — atribuição: BatchComparisonService._compute ← mean_b
01976. [x] app\services\batch_comparison_service.py:72 — atribuição: BatchComparisonService._compute ← delta
01977. [x] app\services\batch_comparison_service.py:73 — controle if em BatchComparisonService._compute
01978. [x] app\services\batch_comparison_service.py:74 — atribuição: BatchComparisonService._compute ← delta_pct
01979. [x] app\services\batch_comparison_service.py:76 — atribuição: BatchComparisonService._compute ← delta_pct
01980. [x] app\services\batch_comparison_service.py:78 — return em BatchComparisonService._compute
01981. [x] Existência e estrutura do módulo: app\services\batch_export_service.py
01982. [x] app\services\batch_export_service.py:3 — import: __future__
01983. [x] app\services\batch_export_service.py:5 — import: csv
01984. [x] app\services\batch_export_service.py:6 — import: json
01985. [x] app\services\batch_export_service.py:7 — import: dataclasses
01986. [x] app\services\batch_export_service.py:8 — import: datetime
01987. [x] app\services\batch_export_service.py:9 — import: pathlib
01988. [x] app\services\batch_export_service.py:10 — import: typing
01989. [x] app\services\batch_export_service.py:12 — import: app.core.parsing
01990. [x] app\services\batch_export_service.py:13 — import: app.infrastructure.experiment_repository
01991. [x] app\services\batch_export_service.py:14 — import: app.infrastructure.template_repository
01992. [x] app\services\batch_export_service.py:18 — definir/revisar ClassDef: BatchExportManifest
01993. [x] app\services\batch_export_service.py:29 — definir/revisar ClassDef: BatchExportService
01994. [x] app\services\batch_export_service.py:30 — definir/revisar FunctionDef: BatchExportService.__init__
01995. [x] app\services\batch_export_service.py:30 — revisar facet 'assinatura/args consistentes' em BatchExportService.__init__
01996. [x] app\services\batch_export_service.py:30 — revisar facet 'docstring em português' em BatchExportService.__init__
01997. [x] app\services\batch_export_service.py:30 — revisar facet 'nomenclatura clara (PEP8)' em BatchExportService.__init__
01998. [x] app\services\batch_export_service.py:30 — revisar facet 'type hints presentes' em BatchExportService.__init__
01999. [x] app\services\batch_export_service.py:30 — revisar facet 'tratamento de erros adequado' em BatchExportService.__init__
02000. [x] app\services\batch_export_service.py:30 — revisar facet 'sem comentários inline desnecessários' em BatchExportService.__init__
02001. [x] app\services\batch_export_service.py:30 — revisar facet 'não imprime side-effects na UI/IO' em BatchExportService.__init__
02002. [x] app\services\batch_export_service.py:30 — revisar facet 'thread-safety revisada' em BatchExportService.__init__
02003. [x] app\services\batch_export_service.py:30 — revisar facet 'performance (sem loops O(n^2))' em BatchExportService.__init__
02004. [x] app\services\batch_export_service.py:30 — revisar facet 'coberto por testes' em BatchExportService.__init__
02005. [x] app\services\batch_export_service.py:36 — atribuição: BatchExportService.__init__ ← ?
02006. [x] app\services\batch_export_service.py:37 — atribuição: BatchExportService.__init__ ← ?
02007. [x] app\services\batch_export_service.py:38 — atribuição: BatchExportService.__init__ ← ?
02008. [x] app\services\batch_export_service.py:41 — definir/revisar FunctionDef: BatchExportService._default_render
02009. [x] app\services\batch_export_service.py:41 — revisar facet 'assinatura/args consistentes' em BatchExportService._default_render
02010. [x] app\services\batch_export_service.py:41 — revisar facet 'docstring em português' em BatchExportService._default_render
02011. [x] app\services\batch_export_service.py:41 — revisar facet 'nomenclatura clara (PEP8)' em BatchExportService._default_render
02012. [x] app\services\batch_export_service.py:41 — revisar facet 'type hints presentes' em BatchExportService._default_render
02013. [x] app\services\batch_export_service.py:41 — revisar facet 'tratamento de erros adequado' em BatchExportService._default_render
02014. [x] app\services\batch_export_service.py:41 — revisar facet 'sem comentários inline desnecessários' em BatchExportService._default_render
02015. [x] app\services\batch_export_service.py:41 — revisar facet 'não imprime side-effects na UI/IO' em BatchExportService._default_render
02016. [x] app\services\batch_export_service.py:41 — revisar facet 'thread-safety revisada' em BatchExportService._default_render
02017. [x] app\services\batch_export_service.py:41 — revisar facet 'performance (sem loops O(n^2))' em BatchExportService._default_render
02018. [x] app\services\batch_export_service.py:41 — revisar facet 'coberto por testes' em BatchExportService._default_render
02019. [x] app\services\batch_export_service.py:42 — return em BatchExportService._default_render
02020. [x] app\services\batch_export_service.py:44 — definir/revisar FunctionDef: BatchExportService.export
02021. [x] app\services\batch_export_service.py:44 — revisar facet 'assinatura/args consistentes' em BatchExportService.export
02022. [x] app\services\batch_export_service.py:44 — revisar facet 'docstring em português' em BatchExportService.export
02023. [x] app\services\batch_export_service.py:44 — revisar facet 'nomenclatura clara (PEP8)' em BatchExportService.export
02024. [x] app\services\batch_export_service.py:44 — revisar facet 'type hints presentes' em BatchExportService.export
02025. [x] app\services\batch_export_service.py:44 — revisar facet 'tratamento de erros adequado' em BatchExportService.export
02026. [x] app\services\batch_export_service.py:44 — revisar facet 'sem comentários inline desnecessários' em BatchExportService.export
02027. [x] app\services\batch_export_service.py:44 — revisar facet 'não imprime side-effects na UI/IO' em BatchExportService.export
02028. [x] app\services\batch_export_service.py:44 — revisar facet 'thread-safety revisada' em BatchExportService.export
02029. [x] app\services\batch_export_service.py:44 — revisar facet 'performance (sem loops O(n^2))' em BatchExportService.export
02030. [x] app\services\batch_export_service.py:44 — revisar facet 'coberto por testes' em BatchExportService.export
02031. [x] app\services\batch_export_service.py:57 — atribuição: BatchExportService.export ← version
02032. [x] app\services\batch_export_service.py:58 — controle if em BatchExportService.export
02033. [x] app\services\batch_export_service.py:59 — raise em BatchExportService.export
02034. [x] app\services\batch_export_service.py:61 — atribuição: BatchExportService.export ← template_text
02035. [x] app\services\batch_export_service.py:62 — atribuição: BatchExportService.export ← template_id
02036. [x] app\services\batch_export_service.py:63 — atribuição: BatchExportService.export ← version_number
02037. [x] app\services\batch_export_service.py:64 — atribuição: BatchExportService.export ← template_hash
02038. [x] app\services\batch_export_service.py:66 — atribuição: BatchExportService.export ← var_ids
02039. [x] app\services\batch_export_service.py:67 — atribuição: BatchExportService.export ← total
02040. [x] app\services\batch_export_service.py:69 — controle if em BatchExportService.export
02041. [x] app\services\batch_export_service.py:70 — raise em BatchExportService.export
02042. [x] app\services\batch_export_service.py:72 — atribuição: BatchExportService.export ← remaining
02043. [x] app\services\batch_export_service.py:74 — atribuição: BatchExportService.export ← out_dir
02044. [x] app\services\batch_export_service.py:78 — atribuição: BatchExportService.export ← written
02045. [x] app\services\batch_export_service.py:79 — atribuição: BatchExportService.export ← page
02046. [x] app\services\batch_export_service.py:81 — controle while em BatchExportService.export
02047. [x] app\services\batch_export_service.py:82 — atribuição: BatchExportService.export ← rows
02048. [x] app\services\batch_export_service.py:83 — controle if em BatchExportService.export
02049. [x] app\services\batch_export_service.py:86 — controle for em BatchExportService.export
02050. [x] app\services\batch_export_service.py:87 — controle if em BatchExportService.export
02051. [x] app\services\batch_export_service.py:88 — raise em BatchExportService.export
02052. [x] app\services\batch_export_service.py:90 — atribuição: BatchExportService.export ← ext_id
02053. [x] app\services\batch_export_service.py:91 — controle if em BatchExportService.export
02054. [x] app\services\batch_export_service.py:94 — atribuição: BatchExportService.export ← text
02055. [x] app\services\batch_export_service.py:95 — atribuição: BatchExportService.export ← filename
02056. [x] app\services\batch_export_service.py:106 — controle if em BatchExportService.export
02057. [x] app\services\batch_export_service.py:109 — controle if em BatchExportService.export
02058. [x] app\services\batch_export_service.py:113 — controle if em BatchExportService.export
02059. [x] app\services\batch_export_service.py:116 — controle if em BatchExportService.export
02060. [x] app\services\batch_export_service.py:117 — atribuição: BatchExportService.export ← manifest_path
02061. [x] app\services\batch_export_service.py:118 — controle with em BatchExportService.export
02062. [x] app\services\batch_export_service.py:121 — atribuição: BatchExportService.export ← manifest_path
02063. [x] app\services\batch_export_service.py:142 — return em BatchExportService.export
02064. [x] Existência e estrutura do módulo: app\services\comparison_service.py
02065. [x] app\services\comparison_service.py:3 — import: __future__
02066. [x] app\services\comparison_service.py:5 — import: difflib
02067. [x] app\services\comparison_service.py:6 — import: dataclasses
02068. [x] app\services\comparison_service.py:7 — import: typing
02069. [x] app\services\comparison_service.py:9 — import: app.infrastructure.experiment_repository
02070. [x] app\services\comparison_service.py:13 — definir/revisar ClassDef: VariableDiff
02071. [x] app\services\comparison_service.py:22 — definir/revisar ClassDef: ComparisonResult
02072. [x] app\services\comparison_service.py:31 — definir/revisar ClassDef: ComparisonService
02073. [x] app\services\comparison_service.py:32 — definir/revisar FunctionDef: ComparisonService.__init__
02074. [x] app\services\comparison_service.py:32 — revisar facet 'assinatura/args consistentes' em ComparisonService.__init__
02075. [x] app\services\comparison_service.py:32 — revisar facet 'docstring em português' em ComparisonService.__init__
02076. [x] app\services\comparison_service.py:32 — revisar facet 'nomenclatura clara (PEP8)' em ComparisonService.__init__
02077. [x] app\services\comparison_service.py:32 — revisar facet 'type hints presentes' em ComparisonService.__init__
02078. [x] app\services\comparison_service.py:32 — revisar facet 'tratamento de erros adequado' em ComparisonService.__init__
02079. [x] app\services\comparison_service.py:32 — revisar facet 'sem comentários inline desnecessários' em ComparisonService.__init__
02080. [x] app\services\comparison_service.py:32 — revisar facet 'não imprime side-effects na UI/IO' em ComparisonService.__init__
02081. [x] app\services\comparison_service.py:32 — revisar facet 'thread-safety revisada' em ComparisonService.__init__
02082. [x] app\services\comparison_service.py:32 — revisar facet 'performance (sem loops O(n^2))' em ComparisonService.__init__
02083. [x] app\services\comparison_service.py:32 — revisar facet 'coberto por testes' em ComparisonService.__init__
02084. [x] app\services\comparison_service.py:33 — atribuição: ComparisonService.__init__ ← ?
02085. [x] app\services\comparison_service.py:35 — definir/revisar FunctionDef: ComparisonService.compare
02086. [x] app\services\comparison_service.py:35 — revisar facet 'assinatura/args consistentes' em ComparisonService.compare
02087. [x] app\services\comparison_service.py:35 — revisar facet 'docstring em português' em ComparisonService.compare
02088. [x] app\services\comparison_service.py:35 — revisar facet 'nomenclatura clara (PEP8)' em ComparisonService.compare
02089. [x] app\services\comparison_service.py:35 — revisar facet 'type hints presentes' em ComparisonService.compare
02090. [x] app\services\comparison_service.py:35 — revisar facet 'tratamento de erros adequado' em ComparisonService.compare
02091. [x] app\services\comparison_service.py:35 — revisar facet 'sem comentários inline desnecessários' em ComparisonService.compare
02092. [x] app\services\comparison_service.py:35 — revisar facet 'não imprime side-effects na UI/IO' em ComparisonService.compare
02093. [x] app\services\comparison_service.py:35 — revisar facet 'thread-safety revisada' em ComparisonService.compare
02094. [x] app\services\comparison_service.py:35 — revisar facet 'performance (sem loops O(n^2))' em ComparisonService.compare
02095. [x] app\services\comparison_service.py:35 — revisar facet 'coberto por testes' em ComparisonService.compare
02096. [x] app\services\comparison_service.py:42 — atribuição: ComparisonService.compare ← a
02097. [x] app\services\comparison_service.py:43 — atribuição: ComparisonService.compare ← b
02098. [x] app\services\comparison_service.py:45 — atribuição: ComparisonService.compare ← var_ids
02099. [x] app\services\comparison_service.py:47 — atribuição: ComparisonService.compare ← diffs
02100. [x] app\services\comparison_service.py:49 — atribuição: ComparisonService.compare ← dat_a
02101. [x] app\services\comparison_service.py:50 — controle if em ComparisonService.compare
02102. [x] app\services\comparison_service.py:51 — atribuição: ComparisonService.compare ← dat_a
02103. [x] app\services\comparison_service.py:52 — atribuição: ComparisonService.compare ← dat_b
02104. [x] app\services\comparison_service.py:53 — atribuição: ComparisonService.compare ← dat_diff
02105. [x] app\services\comparison_service.py:60 — return em ComparisonService.compare
02106. [x] app\services\comparison_service.py:63 — definir/revisar FunctionDef: ComparisonService._diff
02107. [x] app\services\comparison_service.py:63 — revisar facet 'assinatura/args consistentes' em ComparisonService._diff
02108. [x] app\services\comparison_service.py:63 — revisar facet 'docstring em português' em ComparisonService._diff
02109. [x] app\services\comparison_service.py:63 — revisar facet 'nomenclatura clara (PEP8)' em ComparisonService._diff
02110. [x] app\services\comparison_service.py:63 — revisar facet 'type hints presentes' em ComparisonService._diff
02111. [x] app\services\comparison_service.py:63 — revisar facet 'tratamento de erros adequado' em ComparisonService._diff
02112. [x] app\services\comparison_service.py:63 — revisar facet 'sem comentários inline desnecessários' em ComparisonService._diff
02113. [x] app\services\comparison_service.py:63 — revisar facet 'não imprime side-effects na UI/IO' em ComparisonService._diff
02114. [x] app\services\comparison_service.py:63 — revisar facet 'thread-safety revisada' em ComparisonService._diff
02115. [x] app\services\comparison_service.py:63 — revisar facet 'performance (sem loops O(n^2))' em ComparisonService._diff
02116. [x] app\services\comparison_service.py:63 — revisar facet 'coberto por testes' em ComparisonService._diff
02117. [x] app\services\comparison_service.py:64 — atribuição: ComparisonService._diff ← value_a
02118. [x] app\services\comparison_service.py:65 — atribuição: ComparisonService._diff ← value_b
02119. [x] app\services\comparison_service.py:66 — atribuição: ComparisonService._diff ← abs_diff
02120. [x] app\services\comparison_service.py:67 — atribuição: ComparisonService._diff ← rel_diff
02121. [x] app\services\comparison_service.py:68 — controle if em ComparisonService._diff
02122. [x] app\services\comparison_service.py:69 — atribuição: ComparisonService._diff ← abs_diff
02123. [x] app\services\comparison_service.py:70 — controle if em ComparisonService._diff
02124. [x] app\services\comparison_service.py:71 — atribuição: ComparisonService._diff ← rel_diff
02125. [x] app\services\comparison_service.py:72 — return em ComparisonService._diff
02126. [x] app\services\comparison_service.py:74 — definir/revisar FunctionDef: ComparisonService._fetch
02127. [x] app\services\comparison_service.py:74 — revisar facet 'assinatura/args consistentes' em ComparisonService._fetch
02128. [x] app\services\comparison_service.py:74 — revisar facet 'docstring em português' em ComparisonService._fetch
02129. [x] app\services\comparison_service.py:74 — revisar facet 'nomenclatura clara (PEP8)' em ComparisonService._fetch
02130. [x] app\services\comparison_service.py:74 — revisar facet 'type hints presentes' em ComparisonService._fetch
02131. [x] app\services\comparison_service.py:74 — revisar facet 'tratamento de erros adequado' em ComparisonService._fetch
02132. [x] app\services\comparison_service.py:74 — revisar facet 'sem comentários inline desnecessários' em ComparisonService._fetch
02133. [x] app\services\comparison_service.py:74 — revisar facet 'não imprime side-effects na UI/IO' em ComparisonService._fetch
02134. [x] app\services\comparison_service.py:74 — revisar facet 'thread-safety revisada' em ComparisonService._fetch
02135. [x] app\services\comparison_service.py:74 — revisar facet 'performance (sem loops O(n^2))' em ComparisonService._fetch
02136. [x] app\services\comparison_service.py:74 — revisar facet 'coberto por testes' em ComparisonService._fetch
02137. [x] app\services\comparison_service.py:75 — atribuição: ComparisonService._fetch ← values
02138. [x] app\services\comparison_service.py:76 — return em ComparisonService._fetch
02139. [x] Existência e estrutura do módulo: app\services\correlation_service.py
02140. [x] app\services\correlation_service.py:3 — import: __future__
02141. [x] app\services\correlation_service.py:5 — import: typing
02142. [x] app\services\correlation_service.py:7 — import: numpy
02143. [x] app\services\correlation_service.py:10 — definir/revisar ClassDef: CorrelationService
02144. [x] app\services\correlation_service.py:13 — definir/revisar FunctionDef: CorrelationService.identity
02145. [x] app\services\correlation_service.py:13 — revisar facet 'assinatura/args consistentes' em CorrelationService.identity
02146. [x] app\services\correlation_service.py:13 — revisar facet 'docstring em português' em CorrelationService.identity
02147. [x] app\services\correlation_service.py:13 — revisar facet 'nomenclatura clara (PEP8)' em CorrelationService.identity
02148. [x] app\services\correlation_service.py:13 — revisar facet 'type hints presentes' em CorrelationService.identity
02149. [x] app\services\correlation_service.py:13 — revisar facet 'tratamento de erros adequado' em CorrelationService.identity
02150. [x] app\services\correlation_service.py:13 — revisar facet 'sem comentários inline desnecessários' em CorrelationService.identity
02151. [x] app\services\correlation_service.py:13 — revisar facet 'não imprime side-effects na UI/IO' em CorrelationService.identity
02152. [x] app\services\correlation_service.py:13 — revisar facet 'thread-safety revisada' em CorrelationService.identity
02153. [x] app\services\correlation_service.py:13 — revisar facet 'performance (sem loops O(n^2))' em CorrelationService.identity
02154. [x] app\services\correlation_service.py:13 — revisar facet 'coberto por testes' em CorrelationService.identity
02155. [x] app\services\correlation_service.py:14 — return em CorrelationService.identity
02156. [x] app\services\correlation_service.py:16 — definir/revisar FunctionDef: CorrelationService.is_valid
02157. [x] app\services\correlation_service.py:16 — revisar facet 'assinatura/args consistentes' em CorrelationService.is_valid
02158. [x] app\services\correlation_service.py:16 — revisar facet 'docstring em português' em CorrelationService.is_valid
02159. [x] app\services\correlation_service.py:16 — revisar facet 'nomenclatura clara (PEP8)' em CorrelationService.is_valid
02160. [x] app\services\correlation_service.py:16 — revisar facet 'type hints presentes' em CorrelationService.is_valid
02161. [x] app\services\correlation_service.py:16 — revisar facet 'tratamento de erros adequado' em CorrelationService.is_valid
02162. [x] app\services\correlation_service.py:16 — revisar facet 'sem comentários inline desnecessários' em CorrelationService.is_valid
02163. [x] app\services\correlation_service.py:16 — revisar facet 'não imprime side-effects na UI/IO' em CorrelationService.is_valid
02164. [x] app\services\correlation_service.py:16 — revisar facet 'thread-safety revisada' em CorrelationService.is_valid
02165. [x] app\services\correlation_service.py:16 — revisar facet 'performance (sem loops O(n^2))' em CorrelationService.is_valid
02166. [x] app\services\correlation_service.py:16 — revisar facet 'coberto por testes' em CorrelationService.is_valid
02167. [x] app\services\correlation_service.py:17 — try em CorrelationService.is_valid
02168. [x] app\services\correlation_service.py:18 — atribuição: CorrelationService.is_valid ← m
02169. [x] app\services\correlation_service.py:20 — return em CorrelationService.is_valid
02170. [x] app\services\correlation_service.py:22 — controle if em CorrelationService.is_valid
02171. [x] app\services\correlation_service.py:23 — return em CorrelationService.is_valid
02172. [x] app\services\correlation_service.py:24 — controle if em CorrelationService.is_valid
02173. [x] app\services\correlation_service.py:25 — return em CorrelationService.is_valid
02174. [x] app\services\correlation_service.py:26 — controle if em CorrelationService.is_valid
02175. [x] app\services\correlation_service.py:27 — return em CorrelationService.is_valid
02176. [x] app\services\correlation_service.py:28 — controle if em CorrelationService.is_valid
02177. [x] app\services\correlation_service.py:29 — return em CorrelationService.is_valid
02178. [x] app\services\correlation_service.py:30 — atribuição: CorrelationService.is_valid ← eig
02179. [x] app\services\correlation_service.py:31 — controle if em CorrelationService.is_valid
02180. [x] app\services\correlation_service.py:32 — return em CorrelationService.is_valid
02181. [x] app\services\correlation_service.py:33 — return em CorrelationService.is_valid
02182. [x] app\services\correlation_service.py:35 — definir/revisar FunctionDef: CorrelationService.repair
02183. [x] app\services\correlation_service.py:35 — revisar facet 'assinatura/args consistentes' em CorrelationService.repair
02184. [x] app\services\correlation_service.py:35 — revisar facet 'docstring em português' em CorrelationService.repair
02185. [x] app\services\correlation_service.py:35 — revisar facet 'nomenclatura clara (PEP8)' em CorrelationService.repair
02186. [x] app\services\correlation_service.py:35 — revisar facet 'type hints presentes' em CorrelationService.repair
02187. [x] app\services\correlation_service.py:35 — revisar facet 'tratamento de erros adequado' em CorrelationService.repair
02188. [x] app\services\correlation_service.py:35 — revisar facet 'sem comentários inline desnecessários' em CorrelationService.repair
02189. [x] app\services\correlation_service.py:35 — revisar facet 'não imprime side-effects na UI/IO' em CorrelationService.repair
02190. [x] app\services\correlation_service.py:35 — revisar facet 'thread-safety revisada' em CorrelationService.repair
02191. [x] app\services\correlation_service.py:35 — revisar facet 'performance (sem loops O(n^2))' em CorrelationService.repair
02192. [x] app\services\correlation_service.py:35 — revisar facet 'coberto por testes' em CorrelationService.repair
02193. [x] app\services\correlation_service.py:37 — atribuição: CorrelationService.repair ← m
02194. [x] app\services\correlation_service.py:38 — atribuição: CorrelationService.repair ← m
02195. [x] app\services\correlation_service.py:41 — atribuição: CorrelationService.repair ← ?
02196. [x] app\services\correlation_service.py:42 — atribuição: CorrelationService.repair ← eig
02197. [x] app\services\correlation_service.py:43 — atribuição: CorrelationService.repair ← repaired
02198. [x] app\services\correlation_service.py:45 — atribuição: CorrelationService.repair ← d
02199. [x] app\services\correlation_service.py:46 — atribuição: CorrelationService.repair ← ?
02200. [x] app\services\correlation_service.py:47 — atribuição: CorrelationService.repair ← repaired
02201. [x] app\services\correlation_service.py:49 — atribuição: CorrelationService.repair ← repaired
02202. [x] app\services\correlation_service.py:50 — return em CorrelationService.repair
02203. [x] Existência e estrutura do módulo: app\services\log_service.py
02204. [x] app\services\log_service.py:3 — import: __future__
02205. [x] app\services\log_service.py:5 — import: typing
02206. [x] app\services\log_service.py:7 — import: app.domain.events
02207. [x] app\services\log_service.py:8 — import: app.infrastructure.async_log_repository
02208. [x] app\services\log_service.py:9 — import: app.infrastructure.event_bus
02209. [x] app\services\log_service.py:12 — definir/revisar ClassDef: LogService
02210. [x] app\services\log_service.py:15 — definir/revisar FunctionDef: LogService.__init__
02211. [x] app\services\log_service.py:15 — revisar facet 'assinatura/args consistentes' em LogService.__init__
02212. [x] app\services\log_service.py:15 — revisar facet 'docstring em português' em LogService.__init__
02213. [x] app\services\log_service.py:15 — revisar facet 'nomenclatura clara (PEP8)' em LogService.__init__
02214. [x] app\services\log_service.py:15 — revisar facet 'type hints presentes' em LogService.__init__
02215. [x] app\services\log_service.py:15 — revisar facet 'tratamento de erros adequado' em LogService.__init__
02216. [x] app\services\log_service.py:15 — revisar facet 'sem comentários inline desnecessários' em LogService.__init__
02217. [x] app\services\log_service.py:15 — revisar facet 'não imprime side-effects na UI/IO' em LogService.__init__
02218. [x] app\services\log_service.py:15 — revisar facet 'thread-safety revisada' em LogService.__init__
02219. [x] app\services\log_service.py:15 — revisar facet 'performance (sem loops O(n^2))' em LogService.__init__
02220. [x] app\services\log_service.py:15 — revisar facet 'coberto por testes' em LogService.__init__
02221. [x] app\services\log_service.py:20 — atribuição: LogService.__init__ ← ?
02222. [x] app\services\log_service.py:21 — atribuição: LogService.__init__ ← ?
02223. [x] app\services\log_service.py:23 — definir/revisar FunctionDef: LogService._emit
02224. [x] app\services\log_service.py:23 — revisar facet 'assinatura/args consistentes' em LogService._emit
02225. [x] app\services\log_service.py:23 — revisar facet 'docstring em português' em LogService._emit
02226. [x] app\services\log_service.py:23 — revisar facet 'nomenclatura clara (PEP8)' em LogService._emit
02227. [x] app\services\log_service.py:23 — revisar facet 'type hints presentes' em LogService._emit
02228. [x] app\services\log_service.py:23 — revisar facet 'tratamento de erros adequado' em LogService._emit
02229. [x] app\services\log_service.py:23 — revisar facet 'sem comentários inline desnecessários' em LogService._emit
02230. [x] app\services\log_service.py:23 — revisar facet 'não imprime side-effects na UI/IO' em LogService._emit
02231. [x] app\services\log_service.py:23 — revisar facet 'thread-safety revisada' em LogService._emit
02232. [x] app\services\log_service.py:23 — revisar facet 'performance (sem loops O(n^2))' em LogService._emit
02233. [x] app\services\log_service.py:23 — revisar facet 'coberto por testes' em LogService._emit
02234. [x] app\services\log_service.py:33 — controle if em LogService._emit
02235. [x] app\services\log_service.py:43 — controle if em LogService._emit
02236. [x] app\services\log_service.py:48 — definir/revisar FunctionDef: LogService.info
02237. [x] app\services\log_service.py:48 — revisar facet 'assinatura/args consistentes' em LogService.info
02238. [x] app\services\log_service.py:48 — revisar facet 'docstring em português' em LogService.info
02239. [x] app\services\log_service.py:48 — revisar facet 'nomenclatura clara (PEP8)' em LogService.info
02240. [x] app\services\log_service.py:48 — revisar facet 'type hints presentes' em LogService.info
02241. [x] app\services\log_service.py:48 — revisar facet 'tratamento de erros adequado' em LogService.info
02242. [x] app\services\log_service.py:48 — revisar facet 'sem comentários inline desnecessários' em LogService.info
02243. [x] app\services\log_service.py:48 — revisar facet 'não imprime side-effects na UI/IO' em LogService.info
02244. [x] app\services\log_service.py:48 — revisar facet 'thread-safety revisada' em LogService.info
02245. [x] app\services\log_service.py:48 — revisar facet 'performance (sem loops O(n^2))' em LogService.info
02246. [x] app\services\log_service.py:48 — revisar facet 'coberto por testes' em LogService.info
02247. [x] app\services\log_service.py:51 — definir/revisar FunctionDef: LogService.warning
02248. [x] app\services\log_service.py:51 — revisar facet 'assinatura/args consistentes' em LogService.warning
02249. [x] app\services\log_service.py:51 — revisar facet 'docstring em português' em LogService.warning
02250. [x] app\services\log_service.py:51 — revisar facet 'nomenclatura clara (PEP8)' em LogService.warning
02251. [x] app\services\log_service.py:51 — revisar facet 'type hints presentes' em LogService.warning
02252. [x] app\services\log_service.py:51 — revisar facet 'tratamento de erros adequado' em LogService.warning
02253. [x] app\services\log_service.py:51 — revisar facet 'sem comentários inline desnecessários' em LogService.warning
02254. [x] app\services\log_service.py:51 — revisar facet 'não imprime side-effects na UI/IO' em LogService.warning
02255. [x] app\services\log_service.py:51 — revisar facet 'thread-safety revisada' em LogService.warning
02256. [x] app\services\log_service.py:51 — revisar facet 'performance (sem loops O(n^2))' em LogService.warning
02257. [x] app\services\log_service.py:51 — revisar facet 'coberto por testes' em LogService.warning
02258. [x] app\services\log_service.py:54 — definir/revisar FunctionDef: LogService.error
02259. [x] app\services\log_service.py:54 — revisar facet 'assinatura/args consistentes' em LogService.error
02260. [x] app\services\log_service.py:54 — revisar facet 'docstring em português' em LogService.error
02261. [x] app\services\log_service.py:54 — revisar facet 'nomenclatura clara (PEP8)' em LogService.error
02262. [x] app\services\log_service.py:54 — revisar facet 'type hints presentes' em LogService.error
02263. [x] app\services\log_service.py:54 — revisar facet 'tratamento de erros adequado' em LogService.error
02264. [x] app\services\log_service.py:54 — revisar facet 'sem comentários inline desnecessários' em LogService.error
02265. [x] app\services\log_service.py:54 — revisar facet 'não imprime side-effects na UI/IO' em LogService.error
02266. [x] app\services\log_service.py:54 — revisar facet 'thread-safety revisada' em LogService.error
02267. [x] app\services\log_service.py:54 — revisar facet 'performance (sem loops O(n^2))' em LogService.error
02268. [x] app\services\log_service.py:54 — revisar facet 'coberto por testes' em LogService.error
02269. [x] app\services\log_service.py:57 — definir/revisar FunctionDef: LogService.usage
02270. [x] app\services\log_service.py:57 — revisar facet 'assinatura/args consistentes' em LogService.usage
02271. [x] app\services\log_service.py:57 — revisar facet 'docstring em português' em LogService.usage
02272. [x] app\services\log_service.py:57 — revisar facet 'nomenclatura clara (PEP8)' em LogService.usage
02273. [x] app\services\log_service.py:57 — revisar facet 'type hints presentes' em LogService.usage
02274. [x] app\services\log_service.py:57 — revisar facet 'tratamento de erros adequado' em LogService.usage
02275. [x] app\services\log_service.py:57 — revisar facet 'sem comentários inline desnecessários' em LogService.usage
02276. [x] app\services\log_service.py:57 — revisar facet 'não imprime side-effects na UI/IO' em LogService.usage
02277. [x] app\services\log_service.py:57 — revisar facet 'thread-safety revisada' em LogService.usage
02278. [x] app\services\log_service.py:57 — revisar facet 'performance (sem loops O(n^2))' em LogService.usage
02279. [x] app\services\log_service.py:57 — revisar facet 'coberto por testes' em LogService.usage
02280. [x] app\services\log_service.py:60 — definir/revisar FunctionDef: LogService.audit
02281. [x] app\services\log_service.py:60 — revisar facet 'assinatura/args consistentes' em LogService.audit
02282. [x] app\services\log_service.py:60 — revisar facet 'docstring em português' em LogService.audit
02283. [x] app\services\log_service.py:60 — revisar facet 'nomenclatura clara (PEP8)' em LogService.audit
02284. [x] app\services\log_service.py:60 — revisar facet 'type hints presentes' em LogService.audit
02285. [x] app\services\log_service.py:60 — revisar facet 'tratamento de erros adequado' em LogService.audit
02286. [x] app\services\log_service.py:60 — revisar facet 'sem comentários inline desnecessários' em LogService.audit
02287. [x] app\services\log_service.py:60 — revisar facet 'não imprime side-effects na UI/IO' em LogService.audit
02288. [x] app\services\log_service.py:60 — revisar facet 'thread-safety revisada' em LogService.audit
02289. [x] app\services\log_service.py:60 — revisar facet 'performance (sem loops O(n^2))' em LogService.audit
02290. [x] app\services\log_service.py:60 — revisar facet 'coberto por testes' em LogService.audit
02291. [x] Existência e estrutura do módulo: app\services\metrics_service.py
02292. [x] app\services\metrics_service.py:3 — import: __future__
02293. [x] app\services\metrics_service.py:5 — import: dataclasses
02294. [x] app\services\metrics_service.py:6 — import: datetime
02295. [x] app\services\metrics_service.py:7 — import: typing
02296. [x] app\services\metrics_service.py:9 — import: app.infrastructure.async_log_repository
02297. [x] app\services\metrics_service.py:10 — import: app.infrastructure.experiment_repository
02298. [x] app\services\metrics_service.py:14 — definir/revisar ClassDef: KpiSummary
02299. [x] app\services\metrics_service.py:24 — definir/revisar ClassDef: MetricsService
02300. [x] app\services\metrics_service.py:25 — definir/revisar FunctionDef: MetricsService.__init__
02301. [x] app\services\metrics_service.py:25 — revisar facet 'assinatura/args consistentes' em MetricsService.__init__
02302. [x] app\services\metrics_service.py:25 — revisar facet 'docstring em português' em MetricsService.__init__
02303. [x] app\services\metrics_service.py:25 — revisar facet 'nomenclatura clara (PEP8)' em MetricsService.__init__
02304. [x] app\services\metrics_service.py:25 — revisar facet 'type hints presentes' em MetricsService.__init__
02305. [x] app\services\metrics_service.py:25 — revisar facet 'tratamento de erros adequado' em MetricsService.__init__
02306. [x] app\services\metrics_service.py:25 — revisar facet 'sem comentários inline desnecessários' em MetricsService.__init__
02307. [x] app\services\metrics_service.py:25 — revisar facet 'não imprime side-effects na UI/IO' em MetricsService.__init__
02308. [x] app\services\metrics_service.py:25 — revisar facet 'thread-safety revisada' em MetricsService.__init__
02309. [x] app\services\metrics_service.py:25 — revisar facet 'performance (sem loops O(n^2))' em MetricsService.__init__
02310. [x] app\services\metrics_service.py:25 — revisar facet 'coberto por testes' em MetricsService.__init__
02311. [x] app\services\metrics_service.py:31 — atribuição: MetricsService.__init__ ← ?
02312. [x] app\services\metrics_service.py:32 — atribuição: MetricsService.__init__ ← ?
02313. [x] app\services\metrics_service.py:33 — atribuição: MetricsService.__init__ ← ?
02314. [x] app\services\metrics_service.py:35 — definir/revisar FunctionDef: MetricsService.summary
02315. [x] app\services\metrics_service.py:35 — revisar facet 'assinatura/args consistentes' em MetricsService.summary
02316. [x] app\services\metrics_service.py:35 — revisar facet 'docstring em português' em MetricsService.summary
02317. [x] app\services\metrics_service.py:35 — revisar facet 'nomenclatura clara (PEP8)' em MetricsService.summary
02318. [x] app\services\metrics_service.py:35 — revisar facet 'type hints presentes' em MetricsService.summary
02319. [x] app\services\metrics_service.py:35 — revisar facet 'tratamento de erros adequado' em MetricsService.summary
02320. [x] app\services\metrics_service.py:35 — revisar facet 'sem comentários inline desnecessários' em MetricsService.summary
02321. [x] app\services\metrics_service.py:35 — revisar facet 'não imprime side-effects na UI/IO' em MetricsService.summary
02322. [x] app\services\metrics_service.py:35 — revisar facet 'thread-safety revisada' em MetricsService.summary
02323. [x] app\services\metrics_service.py:35 — revisar facet 'performance (sem loops O(n^2))' em MetricsService.summary
02324. [x] app\services\metrics_service.py:35 — revisar facet 'coberto por testes' em MetricsService.summary
02325. [x] app\services\metrics_service.py:36 — controle if em MetricsService.summary
02326. [x] app\services\metrics_service.py:38 — atribuição: MetricsService.summary ← exp_conn
02327. [x] app\services\metrics_service.py:40 — atribuição: MetricsService.summary ← total_batches
02328. [x] app\services\metrics_service.py:41 — atribuição: MetricsService.summary ← total_experiments
02329. [x] app\services\metrics_service.py:42 — atribuição: MetricsService.summary ← total_templates
02330. [x] app\services\metrics_service.py:45 — atribuição: MetricsService.summary ← total_versions
02331. [x] app\services\metrics_service.py:48 — atribuição: MetricsService.summary ← total_logs
02332. [x] app\services\metrics_service.py:50 — atribuição: MetricsService.summary ← now
02333. [x] app\services\metrics_service.py:51 — atribuição: MetricsService.summary ← cutoff_24
02334. [x] app\services\metrics_service.py:52 — atribuição: MetricsService.summary ← cutoff_7d
02335. [x] app\services\metrics_service.py:54 — atribuição: MetricsService.summary ← logs_24h
02336. [x] app\services\metrics_service.py:55 — atribuição: MetricsService.summary ← logs_7d
02337. [x] app\services\metrics_service.py:57 — return em MetricsService.summary
02338. [x] app\services\metrics_service.py:62 — definir/revisar FunctionDef: MetricsService._log_count_since
02339. [x] app\services\metrics_service.py:62 — revisar facet 'assinatura/args consistentes' em MetricsService._log_count_since
02340. [x] app\services\metrics_service.py:62 — revisar facet 'docstring em português' em MetricsService._log_count_since
02341. [x] app\services\metrics_service.py:62 — revisar facet 'nomenclatura clara (PEP8)' em MetricsService._log_count_since
02342. [x] app\services\metrics_service.py:62 — revisar facet 'type hints presentes' em MetricsService._log_count_since
02343. [x] app\services\metrics_service.py:62 — revisar facet 'tratamento de erros adequado' em MetricsService._log_count_since
02344. [x] app\services\metrics_service.py:62 — revisar facet 'sem comentários inline desnecessários' em MetricsService._log_count_since
02345. [x] app\services\metrics_service.py:62 — revisar facet 'não imprime side-effects na UI/IO' em MetricsService._log_count_since
02346. [x] app\services\metrics_service.py:62 — revisar facet 'thread-safety revisada' em MetricsService._log_count_since
02347. [x] app\services\metrics_service.py:62 — revisar facet 'performance (sem loops O(n^2))' em MetricsService._log_count_since
02348. [x] app\services\metrics_service.py:62 — revisar facet 'coberto por testes' em MetricsService._log_count_since
02349. [x] app\services\metrics_service.py:63 — atribuição: MetricsService._log_count_since ← row
02350. [x] app\services\metrics_service.py:66 — return em MetricsService._log_count_since
02351. [x] app\services\metrics_service.py:68 — definir/revisar FunctionDef: MetricsService.experiments_per_batch
02352. [x] app\services\metrics_service.py:68 — revisar facet 'assinatura/args consistentes' em MetricsService.experiments_per_batch
02353. [x] app\services\metrics_service.py:68 — revisar facet 'docstring em português' em MetricsService.experiments_per_batch
02354. [x] app\services\metrics_service.py:68 — revisar facet 'nomenclatura clara (PEP8)' em MetricsService.experiments_per_batch
02355. [x] app\services\metrics_service.py:68 — revisar facet 'type hints presentes' em MetricsService.experiments_per_batch
02356. [x] app\services\metrics_service.py:68 — revisar facet 'tratamento de erros adequado' em MetricsService.experiments_per_batch
02357. [x] app\services\metrics_service.py:68 — revisar facet 'sem comentários inline desnecessários' em MetricsService.experiments_per_batch
02358. [x] app\services\metrics_service.py:68 — revisar facet 'não imprime side-effects na UI/IO' em MetricsService.experiments_per_batch
02359. [x] app\services\metrics_service.py:68 — revisar facet 'thread-safety revisada' em MetricsService.experiments_per_batch
02360. [x] app\services\metrics_service.py:68 — revisar facet 'performance (sem loops O(n^2))' em MetricsService.experiments_per_batch
02361. [x] app\services\metrics_service.py:68 — revisar facet 'coberto por testes' em MetricsService.experiments_per_batch
02362. [x] app\services\metrics_service.py:69 — atribuição: MetricsService.experiments_per_batch ← rows
02363. [x] app\services\metrics_service.py:80 — return em MetricsService.experiments_per_batch
02364. [x] app\services\metrics_service.py:82 — definir/revisar FunctionDef: MetricsService.actions_per_day
02365. [x] app\services\metrics_service.py:82 — revisar facet 'assinatura/args consistentes' em MetricsService.actions_per_day
02366. [x] app\services\metrics_service.py:82 — revisar facet 'docstring em português' em MetricsService.actions_per_day
02367. [x] app\services\metrics_service.py:82 — revisar facet 'nomenclatura clara (PEP8)' em MetricsService.actions_per_day
02368. [x] app\services\metrics_service.py:82 — revisar facet 'type hints presentes' em MetricsService.actions_per_day
02369. [x] app\services\metrics_service.py:82 — revisar facet 'tratamento de erros adequado' em MetricsService.actions_per_day
02370. [x] app\services\metrics_service.py:82 — revisar facet 'sem comentários inline desnecessários' em MetricsService.actions_per_day
02371. [x] app\services\metrics_service.py:82 — revisar facet 'não imprime side-effects na UI/IO' em MetricsService.actions_per_day
02372. [x] app\services\metrics_service.py:82 — revisar facet 'thread-safety revisada' em MetricsService.actions_per_day
02373. [x] app\services\metrics_service.py:82 — revisar facet 'performance (sem loops O(n^2))' em MetricsService.actions_per_day
02374. [x] app\services\metrics_service.py:82 — revisar facet 'coberto por testes' em MetricsService.actions_per_day
02375. [x] app\services\metrics_service.py:83 — atribuição: MetricsService.actions_per_day ← cutoff
02376. [x] app\services\metrics_service.py:84 — atribuição: MetricsService.actions_per_day ← rows
02377. [x] app\services\metrics_service.py:94 — return em MetricsService.actions_per_day
02378. [x] app\services\metrics_service.py:96 — definir/revisar FunctionDef: MetricsService.top_actions
02379. [x] app\services\metrics_service.py:96 — revisar facet 'assinatura/args consistentes' em MetricsService.top_actions
02380. [x] app\services\metrics_service.py:96 — revisar facet 'docstring em português' em MetricsService.top_actions
02381. [x] app\services\metrics_service.py:96 — revisar facet 'nomenclatura clara (PEP8)' em MetricsService.top_actions
02382. [x] app\services\metrics_service.py:96 — revisar facet 'type hints presentes' em MetricsService.top_actions
02383. [x] app\services\metrics_service.py:96 — revisar facet 'tratamento de erros adequado' em MetricsService.top_actions
02384. [x] app\services\metrics_service.py:96 — revisar facet 'sem comentários inline desnecessários' em MetricsService.top_actions
02385. [x] app\services\metrics_service.py:96 — revisar facet 'não imprime side-effects na UI/IO' em MetricsService.top_actions
02386. [x] app\services\metrics_service.py:96 — revisar facet 'thread-safety revisada' em MetricsService.top_actions
02387. [x] app\services\metrics_service.py:96 — revisar facet 'performance (sem loops O(n^2))' em MetricsService.top_actions
02388. [x] app\services\metrics_service.py:96 — revisar facet 'coberto por testes' em MetricsService.top_actions
02389. [x] app\services\metrics_service.py:97 — atribuição: MetricsService.top_actions ← rows
02390. [x] app\services\metrics_service.py:108 — return em MetricsService.top_actions
02391. [x] Existência e estrutura do módulo: app\services\preview_service.py
02392. [x] app\services\preview_service.py:3 — import: __future__
02393. [x] app\services\preview_service.py:5 — import: typing
02394. [x] app\services\preview_service.py:7 — import: app.domain.entities
02395. [x] app\services\preview_service.py:8 — import: app.services.sampling_service
02396. [x] app\services\preview_service.py:11 — definir/revisar ClassDef: PreviewService
02397. [x] app\services\preview_service.py:12 — definir/revisar FunctionDef: PreviewService.__init__
02398. [x] app\services\preview_service.py:12 — revisar facet 'assinatura/args consistentes' em PreviewService.__init__
02399. [x] app\services\preview_service.py:12 — revisar facet 'docstring em português' em PreviewService.__init__
02400. [x] app\services\preview_service.py:12 — revisar facet 'nomenclatura clara (PEP8)' em PreviewService.__init__
02401. [x] app\services\preview_service.py:12 — revisar facet 'type hints presentes' em PreviewService.__init__
02402. [x] app\services\preview_service.py:12 — revisar facet 'tratamento de erros adequado' em PreviewService.__init__
02403. [x] app\services\preview_service.py:12 — revisar facet 'sem comentários inline desnecessários' em PreviewService.__init__
02404. [x] app\services\preview_service.py:12 — revisar facet 'não imprime side-effects na UI/IO' em PreviewService.__init__
02405. [x] app\services\preview_service.py:12 — revisar facet 'thread-safety revisada' em PreviewService.__init__
02406. [x] app\services\preview_service.py:12 — revisar facet 'performance (sem loops O(n^2))' em PreviewService.__init__
02407. [x] app\services\preview_service.py:12 — revisar facet 'coberto por testes' em PreviewService.__init__
02408. [x] app\services\preview_service.py:13 — atribuição: PreviewService.__init__ ← ?
02409. [x] app\services\preview_service.py:15 — definir/revisar FunctionDef: PreviewService.sample_one
02410. [x] app\services\preview_service.py:15 — revisar facet 'assinatura/args consistentes' em PreviewService.sample_one
02411. [x] app\services\preview_service.py:15 — revisar facet 'docstring em português' em PreviewService.sample_one
02412. [x] app\services\preview_service.py:15 — revisar facet 'nomenclatura clara (PEP8)' em PreviewService.sample_one
02413. [x] app\services\preview_service.py:15 — revisar facet 'type hints presentes' em PreviewService.sample_one
02414. [x] app\services\preview_service.py:15 — revisar facet 'tratamento de erros adequado' em PreviewService.sample_one
02415. [x] app\services\preview_service.py:15 — revisar facet 'sem comentários inline desnecessários' em PreviewService.sample_one
02416. [x] app\services\preview_service.py:15 — revisar facet 'não imprime side-effects na UI/IO' em PreviewService.sample_one
02417. [x] app\services\preview_service.py:15 — revisar facet 'thread-safety revisada' em PreviewService.sample_one
02418. [x] app\services\preview_service.py:15 — revisar facet 'performance (sem loops O(n^2))' em PreviewService.sample_one
02419. [x] app\services\preview_service.py:15 — revisar facet 'coberto por testes' em PreviewService.sample_one
02420. [x] app\services\preview_service.py:20 — import: app.core.parsing
02421. [x] app\services\preview_service.py:22 — controle if em PreviewService.sample_one
02422. [x] app\services\preview_service.py:23 — atribuição: PreviewService.sample_one ← request
02423. [x] app\services\preview_service.py:31 — return em PreviewService.sample_one
02424. [x] app\services\preview_service.py:33 — atribuição: PreviewService.sample_one ← request
02425. [x] app\services\preview_service.py:41 — atribuição: PreviewService.sample_one ← result
02426. [x] app\services\preview_service.py:43 — return em PreviewService.sample_one
02427. [x] app\services\preview_service.py:49 — definir/revisar FunctionDef: PreviewService.render
02428. [x] app\services\preview_service.py:49 — revisar facet 'assinatura/args consistentes' em PreviewService.render
02429. [x] app\services\preview_service.py:49 — revisar facet 'docstring em português' em PreviewService.render
02430. [x] app\services\preview_service.py:49 — revisar facet 'nomenclatura clara (PEP8)' em PreviewService.render
02431. [x] app\services\preview_service.py:49 — revisar facet 'type hints presentes' em PreviewService.render
02432. [x] app\services\preview_service.py:49 — revisar facet 'tratamento de erros adequado' em PreviewService.render
02433. [x] app\services\preview_service.py:49 — revisar facet 'sem comentários inline desnecessários' em PreviewService.render
02434. [x] app\services\preview_service.py:49 — revisar facet 'não imprime side-effects na UI/IO' em PreviewService.render
02435. [x] app\services\preview_service.py:49 — revisar facet 'thread-safety revisada' em PreviewService.render
02436. [x] app\services\preview_service.py:49 — revisar facet 'performance (sem loops O(n^2))' em PreviewService.render
02437. [x] app\services\preview_service.py:49 — revisar facet 'coberto por testes' em PreviewService.render
02438. [x] app\services\preview_service.py:55 — import: app.core.parsing
02439. [x] app\services\preview_service.py:57 — atribuição: PreviewService.render ← values
02440. [x] app\services\preview_service.py:59 — definir/revisar FunctionDef: PreviewService.render.replace
02441. [x] app\services\preview_service.py:59 — revisar facet 'assinatura/args consistentes' em PreviewService.render.replace
02442. [x] app\services\preview_service.py:59 — revisar facet 'docstring em português' em PreviewService.render.replace
02443. [x] app\services\preview_service.py:59 — revisar facet 'nomenclatura clara (PEP8)' em PreviewService.render.replace
02444. [x] app\services\preview_service.py:59 — revisar facet 'type hints presentes' em PreviewService.render.replace
02445. [x] app\services\preview_service.py:59 — revisar facet 'tratamento de erros adequado' em PreviewService.render.replace
02446. [x] app\services\preview_service.py:59 — revisar facet 'sem comentários inline desnecessários' em PreviewService.render.replace
02447. [x] app\services\preview_service.py:59 — revisar facet 'não imprime side-effects na UI/IO' em PreviewService.render.replace
02448. [x] app\services\preview_service.py:59 — revisar facet 'thread-safety revisada' em PreviewService.render.replace
02449. [x] app\services\preview_service.py:59 — revisar facet 'performance (sem loops O(n^2))' em PreviewService.render.replace
02450. [x] app\services\preview_service.py:59 — revisar facet 'coberto por testes' em PreviewService.render.replace
02451. [x] app\services\preview_service.py:60 — atribuição: PreviewService.render.replace ← var_id
02452. [x] app\services\preview_service.py:61 — atribuição: PreviewService.render.replace ← value
02453. [x] app\services\preview_service.py:62 — return em PreviewService.render.replace
02454. [x] app\services\preview_service.py:64 — return em PreviewService.render
02455. [x] Existência e estrutura do módulo: app\services\sampling_service.py
02456. [x] app\services\sampling_service.py:3 — import: __future__
02457. [x] app\services\sampling_service.py:5 — import: time
02458. [x] app\services\sampling_service.py:6 — import: typing
02459. [x] app\services\sampling_service.py:8 — import: numpy
02460. [x] app\services\sampling_service.py:10 — import: app.domain.entities
02461. [x] app\services\sampling_service.py:15 — import: app.infrastructure.distribution_registry
02462. [x] app\services\sampling_service.py:16 — import: app.services.strategies.correlated
02463. [x] app\services\sampling_service.py:17 — import: app.services.strategies.latin_hypercube
02464. [x] app\services\sampling_service.py:23 — definir/revisar ClassDef: SamplingService
02465. [x] app\services\sampling_service.py:26 — definir/revisar FunctionDef: SamplingService.__init__
02466. [x] app\services\sampling_service.py:26 — revisar facet 'assinatura/args consistentes' em SamplingService.__init__
02467. [x] app\services\sampling_service.py:26 — revisar facet 'docstring em português' em SamplingService.__init__
02468. [x] app\services\sampling_service.py:26 — revisar facet 'nomenclatura clara (PEP8)' em SamplingService.__init__
02469. [x] app\services\sampling_service.py:26 — revisar facet 'type hints presentes' em SamplingService.__init__
02470. [x] app\services\sampling_service.py:26 — revisar facet 'tratamento de erros adequado' em SamplingService.__init__
02471. [x] app\services\sampling_service.py:26 — revisar facet 'sem comentários inline desnecessários' em SamplingService.__init__
02472. [x] app\services\sampling_service.py:26 — revisar facet 'não imprime side-effects na UI/IO' em SamplingService.__init__
02473. [x] app\services\sampling_service.py:26 — revisar facet 'thread-safety revisada' em SamplingService.__init__
02474. [x] app\services\sampling_service.py:26 — revisar facet 'performance (sem loops O(n^2))' em SamplingService.__init__
02475. [x] app\services\sampling_service.py:26 — revisar facet 'coberto por testes' em SamplingService.__init__
02476. [x] app\services\sampling_service.py:27 — atribuição: SamplingService.__init__ ← ?
02477. [x] app\services\sampling_service.py:28 — atribuição: SamplingService.__init__ ← ?
02478. [x] app\services\sampling_service.py:33 — definir/revisar FunctionDef: SamplingService.register_strategy
02479. [x] app\services\sampling_service.py:33 — revisar facet 'assinatura/args consistentes' em SamplingService.register_strategy
02480. [x] app\services\sampling_service.py:33 — revisar facet 'docstring em português' em SamplingService.register_strategy
02481. [x] app\services\sampling_service.py:33 — revisar facet 'nomenclatura clara (PEP8)' em SamplingService.register_strategy
02482. [x] app\services\sampling_service.py:33 — revisar facet 'type hints presentes' em SamplingService.register_strategy
02483. [x] app\services\sampling_service.py:33 — revisar facet 'tratamento de erros adequado' em SamplingService.register_strategy
02484. [x] app\services\sampling_service.py:33 — revisar facet 'sem comentários inline desnecessários' em SamplingService.register_strategy
02485. [x] app\services\sampling_service.py:33 — revisar facet 'não imprime side-effects na UI/IO' em SamplingService.register_strategy
02486. [x] app\services\sampling_service.py:33 — revisar facet 'thread-safety revisada' em SamplingService.register_strategy
02487. [x] app\services\sampling_service.py:33 — revisar facet 'performance (sem loops O(n^2))' em SamplingService.register_strategy
02488. [x] app\services\sampling_service.py:33 — revisar facet 'coberto por testes' em SamplingService.register_strategy
02489. [x] app\services\sampling_service.py:35 — atribuição: SamplingService.register_strategy ← ?
02490. [x] app\services\sampling_service.py:37 — definir/revisar FunctionDef: SamplingService.run
02491. [x] app\services\sampling_service.py:37 — revisar facet 'assinatura/args consistentes' em SamplingService.run
02492. [x] app\services\sampling_service.py:37 — revisar facet 'docstring em português' em SamplingService.run
02493. [x] app\services\sampling_service.py:37 — revisar facet 'nomenclatura clara (PEP8)' em SamplingService.run
02494. [x] app\services\sampling_service.py:37 — revisar facet 'type hints presentes' em SamplingService.run
02495. [x] app\services\sampling_service.py:37 — revisar facet 'tratamento de erros adequado' em SamplingService.run
02496. [x] app\services\sampling_service.py:37 — revisar facet 'sem comentários inline desnecessários' em SamplingService.run
02497. [x] app\services\sampling_service.py:37 — revisar facet 'não imprime side-effects na UI/IO' em SamplingService.run
02498. [x] app\services\sampling_service.py:37 — revisar facet 'thread-safety revisada' em SamplingService.run
02499. [x] app\services\sampling_service.py:37 — revisar facet 'performance (sem loops O(n^2))' em SamplingService.run
02500. [x] app\services\sampling_service.py:37 — revisar facet 'coberto por testes' em SamplingService.run
02501. [x] app\services\sampling_service.py:42 — atribuição: SamplingService.run ← start
02502. [x] app\services\sampling_service.py:44 — atribuição: SamplingService.run ← strategy
02503. [x] app\services\sampling_service.py:45 — controle if em SamplingService.run
02504. [x] app\services\sampling_service.py:46 — raise em SamplingService.run
02505. [x] app\services\sampling_service.py:48 — atribuição: SamplingService.run ← var_ids
02506. [x] app\services\sampling_service.py:49 — atribuição: SamplingService.run ← n
02507. [x] app\services\sampling_service.py:50 — atribuição: SamplingService.run ← d
02508. [x] app\services\sampling_service.py:52 — controle if em SamplingService.run
02509. [x] app\services\sampling_service.py:53 — return em SamplingService.run
02510. [x] app\services\sampling_service.py:55 — atribuição: SamplingService.run ← rng
02511. [x] app\services\sampling_service.py:56 — atribuição: SamplingService.run ← matrix
02512. [x] app\services\sampling_service.py:58 — controle if em SamplingService.run
02513. [x] app\services\sampling_service.py:59 — atribuição: SamplingService.run ← matrix
02514. [x] app\services\sampling_service.py:61 — atribuição: SamplingService.run ← uniforms
02515. [x] app\services\sampling_service.py:63 — controle for em SamplingService.run
02516. [x] app\services\sampling_service.py:64 — atribuição: SamplingService.run ← spec
02517. [x] app\services\sampling_service.py:65 — atribuição: SamplingService.run ← provider
02518. [x] app\services\sampling_service.py:67 — try em SamplingService.run
02519. [x] app\services\sampling_service.py:68 — controle if em SamplingService.run
02520. [x] app\services\sampling_service.py:69 — atribuição: SamplingService.run ← ?
02521. [x] app\services\sampling_service.py:71 — atribuição: SamplingService.run ← ?
02522. [x] app\services\sampling_service.py:73 — atribuição: SamplingService.run ← ?
02523. [x] app\services\sampling_service.py:75 — controle if em SamplingService.run
02524. [x] app\services\sampling_service.py:76 — atribuição: SamplingService.run ← percent
02525. [x] app\services\sampling_service.py:79 — atribuição: SamplingService.run ← duration
02526. [x] app\services\sampling_service.py:81 — return em SamplingService.run
02527. [x] app\services\sampling_service.py:88 — definir/revisar FunctionDef: SamplingService._sample_correlated
02528. [x] app\services\sampling_service.py:88 — revisar facet 'assinatura/args consistentes' em SamplingService._sample_correlated
02529. [x] app\services\sampling_service.py:88 — revisar facet 'docstring em português' em SamplingService._sample_correlated
02530. [x] app\services\sampling_service.py:88 — revisar facet 'nomenclatura clara (PEP8)' em SamplingService._sample_correlated
02531. [x] app\services\sampling_service.py:88 — revisar facet 'type hints presentes' em SamplingService._sample_correlated
02532. [x] app\services\sampling_service.py:88 — revisar facet 'tratamento de erros adequado' em SamplingService._sample_correlated
02533. [x] app\services\sampling_service.py:88 — revisar facet 'sem comentários inline desnecessários' em SamplingService._sample_correlated
02534. [x] app\services\sampling_service.py:88 — revisar facet 'não imprime side-effects na UI/IO' em SamplingService._sample_correlated
02535. [x] app\services\sampling_service.py:88 — revisar facet 'thread-safety revisada' em SamplingService._sample_correlated
02536. [x] app\services\sampling_service.py:88 — revisar facet 'performance (sem loops O(n^2))' em SamplingService._sample_correlated
02537. [x] app\services\sampling_service.py:88 — revisar facet 'coberto por testes' em SamplingService._sample_correlated
02538. [x] app\services\sampling_service.py:90 — atribuição: SamplingService._sample_correlated ← n
02539. [x] app\services\sampling_service.py:91 — atribuição: SamplingService._sample_correlated ← d
02540. [x] app\services\sampling_service.py:93 — atribuição: SamplingService._sample_correlated ← base
02541. [x] app\services\sampling_service.py:94 — controle for em SamplingService._sample_correlated
02542. [x] app\services\sampling_service.py:95 — atribuição: SamplingService._sample_correlated ← spec
02543. [x] app\services\sampling_service.py:96 — atribuição: SamplingService._sample_correlated ← provider
02544. [x] app\services\sampling_service.py:97 — atribuição: SamplingService._sample_correlated ← ?
02545. [x] app\services\sampling_service.py:99 — controle if em SamplingService._sample_correlated
02546. [x] app\services\sampling_service.py:100 — return em SamplingService._sample_correlated
02547. [x] app\services\sampling_service.py:102 — atribuição: SamplingService._sample_correlated ← corr
02548. [x] app\services\sampling_service.py:103 — return em SamplingService._sample_correlated
02549. [x] app\services\sampling_service.py:106 — definir/revisar FunctionDef: SamplingService.p10_p50_p90
02550. [x] app\services\sampling_service.py:106 — revisar facet 'assinatura/args consistentes' em SamplingService.p10_p50_p90
02551. [x] app\services\sampling_service.py:106 — revisar facet 'docstring em português' em SamplingService.p10_p50_p90
02552. [x] app\services\sampling_service.py:106 — revisar facet 'nomenclatura clara (PEP8)' em SamplingService.p10_p50_p90
02553. [x] app\services\sampling_service.py:106 — revisar facet 'type hints presentes' em SamplingService.p10_p50_p90
02554. [x] app\services\sampling_service.py:106 — revisar facet 'tratamento de erros adequado' em SamplingService.p10_p50_p90
02555. [x] app\services\sampling_service.py:106 — revisar facet 'sem comentários inline desnecessários' em SamplingService.p10_p50_p90
02556. [x] app\services\sampling_service.py:106 — revisar facet 'não imprime side-effects na UI/IO' em SamplingService.p10_p50_p90
02557. [x] app\services\sampling_service.py:106 — revisar facet 'thread-safety revisada' em SamplingService.p10_p50_p90
02558. [x] app\services\sampling_service.py:106 — revisar facet 'performance (sem loops O(n^2))' em SamplingService.p10_p50_p90
02559. [x] app\services\sampling_service.py:106 — revisar facet 'coberto por testes' em SamplingService.p10_p50_p90
02560. [x] app\services\sampling_service.py:107 — controle if em SamplingService.p10_p50_p90
02561. [x] app\services\sampling_service.py:108 — return em SamplingService.p10_p50_p90
02562. [x] app\services\sampling_service.py:109 — atribuição: SamplingService.p10_p50_p90 ← ?
02563. [x] app\services\sampling_service.py:110 — return em SamplingService.p10_p50_p90
02564. [x] Existência e estrutura do módulo: app\services\statistics_service.py
02565. [x] app\services\statistics_service.py:3 — import: __future__
02566. [x] app\services\statistics_service.py:5 — import: dataclasses
02567. [x] app\services\statistics_service.py:6 — import: typing
02568. [x] app\services\statistics_service.py:8 — import: numpy
02569. [x] app\services\statistics_service.py:12 — definir/revisar ClassDef: VariableStats
02570. [x] app\services\statistics_service.py:24 — definir/revisar ClassDef: StatisticsService
02571. [x] app\services\statistics_service.py:25 — definir/revisar FunctionDef: StatisticsService.compute
02572. [x] app\services\statistics_service.py:25 — revisar facet 'assinatura/args consistentes' em StatisticsService.compute
02573. [x] app\services\statistics_service.py:25 — revisar facet 'docstring em português' em StatisticsService.compute
02574. [x] app\services\statistics_service.py:25 — revisar facet 'nomenclatura clara (PEP8)' em StatisticsService.compute
02575. [x] app\services\statistics_service.py:25 — revisar facet 'type hints presentes' em StatisticsService.compute
02576. [x] app\services\statistics_service.py:25 — revisar facet 'tratamento de erros adequado' em StatisticsService.compute
02577. [x] app\services\statistics_service.py:25 — revisar facet 'sem comentários inline desnecessários' em StatisticsService.compute
02578. [x] app\services\statistics_service.py:25 — revisar facet 'não imprime side-effects na UI/IO' em StatisticsService.compute
02579. [x] app\services\statistics_service.py:25 — revisar facet 'thread-safety revisada' em StatisticsService.compute
02580. [x] app\services\statistics_service.py:25 — revisar facet 'performance (sem loops O(n^2))' em StatisticsService.compute
02581. [x] app\services\statistics_service.py:25 — revisar facet 'coberto por testes' em StatisticsService.compute
02582. [x] app\services\statistics_service.py:26 — controle if em StatisticsService.compute
02583. [x] app\services\statistics_service.py:27 — return em StatisticsService.compute
02584. [x] app\services\statistics_service.py:29 — atribuição: StatisticsService.compute ← arr
02585. [x] app\services\statistics_service.py:30 — atribuição: StatisticsService.compute ← ?
02586. [x] app\services\statistics_service.py:32 — return em StatisticsService.compute
02587. [x] app\services\statistics_service.py:44 — definir/revisar FunctionDef: StatisticsService.histogram
02588. [x] app\services\statistics_service.py:44 — revisar facet 'assinatura/args consistentes' em StatisticsService.histogram
02589. [x] app\services\statistics_service.py:44 — revisar facet 'docstring em português' em StatisticsService.histogram
02590. [x] app\services\statistics_service.py:44 — revisar facet 'nomenclatura clara (PEP8)' em StatisticsService.histogram
02591. [x] app\services\statistics_service.py:44 — revisar facet 'type hints presentes' em StatisticsService.histogram
02592. [x] app\services\statistics_service.py:44 — revisar facet 'tratamento de erros adequado' em StatisticsService.histogram
02593. [x] app\services\statistics_service.py:44 — revisar facet 'sem comentários inline desnecessários' em StatisticsService.histogram
02594. [x] app\services\statistics_service.py:44 — revisar facet 'não imprime side-effects na UI/IO' em StatisticsService.histogram
02595. [x] app\services\statistics_service.py:44 — revisar facet 'thread-safety revisada' em StatisticsService.histogram
02596. [x] app\services\statistics_service.py:44 — revisar facet 'performance (sem loops O(n^2))' em StatisticsService.histogram
02597. [x] app\services\statistics_service.py:44 — revisar facet 'coberto por testes' em StatisticsService.histogram
02598. [x] app\services\statistics_service.py:49 — atribuição: StatisticsService.histogram ← arr
02599. [x] app\services\statistics_service.py:50 — atribuição: StatisticsService.histogram ← ?
02600. [x] app\services\statistics_service.py:51 — return em StatisticsService.histogram
02601. [x] Existência e estrutura do módulo: app\services\strategies\__init__.py
02602. [x] app\services\strategies\__init__.py:3 — import: app.services.strategies.base
02603. [x] app\services\strategies\__init__.py:4 — import: app.services.strategies.correlated
02604. [x] app\services\strategies\__init__.py:5 — import: app.services.strategies.latin_hypercube
02605. [x] app\services\strategies\__init__.py:7 — atribuição:  ← __all__
02606. [x] Existência e estrutura do módulo: app\services\strategies\base.py
02607. [x] app\services\strategies\base.py:1 — import: __future__
02608. [x] app\services\strategies\base.py:3 — import: typing
02609. [x] app\services\strategies\base.py:5 — import: numpy
02610. [x] app\services\strategies\base.py:9 — definir/revisar ClassDef: UnionSamplingStrategy
02611. [x] app\services\strategies\base.py:14 — definir/revisar FunctionDef: UnionSamplingStrategy.generate_uniforms
02612. [x] app\services\strategies\base.py:14 — revisar facet 'assinatura/args consistentes' em UnionSamplingStrategy.generate_uniforms
02613. [x] app\services\strategies\base.py:14 — revisar facet 'docstring em português' em UnionSamplingStrategy.generate_uniforms
02614. [x] app\services\strategies\base.py:14 — revisar facet 'nomenclatura clara (PEP8)' em UnionSamplingStrategy.generate_uniforms
02615. [x] app\services\strategies\base.py:14 — revisar facet 'type hints presentes' em UnionSamplingStrategy.generate_uniforms
02616. [x] app\services\strategies\base.py:14 — revisar facet 'tratamento de erros adequado' em UnionSamplingStrategy.generate_uniforms
02617. [x] app\services\strategies\base.py:14 — revisar facet 'sem comentários inline desnecessários' em UnionSamplingStrategy.generate_uniforms
02618. [x] app\services\strategies\base.py:14 — revisar facet 'não imprime side-effects na UI/IO' em UnionSamplingStrategy.generate_uniforms
02619. [x] app\services\strategies\base.py:14 — revisar facet 'thread-safety revisada' em UnionSamplingStrategy.generate_uniforms
02620. [x] app\services\strategies\base.py:14 — revisar facet 'performance (sem loops O(n^2))' em UnionSamplingStrategy.generate_uniforms
02621. [x] app\services\strategies\base.py:14 — revisar facet 'coberto por testes' em UnionSamplingStrategy.generate_uniforms
02622. [x] app\services\strategies\base.py:17 — definir/revisar FunctionDef: make_strategy_fn
02623. [x] app\services\strategies\base.py:17 — revisar facet 'assinatura/args consistentes' em make_strategy_fn
02624. [x] app\services\strategies\base.py:17 — revisar facet 'docstring em português' em make_strategy_fn
02625. [x] app\services\strategies\base.py:17 — revisar facet 'nomenclatura clara (PEP8)' em make_strategy_fn
02626. [x] app\services\strategies\base.py:17 — revisar facet 'type hints presentes' em make_strategy_fn
02627. [x] app\services\strategies\base.py:17 — revisar facet 'tratamento de erros adequado' em make_strategy_fn
02628. [x] app\services\strategies\base.py:17 — revisar facet 'sem comentários inline desnecessários' em make_strategy_fn
02629. [x] app\services\strategies\base.py:17 — revisar facet 'não imprime side-effects na UI/IO' em make_strategy_fn
02630. [x] app\services\strategies\base.py:17 — revisar facet 'thread-safety revisada' em make_strategy_fn
02631. [x] app\services\strategies\base.py:17 — revisar facet 'performance (sem loops O(n^2))' em make_strategy_fn
02632. [x] app\services\strategies\base.py:17 — revisar facet 'coberto por testes' em make_strategy_fn
02633. [x] app\services\strategies\base.py:19 — atribuição: make_strategy_fn ← ?
02634. [x] app\services\strategies\base.py:20 — return em make_strategy_fn
02635. [x] Existência e estrutura do módulo: app\services\strategies\correlated.py
02636. [x] app\services\strategies\correlated.py:1 — import: __future__
02637. [x] app\services\strategies\correlated.py:3 — import: typing
02638. [x] app\services\strategies\correlated.py:5 — import: numpy
02639. [x] app\services\strategies\correlated.py:6 — import: scipy
02640. [x] app\services\strategies\correlated.py:9 — definir/revisar ClassDef: CorrelatedStrategy
02641. [x] app\services\strategies\correlated.py:12 — atribuição: CorrelatedStrategy ← name
02642. [x] app\services\strategies\correlated.py:15 — definir/revisar FunctionDef: CorrelatedStrategy.apply
02643. [x] app\services\strategies\correlated.py:15 — revisar facet 'assinatura/args consistentes' em CorrelatedStrategy.apply
02644. [x] app\services\strategies\correlated.py:15 — revisar facet 'docstring em português' em CorrelatedStrategy.apply
02645. [x] app\services\strategies\correlated.py:15 — revisar facet 'nomenclatura clara (PEP8)' em CorrelatedStrategy.apply
02646. [x] app\services\strategies\correlated.py:15 — revisar facet 'type hints presentes' em CorrelatedStrategy.apply
02647. [x] app\services\strategies\correlated.py:15 — revisar facet 'tratamento de erros adequado' em CorrelatedStrategy.apply
02648. [x] app\services\strategies\correlated.py:15 — revisar facet 'sem comentários inline desnecessários' em CorrelatedStrategy.apply
02649. [x] app\services\strategies\correlated.py:15 — revisar facet 'não imprime side-effects na UI/IO' em CorrelatedStrategy.apply
02650. [x] app\services\strategies\correlated.py:15 — revisar facet 'thread-safety revisada' em CorrelatedStrategy.apply
02651. [x] app\services\strategies\correlated.py:15 — revisar facet 'performance (sem loops O(n^2))' em CorrelatedStrategy.apply
02652. [x] app\services\strategies\correlated.py:15 — revisar facet 'coberto por testes' em CorrelatedStrategy.apply
02653. [x] app\services\strategies\correlated.py:16 — return em CorrelatedStrategy.apply
02654. [x] app\services\strategies\correlated.py:19 — definir/revisar FunctionDef: CorrelatedStrategy.validate
02655. [x] app\services\strategies\correlated.py:19 — revisar facet 'assinatura/args consistentes' em CorrelatedStrategy.validate
02656. [x] app\services\strategies\correlated.py:19 — revisar facet 'docstring em português' em CorrelatedStrategy.validate
02657. [x] app\services\strategies\correlated.py:19 — revisar facet 'nomenclatura clara (PEP8)' em CorrelatedStrategy.validate
02658. [x] app\services\strategies\correlated.py:19 — revisar facet 'type hints presentes' em CorrelatedStrategy.validate
02659. [x] app\services\strategies\correlated.py:19 — revisar facet 'tratamento de erros adequado' em CorrelatedStrategy.validate
02660. [x] app\services\strategies\correlated.py:19 — revisar facet 'sem comentários inline desnecessários' em CorrelatedStrategy.validate
02661. [x] app\services\strategies\correlated.py:19 — revisar facet 'não imprime side-effects na UI/IO' em CorrelatedStrategy.validate
02662. [x] app\services\strategies\correlated.py:19 — revisar facet 'thread-safety revisada' em CorrelatedStrategy.validate
02663. [x] app\services\strategies\correlated.py:19 — revisar facet 'performance (sem loops O(n^2))' em CorrelatedStrategy.validate
02664. [x] app\services\strategies\correlated.py:19 — revisar facet 'coberto por testes' em CorrelatedStrategy.validate
02665. [x] app\services\strategies\correlated.py:20 — atribuição: CorrelatedStrategy.validate ← m
02666. [x] app\services\strategies\correlated.py:21 — controle if em CorrelatedStrategy.validate
02667. [x] app\services\strategies\correlated.py:22 — return em CorrelatedStrategy.validate
02668. [x] app\services\strategies\correlated.py:23 — controle if em CorrelatedStrategy.validate
02669. [x] app\services\strategies\correlated.py:24 — return em CorrelatedStrategy.validate
02670. [x] app\services\strategies\correlated.py:25 — return em CorrelatedStrategy.validate
02671. [x] app\services\strategies\correlated.py:28 — definir/revisar FunctionDef: iman_conover_reorder
02672. [x] app\services\strategies\correlated.py:28 — revisar facet 'assinatura/args consistentes' em iman_conover_reorder
02673. [x] app\services\strategies\correlated.py:28 — revisar facet 'docstring em português' em iman_conover_reorder
02674. [x] app\services\strategies\correlated.py:28 — revisar facet 'nomenclatura clara (PEP8)' em iman_conover_reorder
02675. [x] app\services\strategies\correlated.py:28 — revisar facet 'type hints presentes' em iman_conover_reorder
02676. [x] app\services\strategies\correlated.py:28 — revisar facet 'tratamento de erros adequado' em iman_conover_reorder
02677. [x] app\services\strategies\correlated.py:28 — revisar facet 'sem comentários inline desnecessários' em iman_conover_reorder
02678. [x] app\services\strategies\correlated.py:28 — revisar facet 'não imprime side-effects na UI/IO' em iman_conover_reorder
02679. [x] app\services\strategies\correlated.py:28 — revisar facet 'thread-safety revisada' em iman_conover_reorder
02680. [x] app\services\strategies\correlated.py:28 — revisar facet 'performance (sem loops O(n^2))' em iman_conover_reorder
02681. [x] app\services\strategies\correlated.py:28 — revisar facet 'coberto por testes' em iman_conover_reorder
02682. [x] app\services\strategies\correlated.py:34 — atribuição: iman_conover_reorder ← ?
02683. [x] app\services\strategies\correlated.py:35 — atribuição: iman_conover_reorder ← corr
02684. [x] app\services\strategies\correlated.py:37 — atribuição: iman_conover_reorder ← rng
02685. [x] app\services\strategies\correlated.py:38 — atribuição: iman_conover_reorder ← mvn
02686. [x] app\services\strategies\correlated.py:41 — atribuição: iman_conover_reorder ← scores
02687. [x] app\services\strategies\correlated.py:42 — controle if em iman_conover_reorder
02688. [x] app\services\strategies\correlated.py:43 — atribuição: iman_conover_reorder ← scores
02689. [x] app\services\strategies\correlated.py:45 — atribuição: iman_conover_reorder ← result
02690. [x] app\services\strategies\correlated.py:46 — controle for em iman_conover_reorder
02691. [x] app\services\strategies\correlated.py:47 — atribuição: iman_conover_reorder ← order
02692. [x] app\services\strategies\correlated.py:48 — atribuição: iman_conover_reorder ← sorted_vals
02693. [x] app\services\strategies\correlated.py:49 — atribuição: iman_conover_reorder ← ?
02694. [x] app\services\strategies\correlated.py:51 — return em iman_conover_reorder
02695. [x] Existência e estrutura do módulo: app\services\strategies\latin_hypercube.py
02696. [x] app\services\strategies\latin_hypercube.py:1 — import: __future__
02697. [x] app\services\strategies\latin_hypercube.py:3 — import: numpy
02698. [x] app\services\strategies\latin_hypercube.py:4 — import: scipy.stats
02699. [x] app\services\strategies\latin_hypercube.py:7 — definir/revisar ClassDef: MonteCarloStrategy
02700. [x] app\services\strategies\latin_hypercube.py:8 — atribuição: MonteCarloStrategy ← name
02701. [x] app\services\strategies\latin_hypercube.py:10 — definir/revisar FunctionDef: MonteCarloStrategy.generate_uniforms
02702. [x] app\services\strategies\latin_hypercube.py:10 — revisar facet 'assinatura/args consistentes' em MonteCarloStrategy.generate_uniforms
02703. [x] app\services\strategies\latin_hypercube.py:10 — revisar facet 'docstring em português' em MonteCarloStrategy.generate_uniforms
02704. [x] app\services\strategies\latin_hypercube.py:10 — revisar facet 'nomenclatura clara (PEP8)' em MonteCarloStrategy.generate_uniforms
02705. [x] app\services\strategies\latin_hypercube.py:10 — revisar facet 'type hints presentes' em MonteCarloStrategy.generate_uniforms
02706. [x] app\services\strategies\latin_hypercube.py:10 — revisar facet 'tratamento de erros adequado' em MonteCarloStrategy.generate_uniforms
02707. [x] app\services\strategies\latin_hypercube.py:10 — revisar facet 'sem comentários inline desnecessários' em MonteCarloStrategy.generate_uniforms
02708. [x] app\services\strategies\latin_hypercube.py:10 — revisar facet 'não imprime side-effects na UI/IO' em MonteCarloStrategy.generate_uniforms
02709. [x] app\services\strategies\latin_hypercube.py:10 — revisar facet 'thread-safety revisada' em MonteCarloStrategy.generate_uniforms
02710. [x] app\services\strategies\latin_hypercube.py:10 — revisar facet 'performance (sem loops O(n^2))' em MonteCarloStrategy.generate_uniforms
02711. [x] app\services\strategies\latin_hypercube.py:10 — revisar facet 'coberto por testes' em MonteCarloStrategy.generate_uniforms
02712. [x] app\services\strategies\latin_hypercube.py:11 — return em MonteCarloStrategy.generate_uniforms
02713. [x] app\services\strategies\latin_hypercube.py:14 — definir/revisar ClassDef: LatinHypercubeStrategy
02714. [x] app\services\strategies\latin_hypercube.py:15 — atribuição: LatinHypercubeStrategy ← name
02715. [x] app\services\strategies\latin_hypercube.py:17 — definir/revisar FunctionDef: LatinHypercubeStrategy.generate_uniforms
02716. [x] app\services\strategies\latin_hypercube.py:17 — revisar facet 'assinatura/args consistentes' em LatinHypercubeStrategy.generate_uniforms
02717. [x] app\services\strategies\latin_hypercube.py:17 — revisar facet 'docstring em português' em LatinHypercubeStrategy.generate_uniforms
02718. [x] app\services\strategies\latin_hypercube.py:17 — revisar facet 'nomenclatura clara (PEP8)' em LatinHypercubeStrategy.generate_uniforms
02719. [x] app\services\strategies\latin_hypercube.py:17 — revisar facet 'type hints presentes' em LatinHypercubeStrategy.generate_uniforms
02720. [x] app\services\strategies\latin_hypercube.py:17 — revisar facet 'tratamento de erros adequado' em LatinHypercubeStrategy.generate_uniforms
02721. [x] app\services\strategies\latin_hypercube.py:17 — revisar facet 'sem comentários inline desnecessários' em LatinHypercubeStrategy.generate_uniforms
02722. [x] app\services\strategies\latin_hypercube.py:17 — revisar facet 'não imprime side-effects na UI/IO' em LatinHypercubeStrategy.generate_uniforms
02723. [x] app\services\strategies\latin_hypercube.py:17 — revisar facet 'thread-safety revisada' em LatinHypercubeStrategy.generate_uniforms
02724. [x] app\services\strategies\latin_hypercube.py:17 — revisar facet 'performance (sem loops O(n^2))' em LatinHypercubeStrategy.generate_uniforms
02725. [x] app\services\strategies\latin_hypercube.py:17 — revisar facet 'coberto por testes' em LatinHypercubeStrategy.generate_uniforms
02726. [x] app\services\strategies\latin_hypercube.py:18 — atribuição: LatinHypercubeStrategy.generate_uniforms ← sampler
02727. [x] app\services\strategies\latin_hypercube.py:19 — return em LatinHypercubeStrategy.generate_uniforms
02728. [x] Existência e estrutura do módulo: app\services\strategies\monte_carlo.py
02729. [x] app\services\strategies\monte_carlo.py:1 — import: __future__
02730. [x] app\services\strategies\monte_carlo.py:3 — import: numpy
02731. [x] app\services\strategies\monte_carlo.py:6 — definir/revisar ClassDef: MonteCarloStrategy
02732. [x] app\services\strategies\monte_carlo.py:7 — atribuição: MonteCarloStrategy ← name
02733. [x] app\services\strategies\monte_carlo.py:9 — definir/revisar FunctionDef: MonteCarloStrategy.generate_uniforms
02734. [x] app\services\strategies\monte_carlo.py:9 — revisar facet 'assinatura/args consistentes' em MonteCarloStrategy.generate_uniforms
02735. [x] app\services\strategies\monte_carlo.py:9 — revisar facet 'docstring em português' em MonteCarloStrategy.generate_uniforms
02736. [x] app\services\strategies\monte_carlo.py:9 — revisar facet 'nomenclatura clara (PEP8)' em MonteCarloStrategy.generate_uniforms
02737. [x] app\services\strategies\monte_carlo.py:9 — revisar facet 'type hints presentes' em MonteCarloStrategy.generate_uniforms
02738. [x] app\services\strategies\monte_carlo.py:9 — revisar facet 'tratamento de erros adequado' em MonteCarloStrategy.generate_uniforms
02739. [x] app\services\strategies\monte_carlo.py:9 — revisar facet 'sem comentários inline desnecessários' em MonteCarloStrategy.generate_uniforms
02740. [x] app\services\strategies\monte_carlo.py:9 — revisar facet 'não imprime side-effects na UI/IO' em MonteCarloStrategy.generate_uniforms
02741. [x] app\services\strategies\monte_carlo.py:9 — revisar facet 'thread-safety revisada' em MonteCarloStrategy.generate_uniforms
02742. [x] app\services\strategies\monte_carlo.py:9 — revisar facet 'performance (sem loops O(n^2))' em MonteCarloStrategy.generate_uniforms
02743. [x] app\services\strategies\monte_carlo.py:9 — revisar facet 'coberto por testes' em MonteCarloStrategy.generate_uniforms
02744. [x] app\services\strategies\monte_carlo.py:10 — return em MonteCarloStrategy.generate_uniforms
02745. [x] Existência e estrutura do módulo: app\services\task_scheduler.py
02746. [x] app\services\task_scheduler.py:3 — import: __future__
02747. [x] app\services\task_scheduler.py:5 — import: typing
02748. [x] app\services\task_scheduler.py:7 — import: app.domain.tasks
02749. [x] app\services\task_scheduler.py:8 — import: app.infrastructure.task_repository
02750. [x] app\services\task_scheduler.py:11 — definir/revisar ClassDef: TaskScheduler
02751. [x] app\services\task_scheduler.py:12 — definir/revisar FunctionDef: TaskScheduler.__init__
02752. [x] app\services\task_scheduler.py:12 — revisar facet 'assinatura/args consistentes' em TaskScheduler.__init__
02753. [x] app\services\task_scheduler.py:12 — revisar facet 'docstring em português' em TaskScheduler.__init__
02754. [x] app\services\task_scheduler.py:12 — revisar facet 'nomenclatura clara (PEP8)' em TaskScheduler.__init__
02755. [x] app\services\task_scheduler.py:12 — revisar facet 'type hints presentes' em TaskScheduler.__init__
02756. [x] app\services\task_scheduler.py:12 — revisar facet 'tratamento de erros adequado' em TaskScheduler.__init__
02757. [x] app\services\task_scheduler.py:12 — revisar facet 'sem comentários inline desnecessários' em TaskScheduler.__init__
02758. [x] app\services\task_scheduler.py:12 — revisar facet 'não imprime side-effects na UI/IO' em TaskScheduler.__init__
02759. [x] app\services\task_scheduler.py:12 — revisar facet 'thread-safety revisada' em TaskScheduler.__init__
02760. [x] app\services\task_scheduler.py:12 — revisar facet 'performance (sem loops O(n^2))' em TaskScheduler.__init__
02761. [x] app\services\task_scheduler.py:12 — revisar facet 'coberto por testes' em TaskScheduler.__init__
02762. [x] app\services\task_scheduler.py:13 — atribuição: TaskScheduler.__init__ ← ?
02763. [x] app\services\task_scheduler.py:14 — atribuição: TaskScheduler.__init__ ← ?
02764. [x] app\services\task_scheduler.py:16 — definir/revisar FunctionDef: TaskScheduler.recover
02765. [x] app\services\task_scheduler.py:16 — revisar facet 'assinatura/args consistentes' em TaskScheduler.recover
02766. [x] app\services\task_scheduler.py:16 — revisar facet 'docstring em português' em TaskScheduler.recover
02767. [x] app\services\task_scheduler.py:16 — revisar facet 'nomenclatura clara (PEP8)' em TaskScheduler.recover
02768. [x] app\services\task_scheduler.py:16 — revisar facet 'type hints presentes' em TaskScheduler.recover
02769. [x] app\services\task_scheduler.py:16 — revisar facet 'tratamento de erros adequado' em TaskScheduler.recover
02770. [x] app\services\task_scheduler.py:16 — revisar facet 'sem comentários inline desnecessários' em TaskScheduler.recover
02771. [x] app\services\task_scheduler.py:16 — revisar facet 'não imprime side-effects na UI/IO' em TaskScheduler.recover
02772. [x] app\services\task_scheduler.py:16 — revisar facet 'thread-safety revisada' em TaskScheduler.recover
02773. [x] app\services\task_scheduler.py:16 — revisar facet 'performance (sem loops O(n^2))' em TaskScheduler.recover
02774. [x] app\services\task_scheduler.py:16 — revisar facet 'coberto por testes' em TaskScheduler.recover
02775. [x] app\services\task_scheduler.py:17 — return em TaskScheduler.recover
02776. [x] app\services\task_scheduler.py:19 — definir/revisar FunctionDef: TaskScheduler.enqueue_export
02777. [x] app\services\task_scheduler.py:19 — revisar facet 'assinatura/args consistentes' em TaskScheduler.enqueue_export
02778. [x] app\services\task_scheduler.py:19 — revisar facet 'docstring em português' em TaskScheduler.enqueue_export
02779. [x] app\services\task_scheduler.py:19 — revisar facet 'nomenclatura clara (PEP8)' em TaskScheduler.enqueue_export
02780. [x] app\services\task_scheduler.py:19 — revisar facet 'type hints presentes' em TaskScheduler.enqueue_export
02781. [x] app\services\task_scheduler.py:19 — revisar facet 'tratamento de erros adequado' em TaskScheduler.enqueue_export
02782. [x] app\services\task_scheduler.py:19 — revisar facet 'sem comentários inline desnecessários' em TaskScheduler.enqueue_export
02783. [x] app\services\task_scheduler.py:19 — revisar facet 'não imprime side-effects na UI/IO' em TaskScheduler.enqueue_export
02784. [x] app\services\task_scheduler.py:19 — revisar facet 'thread-safety revisada' em TaskScheduler.enqueue_export
02785. [x] app\services\task_scheduler.py:19 — revisar facet 'performance (sem loops O(n^2))' em TaskScheduler.enqueue_export
02786. [x] app\services\task_scheduler.py:19 — revisar facet 'coberto por testes' em TaskScheduler.enqueue_export
02787. [x] app\services\task_scheduler.py:22 — return em TaskScheduler.enqueue_export
02788. [x] app\services\task_scheduler.py:28 — definir/revisar FunctionDef: TaskScheduler.claim_next
02789. [x] app\services\task_scheduler.py:28 — revisar facet 'assinatura/args consistentes' em TaskScheduler.claim_next
02790. [x] app\services\task_scheduler.py:28 — revisar facet 'docstring em português' em TaskScheduler.claim_next
02791. [x] app\services\task_scheduler.py:28 — revisar facet 'nomenclatura clara (PEP8)' em TaskScheduler.claim_next
02792. [x] app\services\task_scheduler.py:28 — revisar facet 'type hints presentes' em TaskScheduler.claim_next
02793. [x] app\services\task_scheduler.py:28 — revisar facet 'tratamento de erros adequado' em TaskScheduler.claim_next
02794. [x] app\services\task_scheduler.py:28 — revisar facet 'sem comentários inline desnecessários' em TaskScheduler.claim_next
02795. [x] app\services\task_scheduler.py:28 — revisar facet 'não imprime side-effects na UI/IO' em TaskScheduler.claim_next
02796. [x] app\services\task_scheduler.py:28 — revisar facet 'thread-safety revisada' em TaskScheduler.claim_next
02797. [x] app\services\task_scheduler.py:28 — revisar facet 'performance (sem loops O(n^2))' em TaskScheduler.claim_next
02798. [x] app\services\task_scheduler.py:28 — revisar facet 'coberto por testes' em TaskScheduler.claim_next
02799. [x] app\services\task_scheduler.py:29 — atribuição: TaskScheduler.claim_next ← task
02800. [x] app\services\task_scheduler.py:30 — controle if em TaskScheduler.claim_next
02801. [x] app\services\task_scheduler.py:32 — return em TaskScheduler.claim_next
02802. [x] app\services\task_scheduler.py:34 — definir/revisar FunctionDef: TaskScheduler.execute
02803. [x] app\services\task_scheduler.py:34 — revisar facet 'assinatura/args consistentes' em TaskScheduler.execute
02804. [x] app\services\task_scheduler.py:34 — revisar facet 'docstring em português' em TaskScheduler.execute
02805. [x] app\services\task_scheduler.py:34 — revisar facet 'nomenclatura clara (PEP8)' em TaskScheduler.execute
02806. [x] app\services\task_scheduler.py:34 — revisar facet 'type hints presentes' em TaskScheduler.execute
02807. [x] app\services\task_scheduler.py:34 — revisar facet 'tratamento de erros adequado' em TaskScheduler.execute
02808. [x] app\services\task_scheduler.py:34 — revisar facet 'sem comentários inline desnecessários' em TaskScheduler.execute
02809. [x] app\services\task_scheduler.py:34 — revisar facet 'não imprime side-effects na UI/IO' em TaskScheduler.execute
02810. [x] app\services\task_scheduler.py:34 — revisar facet 'thread-safety revisada' em TaskScheduler.execute
02811. [x] app\services\task_scheduler.py:34 — revisar facet 'performance (sem loops O(n^2))' em TaskScheduler.execute
02812. [x] app\services\task_scheduler.py:34 — revisar facet 'coberto por testes' em TaskScheduler.execute
02813. [x] app\services\task_scheduler.py:41 — controle if em TaskScheduler.execute
02814. [x] app\services\task_scheduler.py:44 — raise em TaskScheduler.execute
02815. [x] app\services\task_scheduler.py:46 — definir/revisar FunctionDef: TaskScheduler._run_export
02816. [x] app\services\task_scheduler.py:46 — revisar facet 'assinatura/args consistentes' em TaskScheduler._run_export
02817. [x] app\services\task_scheduler.py:46 — revisar facet 'docstring em português' em TaskScheduler._run_export
02818. [x] app\services\task_scheduler.py:46 — revisar facet 'nomenclatura clara (PEP8)' em TaskScheduler._run_export
02819. [x] app\services\task_scheduler.py:46 — revisar facet 'type hints presentes' em TaskScheduler._run_export
02820. [x] app\services\task_scheduler.py:46 — revisar facet 'tratamento de erros adequado' em TaskScheduler._run_export
02821. [x] app\services\task_scheduler.py:46 — revisar facet 'sem comentários inline desnecessários' em TaskScheduler._run_export
02822. [x] app\services\task_scheduler.py:46 — revisar facet 'não imprime side-effects na UI/IO' em TaskScheduler._run_export
02823. [x] app\services\task_scheduler.py:46 — revisar facet 'thread-safety revisada' em TaskScheduler._run_export
02824. [x] app\services\task_scheduler.py:46 — revisar facet 'performance (sem loops O(n^2))' em TaskScheduler._run_export
02825. [x] app\services\task_scheduler.py:46 — revisar facet 'coberto por testes' em TaskScheduler._run_export
02826. [x] app\services\task_scheduler.py:47 — atribuição: TaskScheduler._run_export ← payload
02827. [x] app\services\task_scheduler.py:48 — atribuição: TaskScheduler._run_export ← start
02828. [x] app\services\task_scheduler.py:62 — definir/revisar FunctionDef: TaskScheduler.persist_cursor
02829. [x] app\services\task_scheduler.py:62 — revisar facet 'assinatura/args consistentes' em TaskScheduler.persist_cursor
02830. [x] app\services\task_scheduler.py:62 — revisar facet 'docstring em português' em TaskScheduler.persist_cursor
02831. [x] app\services\task_scheduler.py:62 — revisar facet 'nomenclatura clara (PEP8)' em TaskScheduler.persist_cursor
02832. [x] app\services\task_scheduler.py:62 — revisar facet 'type hints presentes' em TaskScheduler.persist_cursor
02833. [x] app\services\task_scheduler.py:62 — revisar facet 'tratamento de erros adequado' em TaskScheduler.persist_cursor
02834. [x] app\services\task_scheduler.py:62 — revisar facet 'sem comentários inline desnecessários' em TaskScheduler.persist_cursor
02835. [x] app\services\task_scheduler.py:62 — revisar facet 'não imprime side-effects na UI/IO' em TaskScheduler.persist_cursor
02836. [x] app\services\task_scheduler.py:62 — revisar facet 'thread-safety revisada' em TaskScheduler.persist_cursor
02837. [x] app\services\task_scheduler.py:62 — revisar facet 'performance (sem loops O(n^2))' em TaskScheduler.persist_cursor
02838. [x] app\services\task_scheduler.py:62 — revisar facet 'coberto por testes' em TaskScheduler.persist_cursor
02839. [x] app\services\task_scheduler.py:63 — atribuição: TaskScheduler.persist_cursor ← task
02840. [x] app\services\task_scheduler.py:64 — controle if em TaskScheduler.persist_cursor
02841. [x] app\services\task_scheduler.py:67 — definir/revisar FunctionDef: TaskScheduler.mark_completed
02842. [x] app\services\task_scheduler.py:67 — revisar facet 'assinatura/args consistentes' em TaskScheduler.mark_completed
02843. [x] app\services\task_scheduler.py:67 — revisar facet 'docstring em português' em TaskScheduler.mark_completed
02844. [x] app\services\task_scheduler.py:67 — revisar facet 'nomenclatura clara (PEP8)' em TaskScheduler.mark_completed
02845. [x] app\services\task_scheduler.py:67 — revisar facet 'type hints presentes' em TaskScheduler.mark_completed
02846. [x] app\services\task_scheduler.py:67 — revisar facet 'tratamento de erros adequado' em TaskScheduler.mark_completed
02847. [x] app\services\task_scheduler.py:67 — revisar facet 'sem comentários inline desnecessários' em TaskScheduler.mark_completed
02848. [x] app\services\task_scheduler.py:67 — revisar facet 'não imprime side-effects na UI/IO' em TaskScheduler.mark_completed
02849. [x] app\services\task_scheduler.py:67 — revisar facet 'thread-safety revisada' em TaskScheduler.mark_completed
02850. [x] app\services\task_scheduler.py:67 — revisar facet 'performance (sem loops O(n^2))' em TaskScheduler.mark_completed
02851. [x] app\services\task_scheduler.py:67 — revisar facet 'coberto por testes' em TaskScheduler.mark_completed
02852. [x] app\services\task_scheduler.py:70 — definir/revisar FunctionDef: TaskScheduler.mark_failed
02853. [x] app\services\task_scheduler.py:70 — revisar facet 'assinatura/args consistentes' em TaskScheduler.mark_failed
02854. [x] app\services\task_scheduler.py:70 — revisar facet 'docstring em português' em TaskScheduler.mark_failed
02855. [x] app\services\task_scheduler.py:70 — revisar facet 'nomenclatura clara (PEP8)' em TaskScheduler.mark_failed
02856. [x] app\services\task_scheduler.py:70 — revisar facet 'type hints presentes' em TaskScheduler.mark_failed
02857. [x] app\services\task_scheduler.py:70 — revisar facet 'tratamento de erros adequado' em TaskScheduler.mark_failed
02858. [x] app\services\task_scheduler.py:70 — revisar facet 'sem comentários inline desnecessários' em TaskScheduler.mark_failed
02859. [x] app\services\task_scheduler.py:70 — revisar facet 'não imprime side-effects na UI/IO' em TaskScheduler.mark_failed
02860. [x] app\services\task_scheduler.py:70 — revisar facet 'thread-safety revisada' em TaskScheduler.mark_failed
02861. [x] app\services\task_scheduler.py:70 — revisar facet 'performance (sem loops O(n^2))' em TaskScheduler.mark_failed
02862. [x] app\services\task_scheduler.py:70 — revisar facet 'coberto por testes' em TaskScheduler.mark_failed
02863. [x] app\services\task_scheduler.py:73 — definir/revisar FunctionDef: TaskScheduler.pause
02864. [x] app\services\task_scheduler.py:73 — revisar facet 'assinatura/args consistentes' em TaskScheduler.pause
02865. [x] app\services\task_scheduler.py:73 — revisar facet 'docstring em português' em TaskScheduler.pause
02866. [x] app\services\task_scheduler.py:73 — revisar facet 'nomenclatura clara (PEP8)' em TaskScheduler.pause
02867. [x] app\services\task_scheduler.py:73 — revisar facet 'type hints presentes' em TaskScheduler.pause
02868. [x] app\services\task_scheduler.py:73 — revisar facet 'tratamento de erros adequado' em TaskScheduler.pause
02869. [x] app\services\task_scheduler.py:73 — revisar facet 'sem comentários inline desnecessários' em TaskScheduler.pause
02870. [x] app\services\task_scheduler.py:73 — revisar facet 'não imprime side-effects na UI/IO' em TaskScheduler.pause
02871. [x] app\services\task_scheduler.py:73 — revisar facet 'thread-safety revisada' em TaskScheduler.pause
02872. [x] app\services\task_scheduler.py:73 — revisar facet 'performance (sem loops O(n^2))' em TaskScheduler.pause
02873. [x] app\services\task_scheduler.py:73 — revisar facet 'coberto por testes' em TaskScheduler.pause
02874. [x] app\services\task_scheduler.py:76 — definir/revisar FunctionDef: TaskScheduler.resume
02875. [x] app\services\task_scheduler.py:76 — revisar facet 'assinatura/args consistentes' em TaskScheduler.resume
02876. [x] app\services\task_scheduler.py:76 — revisar facet 'docstring em português' em TaskScheduler.resume
02877. [x] app\services\task_scheduler.py:76 — revisar facet 'nomenclatura clara (PEP8)' em TaskScheduler.resume
02878. [x] app\services\task_scheduler.py:76 — revisar facet 'type hints presentes' em TaskScheduler.resume
02879. [x] app\services\task_scheduler.py:76 — revisar facet 'tratamento de erros adequado' em TaskScheduler.resume
02880. [x] app\services\task_scheduler.py:76 — revisar facet 'sem comentários inline desnecessários' em TaskScheduler.resume
02881. [x] app\services\task_scheduler.py:76 — revisar facet 'não imprime side-effects na UI/IO' em TaskScheduler.resume
02882. [x] app\services\task_scheduler.py:76 — revisar facet 'thread-safety revisada' em TaskScheduler.resume
02883. [x] app\services\task_scheduler.py:76 — revisar facet 'performance (sem loops O(n^2))' em TaskScheduler.resume
02884. [x] app\services\task_scheduler.py:76 — revisar facet 'coberto por testes' em TaskScheduler.resume
02885. [x] app\services\task_scheduler.py:79 — definir/revisar FunctionDef: TaskScheduler.state_of
02886. [x] app\services\task_scheduler.py:79 — revisar facet 'assinatura/args consistentes' em TaskScheduler.state_of
02887. [x] app\services\task_scheduler.py:79 — revisar facet 'docstring em português' em TaskScheduler.state_of
02888. [x] app\services\task_scheduler.py:79 — revisar facet 'nomenclatura clara (PEP8)' em TaskScheduler.state_of
02889. [x] app\services\task_scheduler.py:79 — revisar facet 'type hints presentes' em TaskScheduler.state_of
02890. [x] app\services\task_scheduler.py:79 — revisar facet 'tratamento de erros adequado' em TaskScheduler.state_of
02891. [x] app\services\task_scheduler.py:79 — revisar facet 'sem comentários inline desnecessários' em TaskScheduler.state_of
02892. [x] app\services\task_scheduler.py:79 — revisar facet 'não imprime side-effects na UI/IO' em TaskScheduler.state_of
02893. [x] app\services\task_scheduler.py:79 — revisar facet 'thread-safety revisada' em TaskScheduler.state_of
02894. [x] app\services\task_scheduler.py:79 — revisar facet 'performance (sem loops O(n^2))' em TaskScheduler.state_of
02895. [x] app\services\task_scheduler.py:79 — revisar facet 'coberto por testes' em TaskScheduler.state_of
02896. [x] app\services\task_scheduler.py:80 — atribuição: TaskScheduler.state_of ← task
02897. [x] app\services\task_scheduler.py:81 — return em TaskScheduler.state_of
02898. [x] Existência e estrutura do módulo: app\services\template_service.py
02899. [x] app\services\template_service.py:3 — import: __future__
02900. [x] app\services\template_service.py:5 — import: difflib
02901. [x] app\services\template_service.py:6 — import: typing
02902. [x] app\services\template_service.py:8 — import: app.infrastructure.template_repository
02903. [x] app\services\template_service.py:11 — definir/revisar ClassDef: TemplateService
02904. [x] app\services\template_service.py:12 — definir/revisar FunctionDef: TemplateService.__init__
02905. [x] app\services\template_service.py:12 — revisar facet 'assinatura/args consistentes' em TemplateService.__init__
02906. [x] app\services\template_service.py:12 — revisar facet 'docstring em português' em TemplateService.__init__
02907. [x] app\services\template_service.py:12 — revisar facet 'nomenclatura clara (PEP8)' em TemplateService.__init__
02908. [x] app\services\template_service.py:12 — revisar facet 'type hints presentes' em TemplateService.__init__
02909. [x] app\services\template_service.py:12 — revisar facet 'tratamento de erros adequado' em TemplateService.__init__
02910. [x] app\services\template_service.py:12 — revisar facet 'sem comentários inline desnecessários' em TemplateService.__init__
02911. [x] app\services\template_service.py:12 — revisar facet 'não imprime side-effects na UI/IO' em TemplateService.__init__
02912. [x] app\services\template_service.py:12 — revisar facet 'thread-safety revisada' em TemplateService.__init__
02913. [x] app\services\template_service.py:12 — revisar facet 'performance (sem loops O(n^2))' em TemplateService.__init__
02914. [x] app\services\template_service.py:12 — revisar facet 'coberto por testes' em TemplateService.__init__
02915. [x] app\services\template_service.py:13 — atribuição: TemplateService.__init__ ← ?
02916. [x] app\services\template_service.py:15 — definir/revisar FunctionDef: TemplateService.save
02917. [x] app\services\template_service.py:15 — revisar facet 'assinatura/args consistentes' em TemplateService.save
02918. [x] app\services\template_service.py:15 — revisar facet 'docstring em português' em TemplateService.save
02919. [x] app\services\template_service.py:15 — revisar facet 'nomenclatura clara (PEP8)' em TemplateService.save
02920. [x] app\services\template_service.py:15 — revisar facet 'type hints presentes' em TemplateService.save
02921. [x] app\services\template_service.py:15 — revisar facet 'tratamento de erros adequado' em TemplateService.save
02922. [x] app\services\template_service.py:15 — revisar facet 'sem comentários inline desnecessários' em TemplateService.save
02923. [x] app\services\template_service.py:15 — revisar facet 'não imprime side-effects na UI/IO' em TemplateService.save
02924. [x] app\services\template_service.py:15 — revisar facet 'thread-safety revisada' em TemplateService.save
02925. [x] app\services\template_service.py:15 — revisar facet 'performance (sem loops O(n^2))' em TemplateService.save
02926. [x] app\services\template_service.py:15 — revisar facet 'coberto por testes' em TemplateService.save
02927. [x] app\services\template_service.py:16 — return em TemplateService.save
02928. [x] app\services\template_service.py:18 — definir/revisar FunctionDef: TemplateService.diff
02929. [x] app\services\template_service.py:18 — revisar facet 'assinatura/args consistentes' em TemplateService.diff
02930. [x] app\services\template_service.py:18 — revisar facet 'docstring em português' em TemplateService.diff
02931. [x] app\services\template_service.py:18 — revisar facet 'nomenclatura clara (PEP8)' em TemplateService.diff
02932. [x] app\services\template_service.py:18 — revisar facet 'type hints presentes' em TemplateService.diff
02933. [x] app\services\template_service.py:18 — revisar facet 'tratamento de erros adequado' em TemplateService.diff
02934. [x] app\services\template_service.py:18 — revisar facet 'sem comentários inline desnecessários' em TemplateService.diff
02935. [x] app\services\template_service.py:18 — revisar facet 'não imprime side-effects na UI/IO' em TemplateService.diff
02936. [x] app\services\template_service.py:18 — revisar facet 'thread-safety revisada' em TemplateService.diff
02937. [x] app\services\template_service.py:18 — revisar facet 'performance (sem loops O(n^2))' em TemplateService.diff
02938. [x] app\services\template_service.py:18 — revisar facet 'coberto por testes' em TemplateService.diff
02939. [x] app\services\template_service.py:19 — atribuição: TemplateService.diff ← a
02940. [x] app\services\template_service.py:20 — atribuição: TemplateService.diff ← b
02941. [x] app\services\template_service.py:21 — controle if em TemplateService.diff
02942. [x] app\services\template_service.py:22 — return em TemplateService.diff
02943. [x] app\services\template_service.py:23 — return em TemplateService.diff
02944. [x] app\services\template_service.py:32 — definir/revisar FunctionDef: TemplateService.restore
02945. [x] app\services\template_service.py:32 — revisar facet 'assinatura/args consistentes' em TemplateService.restore
02946. [x] app\services\template_service.py:32 — revisar facet 'docstring em português' em TemplateService.restore
02947. [x] app\services\template_service.py:32 — revisar facet 'nomenclatura clara (PEP8)' em TemplateService.restore
02948. [x] app\services\template_service.py:32 — revisar facet 'type hints presentes' em TemplateService.restore
02949. [x] app\services\template_service.py:32 — revisar facet 'tratamento de erros adequado' em TemplateService.restore
02950. [x] app\services\template_service.py:32 — revisar facet 'sem comentários inline desnecessários' em TemplateService.restore
02951. [x] app\services\template_service.py:32 — revisar facet 'não imprime side-effects na UI/IO' em TemplateService.restore
02952. [x] app\services\template_service.py:32 — revisar facet 'thread-safety revisada' em TemplateService.restore
02953. [x] app\services\template_service.py:32 — revisar facet 'performance (sem loops O(n^2))' em TemplateService.restore
02954. [x] app\services\template_service.py:32 — revisar facet 'coberto por testes' em TemplateService.restore
02955. [x] app\services\template_service.py:34 — atribuição: TemplateService.restore ← old
02956. [x] app\services\template_service.py:35 — controle if em TemplateService.restore
02957. [x] app\services\template_service.py:36 — raise em TemplateService.restore
02958. [x] app\services\template_service.py:37 — return em TemplateService.restore
02959. [x] Existência e estrutura do módulo: app\ui\__init__.py
02960. [x] Existência e estrutura do módulo: app\ui\editor\__init__.py
02961. [x] app\ui\editor\__init__.py:3 — import: app.ui.editor.code_editor
02962. [x] app\ui\editor\__init__.py:4 — import: app.ui.editor.editor_tabs
02963. [x] app\ui\editor\__init__.py:5 — import: app.ui.editor.editor_widget
02964. [x] app\ui\editor\__init__.py:6 — import: app.ui.editor.find_replace_bar
02965. [x] app\ui\editor\__init__.py:7 — import: app.ui.editor.highlighter
02966. [x] app\ui\editor\__init__.py:9 — atribuição:  ← __all__
02967. [x] Existência e estrutura do módulo: app\ui\editor\code_editor.py
02968. [x] app\ui\editor\code_editor.py:3 — import: __future__
02969. [x] app\ui\editor\code_editor.py:5 — import: PySide6.QtCore
02970. [x] app\ui\editor\code_editor.py:6 — import: PySide6.QtGui
02971. [x] app\ui\editor\code_editor.py:14 — import: PySide6.QtWidgets
02972. [x] app\ui\editor\code_editor.py:17 — definir/revisar ClassDef: _LineNumberArea
02973. [x] app\ui\editor\code_editor.py:18 — definir/revisar FunctionDef: _LineNumberArea.__init__
02974. [x] app\ui\editor\code_editor.py:18 — revisar facet 'assinatura/args consistentes' em _LineNumberArea.__init__
02975. [x] app\ui\editor\code_editor.py:18 — revisar facet 'docstring em português' em _LineNumberArea.__init__
02976. [x] app\ui\editor\code_editor.py:18 — revisar facet 'nomenclatura clara (PEP8)' em _LineNumberArea.__init__
02977. [x] app\ui\editor\code_editor.py:18 — revisar facet 'type hints presentes' em _LineNumberArea.__init__
02978. [x] app\ui\editor\code_editor.py:18 — revisar facet 'tratamento de erros adequado' em _LineNumberArea.__init__
02979. [x] app\ui\editor\code_editor.py:18 — revisar facet 'sem comentários inline desnecessários' em _LineNumberArea.__init__
02980. [x] app\ui\editor\code_editor.py:18 — revisar facet 'não imprime side-effects na UI/IO' em _LineNumberArea.__init__
02981. [x] app\ui\editor\code_editor.py:18 — revisar facet 'thread-safety revisada' em _LineNumberArea.__init__
02982. [x] app\ui\editor\code_editor.py:18 — revisar facet 'performance (sem loops O(n^2))' em _LineNumberArea.__init__
02983. [x] app\ui\editor\code_editor.py:18 — revisar facet 'coberto por testes' em _LineNumberArea.__init__
02984. [x] app\ui\editor\code_editor.py:20 — atribuição: _LineNumberArea.__init__ ← ?
02985. [x] app\ui\editor\code_editor.py:22 — definir/revisar FunctionDef: _LineNumberArea.sizeHint
02986. [x] app\ui\editor\code_editor.py:22 — revisar facet 'assinatura/args consistentes' em _LineNumberArea.sizeHint
02987. [x] app\ui\editor\code_editor.py:22 — revisar facet 'docstring em português' em _LineNumberArea.sizeHint
02988. [x] app\ui\editor\code_editor.py:22 — revisar facet 'nomenclatura clara (PEP8)' em _LineNumberArea.sizeHint
02989. [x] app\ui\editor\code_editor.py:22 — revisar facet 'type hints presentes' em _LineNumberArea.sizeHint
02990. [x] app\ui\editor\code_editor.py:22 — revisar facet 'tratamento de erros adequado' em _LineNumberArea.sizeHint
02991. [x] app\ui\editor\code_editor.py:22 — revisar facet 'sem comentários inline desnecessários' em _LineNumberArea.sizeHint
02992. [x] app\ui\editor\code_editor.py:22 — revisar facet 'não imprime side-effects na UI/IO' em _LineNumberArea.sizeHint
02993. [x] app\ui\editor\code_editor.py:22 — revisar facet 'thread-safety revisada' em _LineNumberArea.sizeHint
02994. [x] app\ui\editor\code_editor.py:22 — revisar facet 'performance (sem loops O(n^2))' em _LineNumberArea.sizeHint
02995. [x] app\ui\editor\code_editor.py:22 — revisar facet 'coberto por testes' em _LineNumberArea.sizeHint
02996. [x] app\ui\editor\code_editor.py:23 — return em _LineNumberArea.sizeHint
02997. [x] app\ui\editor\code_editor.py:25 — definir/revisar FunctionDef: _LineNumberArea.paintEvent
02998. [x] app\ui\editor\code_editor.py:25 — revisar facet 'assinatura/args consistentes' em _LineNumberArea.paintEvent
02999. [x] app\ui\editor\code_editor.py:25 — revisar facet 'docstring em português' em _LineNumberArea.paintEvent
03000. [x] app\ui\editor\code_editor.py:25 — revisar facet 'nomenclatura clara (PEP8)' em _LineNumberArea.paintEvent
03001. [x] app\ui\editor\code_editor.py:25 — revisar facet 'type hints presentes' em _LineNumberArea.paintEvent
03002. [x] app\ui\editor\code_editor.py:25 — revisar facet 'tratamento de erros adequado' em _LineNumberArea.paintEvent
03003. [x] app\ui\editor\code_editor.py:25 — revisar facet 'sem comentários inline desnecessários' em _LineNumberArea.paintEvent
03004. [x] app\ui\editor\code_editor.py:25 — revisar facet 'não imprime side-effects na UI/IO' em _LineNumberArea.paintEvent
03005. [x] app\ui\editor\code_editor.py:25 — revisar facet 'thread-safety revisada' em _LineNumberArea.paintEvent
03006. [x] app\ui\editor\code_editor.py:25 — revisar facet 'performance (sem loops O(n^2))' em _LineNumberArea.paintEvent
03007. [x] app\ui\editor\code_editor.py:25 — revisar facet 'coberto por testes' em _LineNumberArea.paintEvent
03008. [x] app\ui\editor\code_editor.py:29 — definir/revisar ClassDef: CodeEditor
03009. [x] app\ui\editor\code_editor.py:30 — atribuição: CodeEditor ← BASE_FONT_SIZE
03010. [x] app\ui\editor\code_editor.py:32 — definir/revisar FunctionDef: CodeEditor.__init__
03011. [x] app\ui\editor\code_editor.py:32 — revisar facet 'assinatura/args consistentes' em CodeEditor.__init__
03012. [x] app\ui\editor\code_editor.py:32 — revisar facet 'docstring em português' em CodeEditor.__init__
03013. [x] app\ui\editor\code_editor.py:32 — revisar facet 'nomenclatura clara (PEP8)' em CodeEditor.__init__
03014. [x] app\ui\editor\code_editor.py:32 — revisar facet 'type hints presentes' em CodeEditor.__init__
03015. [x] app\ui\editor\code_editor.py:32 — revisar facet 'tratamento de erros adequado' em CodeEditor.__init__
03016. [x] app\ui\editor\code_editor.py:32 — revisar facet 'sem comentários inline desnecessários' em CodeEditor.__init__
03017. [x] app\ui\editor\code_editor.py:32 — revisar facet 'não imprime side-effects na UI/IO' em CodeEditor.__init__
03018. [x] app\ui\editor\code_editor.py:32 — revisar facet 'thread-safety revisada' em CodeEditor.__init__
03019. [x] app\ui\editor\code_editor.py:32 — revisar facet 'performance (sem loops O(n^2))' em CodeEditor.__init__
03020. [x] app\ui\editor\code_editor.py:32 — revisar facet 'coberto por testes' em CodeEditor.__init__
03021. [x] app\ui\editor\code_editor.py:34 — import: app.ui.editor.themes
03022. [x] app\ui\editor\code_editor.py:36 — atribuição: CodeEditor.__init__ ← ?
03023. [x] app\ui\editor\code_editor.py:37 — atribuição: CodeEditor.__init__ ← ?
03024. [x] app\ui\editor\code_editor.py:38 — atribuição: CodeEditor.__init__ ← ?
03025. [x] app\ui\editor\code_editor.py:40 — atribuição: CodeEditor.__init__ ← font
03026. [x] app\ui\editor\code_editor.py:47 — atribuição: CodeEditor.__init__ ← ?
03027. [x] app\ui\editor\code_editor.py:56 — definir/revisar FunctionDef: CodeEditor.apply_theme
03028. [x] app\ui\editor\code_editor.py:56 — revisar facet 'assinatura/args consistentes' em CodeEditor.apply_theme
03029. [x] app\ui\editor\code_editor.py:56 — revisar facet 'docstring em português' em CodeEditor.apply_theme
03030. [x] app\ui\editor\code_editor.py:56 — revisar facet 'nomenclatura clara (PEP8)' em CodeEditor.apply_theme
03031. [x] app\ui\editor\code_editor.py:56 — revisar facet 'type hints presentes' em CodeEditor.apply_theme
03032. [x] app\ui\editor\code_editor.py:56 — revisar facet 'tratamento de erros adequado' em CodeEditor.apply_theme
03033. [x] app\ui\editor\code_editor.py:56 — revisar facet 'sem comentários inline desnecessários' em CodeEditor.apply_theme
03034. [x] app\ui\editor\code_editor.py:56 — revisar facet 'não imprime side-effects na UI/IO' em CodeEditor.apply_theme
03035. [x] app\ui\editor\code_editor.py:56 — revisar facet 'thread-safety revisada' em CodeEditor.apply_theme
03036. [x] app\ui\editor\code_editor.py:56 — revisar facet 'performance (sem loops O(n^2))' em CodeEditor.apply_theme
03037. [x] app\ui\editor\code_editor.py:56 — revisar facet 'coberto por testes' em CodeEditor.apply_theme
03038. [x] app\ui\editor\code_editor.py:57 — import: app.ui.editor.themes
03039. [x] app\ui\editor\code_editor.py:59 — atribuição: CodeEditor.apply_theme ← ?
03040. [x] app\ui\editor\code_editor.py:60 — atribuição: CodeEditor.apply_theme ← ?
03041. [x] app\ui\editor\code_editor.py:61 — atribuição: CodeEditor.apply_theme ← colors
03042. [x] app\ui\editor\code_editor.py:63 — atribuição: CodeEditor.apply_theme ← palette
03043. [x] app\ui\editor\code_editor.py:64 — import: PySide6.QtGui
03044. [x] app\ui\editor\code_editor.py:79 — definir/revisar FunctionDef: CodeEditor._apply_editor_font
03045. [x] app\ui\editor\code_editor.py:79 — revisar facet 'assinatura/args consistentes' em CodeEditor._apply_editor_font
03046. [x] app\ui\editor\code_editor.py:79 — revisar facet 'docstring em português' em CodeEditor._apply_editor_font
03047. [x] app\ui\editor\code_editor.py:79 — revisar facet 'nomenclatura clara (PEP8)' em CodeEditor._apply_editor_font
03048. [x] app\ui\editor\code_editor.py:79 — revisar facet 'type hints presentes' em CodeEditor._apply_editor_font
03049. [x] app\ui\editor\code_editor.py:79 — revisar facet 'tratamento de erros adequado' em CodeEditor._apply_editor_font
03050. [x] app\ui\editor\code_editor.py:79 — revisar facet 'sem comentários inline desnecessários' em CodeEditor._apply_editor_font
03051. [x] app\ui\editor\code_editor.py:79 — revisar facet 'não imprime side-effects na UI/IO' em CodeEditor._apply_editor_font
03052. [x] app\ui\editor\code_editor.py:79 — revisar facet 'thread-safety revisada' em CodeEditor._apply_editor_font
03053. [x] app\ui\editor\code_editor.py:79 — revisar facet 'performance (sem loops O(n^2))' em CodeEditor._apply_editor_font
03054. [x] app\ui\editor\code_editor.py:79 — revisar facet 'coberto por testes' em CodeEditor._apply_editor_font
03055. [x] app\ui\editor\code_editor.py:80 — import: app.ui.editor.themes
03056. [x] app\ui\editor\code_editor.py:82 — atribuição: CodeEditor._apply_editor_font ← size
03057. [x] app\ui\editor\code_editor.py:83 — controle if em CodeEditor._apply_editor_font
03058. [x] app\ui\editor\code_editor.py:84 — return em CodeEditor._apply_editor_font
03059. [x] app\ui\editor\code_editor.py:85 — atribuição: CodeEditor._apply_editor_font ← font
03060. [x] app\ui\editor\code_editor.py:91 — definir/revisar FunctionDef: CodeEditor.zoom
03061. [x] app\ui\editor\code_editor.py:91 — revisar facet 'assinatura/args consistentes' em CodeEditor.zoom
03062. [x] app\ui\editor\code_editor.py:91 — revisar facet 'docstring em português' em CodeEditor.zoom
03063. [x] app\ui\editor\code_editor.py:91 — revisar facet 'nomenclatura clara (PEP8)' em CodeEditor.zoom
03064. [x] app\ui\editor\code_editor.py:91 — revisar facet 'type hints presentes' em CodeEditor.zoom
03065. [x] app\ui\editor\code_editor.py:91 — revisar facet 'tratamento de erros adequado' em CodeEditor.zoom
03066. [x] app\ui\editor\code_editor.py:91 — revisar facet 'sem comentários inline desnecessários' em CodeEditor.zoom
03067. [x] app\ui\editor\code_editor.py:91 — revisar facet 'não imprime side-effects na UI/IO' em CodeEditor.zoom
03068. [x] app\ui\editor\code_editor.py:91 — revisar facet 'thread-safety revisada' em CodeEditor.zoom
03069. [x] app\ui\editor\code_editor.py:91 — revisar facet 'performance (sem loops O(n^2))' em CodeEditor.zoom
03070. [x] app\ui\editor\code_editor.py:91 — revisar facet 'coberto por testes' em CodeEditor.zoom
03071. [x] app\ui\editor\code_editor.py:92 — import: app.ui.editor.themes
03072. [x] app\ui\editor\code_editor.py:94 — controle if em CodeEditor.zoom
03073. [x] app\ui\editor\code_editor.py:95 — atribuição: CodeEditor.zoom ← ?
03074. [x] app\ui\editor\code_editor.py:97 — atribuição: CodeEditor.zoom ← ?
03075. [x] app\ui\editor\code_editor.py:101 — definir/revisar FunctionDef: CodeEditor.zoom_reset
03076. [x] app\ui\editor\code_editor.py:101 — revisar facet 'assinatura/args consistentes' em CodeEditor.zoom_reset
03077. [x] app\ui\editor\code_editor.py:101 — revisar facet 'docstring em português' em CodeEditor.zoom_reset
03078. [x] app\ui\editor\code_editor.py:101 — revisar facet 'nomenclatura clara (PEP8)' em CodeEditor.zoom_reset
03079. [x] app\ui\editor\code_editor.py:101 — revisar facet 'type hints presentes' em CodeEditor.zoom_reset
03080. [x] app\ui\editor\code_editor.py:101 — revisar facet 'tratamento de erros adequado' em CodeEditor.zoom_reset
03081. [x] app\ui\editor\code_editor.py:101 — revisar facet 'sem comentários inline desnecessários' em CodeEditor.zoom_reset
03082. [x] app\ui\editor\code_editor.py:101 — revisar facet 'não imprime side-effects na UI/IO' em CodeEditor.zoom_reset
03083. [x] app\ui\editor\code_editor.py:101 — revisar facet 'thread-safety revisada' em CodeEditor.zoom_reset
03084. [x] app\ui\editor\code_editor.py:101 — revisar facet 'performance (sem loops O(n^2))' em CodeEditor.zoom_reset
03085. [x] app\ui\editor\code_editor.py:101 — revisar facet 'coberto por testes' em CodeEditor.zoom_reset
03086. [x] app\ui\editor\code_editor.py:102 — import: app.ui.editor.themes
03087. [x] app\ui\editor\code_editor.py:104 — atribuição: CodeEditor.zoom_reset ← ?
03088. [x] app\ui\editor\code_editor.py:109 — definir/revisar FunctionDef: CodeEditor.line_number_width
03089. [x] app\ui\editor\code_editor.py:109 — revisar facet 'assinatura/args consistentes' em CodeEditor.line_number_width
03090. [x] app\ui\editor\code_editor.py:109 — revisar facet 'docstring em português' em CodeEditor.line_number_width
03091. [x] app\ui\editor\code_editor.py:109 — revisar facet 'nomenclatura clara (PEP8)' em CodeEditor.line_number_width
03092. [x] app\ui\editor\code_editor.py:109 — revisar facet 'type hints presentes' em CodeEditor.line_number_width
03093. [x] app\ui\editor\code_editor.py:109 — revisar facet 'tratamento de erros adequado' em CodeEditor.line_number_width
03094. [x] app\ui\editor\code_editor.py:109 — revisar facet 'sem comentários inline desnecessários' em CodeEditor.line_number_width
03095. [x] app\ui\editor\code_editor.py:109 — revisar facet 'não imprime side-effects na UI/IO' em CodeEditor.line_number_width
03096. [x] app\ui\editor\code_editor.py:109 — revisar facet 'thread-safety revisada' em CodeEditor.line_number_width
03097. [x] app\ui\editor\code_editor.py:109 — revisar facet 'performance (sem loops O(n^2))' em CodeEditor.line_number_width
03098. [x] app\ui\editor\code_editor.py:109 — revisar facet 'coberto por testes' em CodeEditor.line_number_width
03099. [x] app\ui\editor\code_editor.py:110 — atribuição: CodeEditor.line_number_width ← digits
03100. [x] app\ui\editor\code_editor.py:111 — return em CodeEditor.line_number_width
03101. [x] app\ui\editor\code_editor.py:113 — definir/revisar FunctionDef: CodeEditor._update_area_width
03102. [x] app\ui\editor\code_editor.py:113 — revisar facet 'assinatura/args consistentes' em CodeEditor._update_area_width
03103. [x] app\ui\editor\code_editor.py:113 — revisar facet 'docstring em português' em CodeEditor._update_area_width
03104. [x] app\ui\editor\code_editor.py:113 — revisar facet 'nomenclatura clara (PEP8)' em CodeEditor._update_area_width
03105. [x] app\ui\editor\code_editor.py:113 — revisar facet 'type hints presentes' em CodeEditor._update_area_width
03106. [x] app\ui\editor\code_editor.py:113 — revisar facet 'tratamento de erros adequado' em CodeEditor._update_area_width
03107. [x] app\ui\editor\code_editor.py:113 — revisar facet 'sem comentários inline desnecessários' em CodeEditor._update_area_width
03108. [x] app\ui\editor\code_editor.py:113 — revisar facet 'não imprime side-effects na UI/IO' em CodeEditor._update_area_width
03109. [x] app\ui\editor\code_editor.py:113 — revisar facet 'thread-safety revisada' em CodeEditor._update_area_width
03110. [x] app\ui\editor\code_editor.py:113 — revisar facet 'performance (sem loops O(n^2))' em CodeEditor._update_area_width
03111. [x] app\ui\editor\code_editor.py:113 — revisar facet 'coberto por testes' em CodeEditor._update_area_width
03112. [x] app\ui\editor\code_editor.py:116 — definir/revisar FunctionDef: CodeEditor._update_area
03113. [x] app\ui\editor\code_editor.py:116 — revisar facet 'assinatura/args consistentes' em CodeEditor._update_area
03114. [x] app\ui\editor\code_editor.py:116 — revisar facet 'docstring em português' em CodeEditor._update_area
03115. [x] app\ui\editor\code_editor.py:116 — revisar facet 'nomenclatura clara (PEP8)' em CodeEditor._update_area
03116. [x] app\ui\editor\code_editor.py:116 — revisar facet 'type hints presentes' em CodeEditor._update_area
03117. [x] app\ui\editor\code_editor.py:116 — revisar facet 'tratamento de erros adequado' em CodeEditor._update_area
03118. [x] app\ui\editor\code_editor.py:116 — revisar facet 'sem comentários inline desnecessários' em CodeEditor._update_area
03119. [x] app\ui\editor\code_editor.py:116 — revisar facet 'não imprime side-effects na UI/IO' em CodeEditor._update_area
03120. [x] app\ui\editor\code_editor.py:116 — revisar facet 'thread-safety revisada' em CodeEditor._update_area
03121. [x] app\ui\editor\code_editor.py:116 — revisar facet 'performance (sem loops O(n^2))' em CodeEditor._update_area
03122. [x] app\ui\editor\code_editor.py:116 — revisar facet 'coberto por testes' em CodeEditor._update_area
03123. [x] app\ui\editor\code_editor.py:117 — controle if em CodeEditor._update_area
03124. [x] app\ui\editor\code_editor.py:121 — controle if em CodeEditor._update_area
03125. [x] app\ui\editor\code_editor.py:124 — definir/revisar FunctionDef: CodeEditor.resizeEvent
03126. [x] app\ui\editor\code_editor.py:124 — revisar facet 'assinatura/args consistentes' em CodeEditor.resizeEvent
03127. [x] app\ui\editor\code_editor.py:124 — revisar facet 'docstring em português' em CodeEditor.resizeEvent
03128. [x] app\ui\editor\code_editor.py:124 — revisar facet 'nomenclatura clara (PEP8)' em CodeEditor.resizeEvent
03129. [x] app\ui\editor\code_editor.py:124 — revisar facet 'type hints presentes' em CodeEditor.resizeEvent
03130. [x] app\ui\editor\code_editor.py:124 — revisar facet 'tratamento de erros adequado' em CodeEditor.resizeEvent
03131. [x] app\ui\editor\code_editor.py:124 — revisar facet 'sem comentários inline desnecessários' em CodeEditor.resizeEvent
03132. [x] app\ui\editor\code_editor.py:124 — revisar facet 'não imprime side-effects na UI/IO' em CodeEditor.resizeEvent
03133. [x] app\ui\editor\code_editor.py:124 — revisar facet 'thread-safety revisada' em CodeEditor.resizeEvent
03134. [x] app\ui\editor\code_editor.py:124 — revisar facet 'performance (sem loops O(n^2))' em CodeEditor.resizeEvent
03135. [x] app\ui\editor\code_editor.py:124 — revisar facet 'coberto por testes' em CodeEditor.resizeEvent
03136. [x] app\ui\editor\code_editor.py:126 — atribuição: CodeEditor.resizeEvent ← cr
03137. [x] app\ui\editor\code_editor.py:129 — definir/revisar FunctionDef: CodeEditor.paint_line_numbers
03138. [x] app\ui\editor\code_editor.py:129 — revisar facet 'assinatura/args consistentes' em CodeEditor.paint_line_numbers
03139. [x] app\ui\editor\code_editor.py:129 — revisar facet 'docstring em português' em CodeEditor.paint_line_numbers
03140. [x] app\ui\editor\code_editor.py:129 — revisar facet 'nomenclatura clara (PEP8)' em CodeEditor.paint_line_numbers
03141. [x] app\ui\editor\code_editor.py:129 — revisar facet 'type hints presentes' em CodeEditor.paint_line_numbers
03142. [x] app\ui\editor\code_editor.py:129 — revisar facet 'tratamento de erros adequado' em CodeEditor.paint_line_numbers
03143. [x] app\ui\editor\code_editor.py:129 — revisar facet 'sem comentários inline desnecessários' em CodeEditor.paint_line_numbers
03144. [x] app\ui\editor\code_editor.py:129 — revisar facet 'não imprime side-effects na UI/IO' em CodeEditor.paint_line_numbers
03145. [x] app\ui\editor\code_editor.py:129 — revisar facet 'thread-safety revisada' em CodeEditor.paint_line_numbers
03146. [x] app\ui\editor\code_editor.py:129 — revisar facet 'performance (sem loops O(n^2))' em CodeEditor.paint_line_numbers
03147. [x] app\ui\editor\code_editor.py:129 — revisar facet 'coberto por testes' em CodeEditor.paint_line_numbers
03148. [x] app\ui\editor\code_editor.py:130 — atribuição: CodeEditor.paint_line_numbers ← colors
03149. [x] app\ui\editor\code_editor.py:131 — atribuição: CodeEditor.paint_line_numbers ← painter
03150. [x] app\ui\editor\code_editor.py:134 — atribuição: CodeEditor.paint_line_numbers ← block
03151. [x] app\ui\editor\code_editor.py:135 — atribuição: CodeEditor.paint_line_numbers ← block_number
03152. [x] app\ui\editor\code_editor.py:136 — atribuição: CodeEditor.paint_line_numbers ← top
03153. [x] app\ui\editor\code_editor.py:137 — atribuição: CodeEditor.paint_line_numbers ← bottom
03154. [x] app\ui\editor\code_editor.py:138 — atribuição: CodeEditor.paint_line_numbers ← current
03155. [x] app\ui\editor\code_editor.py:141 — controle while em CodeEditor.paint_line_numbers
03156. [x] app\ui\editor\code_editor.py:142 — controle if em CodeEditor.paint_line_numbers
03157. [x] app\ui\editor\code_editor.py:143 — controle if em CodeEditor.paint_line_numbers
03158. [x] app\ui\editor\code_editor.py:150 — controle if em CodeEditor.paint_line_numbers
03159. [x] app\ui\editor\code_editor.py:152 — atribuição: CodeEditor.paint_line_numbers ← block
03160. [x] app\ui\editor\code_editor.py:153 — atribuição: CodeEditor.paint_line_numbers ← top
03161. [x] app\ui\editor\code_editor.py:154 — atribuição: CodeEditor.paint_line_numbers ← bottom
03162. [x] app\ui\editor\code_editor.py:157 — definir/revisar FunctionDef: CodeEditor._highlight_current
03163. [x] app\ui\editor\code_editor.py:157 — revisar facet 'assinatura/args consistentes' em CodeEditor._highlight_current
03164. [x] app\ui\editor\code_editor.py:157 — revisar facet 'docstring em português' em CodeEditor._highlight_current
03165. [x] app\ui\editor\code_editor.py:157 — revisar facet 'nomenclatura clara (PEP8)' em CodeEditor._highlight_current
03166. [x] app\ui\editor\code_editor.py:157 — revisar facet 'type hints presentes' em CodeEditor._highlight_current
03167. [x] app\ui\editor\code_editor.py:157 — revisar facet 'tratamento de erros adequado' em CodeEditor._highlight_current
03168. [x] app\ui\editor\code_editor.py:157 — revisar facet 'sem comentários inline desnecessários' em CodeEditor._highlight_current
03169. [x] app\ui\editor\code_editor.py:157 — revisar facet 'não imprime side-effects na UI/IO' em CodeEditor._highlight_current
03170. [x] app\ui\editor\code_editor.py:157 — revisar facet 'thread-safety revisada' em CodeEditor._highlight_current
03171. [x] app\ui\editor\code_editor.py:157 — revisar facet 'performance (sem loops O(n^2))' em CodeEditor._highlight_current
03172. [x] app\ui\editor\code_editor.py:157 — revisar facet 'coberto por testes' em CodeEditor._highlight_current
03173. [x] app\ui\editor\code_editor.py:158 — atribuição: CodeEditor._highlight_current ← sel
03174. [x] app\ui\editor\code_editor.py:161 — atribuição: CodeEditor._highlight_current ← ?
03175. [x] app\ui\editor\code_editor.py:166 — definir/revisar FunctionDef: CodeEditor.keyPressEvent
03176. [x] app\ui\editor\code_editor.py:166 — revisar facet 'assinatura/args consistentes' em CodeEditor.keyPressEvent
03177. [x] app\ui\editor\code_editor.py:166 — revisar facet 'docstring em português' em CodeEditor.keyPressEvent
03178. [x] app\ui\editor\code_editor.py:166 — revisar facet 'nomenclatura clara (PEP8)' em CodeEditor.keyPressEvent
03179. [x] app\ui\editor\code_editor.py:166 — revisar facet 'type hints presentes' em CodeEditor.keyPressEvent
03180. [x] app\ui\editor\code_editor.py:166 — revisar facet 'tratamento de erros adequado' em CodeEditor.keyPressEvent
03181. [x] app\ui\editor\code_editor.py:166 — revisar facet 'sem comentários inline desnecessários' em CodeEditor.keyPressEvent
03182. [x] app\ui\editor\code_editor.py:166 — revisar facet 'não imprime side-effects na UI/IO' em CodeEditor.keyPressEvent
03183. [x] app\ui\editor\code_editor.py:166 — revisar facet 'thread-safety revisada' em CodeEditor.keyPressEvent
03184. [x] app\ui\editor\code_editor.py:166 — revisar facet 'performance (sem loops O(n^2))' em CodeEditor.keyPressEvent
03185. [x] app\ui\editor\code_editor.py:166 — revisar facet 'coberto por testes' em CodeEditor.keyPressEvent
03186. [x] app\ui\editor\code_editor.py:167 — controle if em CodeEditor.keyPressEvent
03187. [x] app\ui\editor\code_editor.py:169 — return em CodeEditor.keyPressEvent
03188. [x] app\ui\editor\code_editor.py:170 — controle if em CodeEditor.keyPressEvent
03189. [x] app\ui\editor\code_editor.py:172 — return em CodeEditor.keyPressEvent
03190. [x] app\ui\editor\code_editor.py:173 — controle if em CodeEditor.keyPressEvent
03191. [x] app\ui\editor\code_editor.py:175 — return em CodeEditor.keyPressEvent
03192. [x] app\ui\editor\code_editor.py:176 — atribuição: CodeEditor.keyPressEvent ← ctrl
03193. [x] app\ui\editor\code_editor.py:177 — controle if em CodeEditor.keyPressEvent
03194. [x] app\ui\editor\code_editor.py:179 — return em CodeEditor.keyPressEvent
03195. [x] app\ui\editor\code_editor.py:180 — controle if em CodeEditor.keyPressEvent
03196. [x] app\ui\editor\code_editor.py:182 — return em CodeEditor.keyPressEvent
03197. [x] app\ui\editor\code_editor.py:183 — controle if em CodeEditor.keyPressEvent
03198. [x] app\ui\editor\code_editor.py:185 — return em CodeEditor.keyPressEvent
03199. [x] app\ui\editor\code_editor.py:188 — definir/revisar FunctionDef: CodeEditor.wheelEvent
03200. [x] app\ui\editor\code_editor.py:188 — revisar facet 'assinatura/args consistentes' em CodeEditor.wheelEvent
03201. [x] app\ui\editor\code_editor.py:188 — revisar facet 'docstring em português' em CodeEditor.wheelEvent
03202. [x] app\ui\editor\code_editor.py:188 — revisar facet 'nomenclatura clara (PEP8)' em CodeEditor.wheelEvent
03203. [x] app\ui\editor\code_editor.py:188 — revisar facet 'type hints presentes' em CodeEditor.wheelEvent
03204. [x] app\ui\editor\code_editor.py:188 — revisar facet 'tratamento de erros adequado' em CodeEditor.wheelEvent
03205. [x] app\ui\editor\code_editor.py:188 — revisar facet 'sem comentários inline desnecessários' em CodeEditor.wheelEvent
03206. [x] app\ui\editor\code_editor.py:188 — revisar facet 'não imprime side-effects na UI/IO' em CodeEditor.wheelEvent
03207. [x] app\ui\editor\code_editor.py:188 — revisar facet 'thread-safety revisada' em CodeEditor.wheelEvent
03208. [x] app\ui\editor\code_editor.py:188 — revisar facet 'performance (sem loops O(n^2))' em CodeEditor.wheelEvent
03209. [x] app\ui\editor\code_editor.py:188 — revisar facet 'coberto por testes' em CodeEditor.wheelEvent
03210. [x] app\ui\editor\code_editor.py:189 — controle if em CodeEditor.wheelEvent
03211. [x] app\ui\editor\code_editor.py:192 — return em CodeEditor.wheelEvent
03212. [x] app\ui\editor\code_editor.py:195 — definir/revisar FunctionDef: CodeEditor._auto_indent
03213. [x] app\ui\editor\code_editor.py:195 — revisar facet 'assinatura/args consistentes' em CodeEditor._auto_indent
03214. [x] app\ui\editor\code_editor.py:195 — revisar facet 'docstring em português' em CodeEditor._auto_indent
03215. [x] app\ui\editor\code_editor.py:195 — revisar facet 'nomenclatura clara (PEP8)' em CodeEditor._auto_indent
03216. [x] app\ui\editor\code_editor.py:195 — revisar facet 'type hints presentes' em CodeEditor._auto_indent
03217. [x] app\ui\editor\code_editor.py:195 — revisar facet 'tratamento de erros adequado' em CodeEditor._auto_indent
03218. [x] app\ui\editor\code_editor.py:195 — revisar facet 'sem comentários inline desnecessários' em CodeEditor._auto_indent
03219. [x] app\ui\editor\code_editor.py:195 — revisar facet 'não imprime side-effects na UI/IO' em CodeEditor._auto_indent
03220. [x] app\ui\editor\code_editor.py:195 — revisar facet 'thread-safety revisada' em CodeEditor._auto_indent
03221. [x] app\ui\editor\code_editor.py:195 — revisar facet 'performance (sem loops O(n^2))' em CodeEditor._auto_indent
03222. [x] app\ui\editor\code_editor.py:195 — revisar facet 'coberto por testes' em CodeEditor._auto_indent
03223. [x] app\ui\editor\code_editor.py:196 — atribuição: CodeEditor._auto_indent ← cursor
03224. [x] app\ui\editor\code_editor.py:197 — atribuição: CodeEditor._auto_indent ← line
03225. [x] app\ui\editor\code_editor.py:198 — atribuição: CodeEditor._auto_indent ← indent
03226. [x] app\ui\editor\code_editor.py:199 — atribuição: CodeEditor._auto_indent ← extra
03227. [x] app\ui\editor\code_editor.py:204 — definir/revisar FunctionDef: CodeEditor._indent_selection
03228. [x] app\ui\editor\code_editor.py:204 — revisar facet 'assinatura/args consistentes' em CodeEditor._indent_selection
03229. [x] app\ui\editor\code_editor.py:204 — revisar facet 'docstring em português' em CodeEditor._indent_selection
03230. [x] app\ui\editor\code_editor.py:204 — revisar facet 'nomenclatura clara (PEP8)' em CodeEditor._indent_selection
03231. [x] app\ui\editor\code_editor.py:204 — revisar facet 'type hints presentes' em CodeEditor._indent_selection
03232. [x] app\ui\editor\code_editor.py:204 — revisar facet 'tratamento de erros adequado' em CodeEditor._indent_selection
03233. [x] app\ui\editor\code_editor.py:204 — revisar facet 'sem comentários inline desnecessários' em CodeEditor._indent_selection
03234. [x] app\ui\editor\code_editor.py:204 — revisar facet 'não imprime side-effects na UI/IO' em CodeEditor._indent_selection
03235. [x] app\ui\editor\code_editor.py:204 — revisar facet 'thread-safety revisada' em CodeEditor._indent_selection
03236. [x] app\ui\editor\code_editor.py:204 — revisar facet 'performance (sem loops O(n^2))' em CodeEditor._indent_selection
03237. [x] app\ui\editor\code_editor.py:204 — revisar facet 'coberto por testes' em CodeEditor._indent_selection
03238. [x] app\ui\editor\code_editor.py:205 — atribuição: CodeEditor._indent_selection ← cursor
03239. [x] app\ui\editor\code_editor.py:206 — atribuição: CodeEditor._indent_selection ← ?
03240. [x] app\ui\editor\code_editor.py:209 — atribuição: CodeEditor._indent_selection ← first
03241. [x] app\ui\editor\code_editor.py:211 — atribuição: CodeEditor._indent_selection ← last
03242. [x] app\ui\editor\code_editor.py:215 — controle for em CodeEditor._indent_selection
03243. [x] app\ui\editor\code_editor.py:216 — controle if em CodeEditor._indent_selection
03244. [x] app\ui\editor\code_editor.py:219 — atribuição: CodeEditor._indent_selection ← text
03245. [x] app\ui\editor\code_editor.py:220 — controle if em CodeEditor._indent_selection
03246. [x] Existência e estrutura do módulo: app\ui\editor\editor_tabs.py
03247. [x] app\ui\editor\editor_tabs.py:3 — import: __future__
03248. [x] app\ui\editor\editor_tabs.py:5 — import: PySide6.QtCore
03249. [x] app\ui\editor\editor_tabs.py:6 — import: PySide6.QtWidgets
03250. [x] app\ui\editor\editor_tabs.py:8 — import: app.ui.editor.editor_widget
03251. [x] app\ui\editor\editor_tabs.py:11 — definir/revisar ClassDef: EditorTabs
03252. [x] app\ui\editor\editor_tabs.py:12 — atribuição: EditorTabs ← tab_dirty_changed
03253. [x] app\ui\editor\editor_tabs.py:13 — atribuição: EditorTabs ← close_tab_requested
03254. [x] app\ui\editor\editor_tabs.py:15 — definir/revisar FunctionDef: EditorTabs.__init__
03255. [x] app\ui\editor\editor_tabs.py:15 — revisar facet 'assinatura/args consistentes' em EditorTabs.__init__
03256. [x] app\ui\editor\editor_tabs.py:15 — revisar facet 'docstring em português' em EditorTabs.__init__
03257. [x] app\ui\editor\editor_tabs.py:15 — revisar facet 'nomenclatura clara (PEP8)' em EditorTabs.__init__
03258. [x] app\ui\editor\editor_tabs.py:15 — revisar facet 'type hints presentes' em EditorTabs.__init__
03259. [x] app\ui\editor\editor_tabs.py:15 — revisar facet 'tratamento de erros adequado' em EditorTabs.__init__
03260. [x] app\ui\editor\editor_tabs.py:15 — revisar facet 'sem comentários inline desnecessários' em EditorTabs.__init__
03261. [x] app\ui\editor\editor_tabs.py:15 — revisar facet 'não imprime side-effects na UI/IO' em EditorTabs.__init__
03262. [x] app\ui\editor\editor_tabs.py:15 — revisar facet 'thread-safety revisada' em EditorTabs.__init__
03263. [x] app\ui\editor\editor_tabs.py:15 — revisar facet 'performance (sem loops O(n^2))' em EditorTabs.__init__
03264. [x] app\ui\editor\editor_tabs.py:15 — revisar facet 'coberto por testes' em EditorTabs.__init__
03265. [x] app\ui\editor\editor_tabs.py:23 — definir/revisar FunctionDef: EditorTabs.open_file
03266. [x] app\ui\editor\editor_tabs.py:23 — revisar facet 'assinatura/args consistentes' em EditorTabs.open_file
03267. [x] app\ui\editor\editor_tabs.py:23 — revisar facet 'docstring em português' em EditorTabs.open_file
03268. [x] app\ui\editor\editor_tabs.py:23 — revisar facet 'nomenclatura clara (PEP8)' em EditorTabs.open_file
03269. [x] app\ui\editor\editor_tabs.py:23 — revisar facet 'type hints presentes' em EditorTabs.open_file
03270. [x] app\ui\editor\editor_tabs.py:23 — revisar facet 'tratamento de erros adequado' em EditorTabs.open_file
03271. [x] app\ui\editor\editor_tabs.py:23 — revisar facet 'sem comentários inline desnecessários' em EditorTabs.open_file
03272. [x] app\ui\editor\editor_tabs.py:23 — revisar facet 'não imprime side-effects na UI/IO' em EditorTabs.open_file
03273. [x] app\ui\editor\editor_tabs.py:23 — revisar facet 'thread-safety revisada' em EditorTabs.open_file
03274. [x] app\ui\editor\editor_tabs.py:23 — revisar facet 'performance (sem loops O(n^2))' em EditorTabs.open_file
03275. [x] app\ui\editor\editor_tabs.py:23 — revisar facet 'coberto por testes' em EditorTabs.open_file
03276. [x] app\ui\editor\editor_tabs.py:24 — atribuição: EditorTabs.open_file ← existing
03277. [x] app\ui\editor\editor_tabs.py:25 — controle if em EditorTabs.open_file
03278. [x] app\ui\editor\editor_tabs.py:27 — return em EditorTabs.open_file
03279. [x] app\ui\editor\editor_tabs.py:28 — atribuição: EditorTabs.open_file ← tab
03280. [x] app\ui\editor\editor_tabs.py:31 — return em EditorTabs.open_file
03281. [x] app\ui\editor\editor_tabs.py:33 — definir/revisar FunctionDef: EditorTabs.new_tab
03282. [x] app\ui\editor\editor_tabs.py:33 — revisar facet 'assinatura/args consistentes' em EditorTabs.new_tab
03283. [x] app\ui\editor\editor_tabs.py:33 — revisar facet 'docstring em português' em EditorTabs.new_tab
03284. [x] app\ui\editor\editor_tabs.py:33 — revisar facet 'nomenclatura clara (PEP8)' em EditorTabs.new_tab
03285. [x] app\ui\editor\editor_tabs.py:33 — revisar facet 'type hints presentes' em EditorTabs.new_tab
03286. [x] app\ui\editor\editor_tabs.py:33 — revisar facet 'tratamento de erros adequado' em EditorTabs.new_tab
03287. [x] app\ui\editor\editor_tabs.py:33 — revisar facet 'sem comentários inline desnecessários' em EditorTabs.new_tab
03288. [x] app\ui\editor\editor_tabs.py:33 — revisar facet 'não imprime side-effects na UI/IO' em EditorTabs.new_tab
03289. [x] app\ui\editor\editor_tabs.py:33 — revisar facet 'thread-safety revisada' em EditorTabs.new_tab
03290. [x] app\ui\editor\editor_tabs.py:33 — revisar facet 'performance (sem loops O(n^2))' em EditorTabs.new_tab
03291. [x] app\ui\editor\editor_tabs.py:33 — revisar facet 'coberto por testes' em EditorTabs.new_tab
03292. [x] app\ui\editor\editor_tabs.py:34 — atribuição: EditorTabs.new_tab ← tab
03293. [x] app\ui\editor\editor_tabs.py:35 — controle if em EditorTabs.new_tab
03294. [x] app\ui\editor\editor_tabs.py:38 — return em EditorTabs.new_tab
03295. [x] app\ui\editor\editor_tabs.py:40 — definir/revisar FunctionDef: EditorTabs._add_tab
03296. [x] app\ui\editor\editor_tabs.py:40 — revisar facet 'assinatura/args consistentes' em EditorTabs._add_tab
03297. [x] app\ui\editor\editor_tabs.py:40 — revisar facet 'docstring em português' em EditorTabs._add_tab
03298. [x] app\ui\editor\editor_tabs.py:40 — revisar facet 'nomenclatura clara (PEP8)' em EditorTabs._add_tab
03299. [x] app\ui\editor\editor_tabs.py:40 — revisar facet 'type hints presentes' em EditorTabs._add_tab
03300. [x] app\ui\editor\editor_tabs.py:40 — revisar facet 'tratamento de erros adequado' em EditorTabs._add_tab
03301. [x] app\ui\editor\editor_tabs.py:40 — revisar facet 'sem comentários inline desnecessários' em EditorTabs._add_tab
03302. [x] app\ui\editor\editor_tabs.py:40 — revisar facet 'não imprime side-effects na UI/IO' em EditorTabs._add_tab
03303. [x] app\ui\editor\editor_tabs.py:40 — revisar facet 'thread-safety revisada' em EditorTabs._add_tab
03304. [x] app\ui\editor\editor_tabs.py:40 — revisar facet 'performance (sem loops O(n^2))' em EditorTabs._add_tab
03305. [x] app\ui\editor\editor_tabs.py:40 — revisar facet 'coberto por testes' em EditorTabs._add_tab
03306. [x] app\ui\editor\editor_tabs.py:41 — controle if em EditorTabs._add_tab
03307. [x] app\ui\editor\editor_tabs.py:42 — import: pathlib
03308. [x] app\ui\editor\editor_tabs.py:44 — atribuição: EditorTabs._add_tab ← title
03309. [x] app\ui\editor\editor_tabs.py:45 — atribuição: EditorTabs._add_tab ← index
03310. [x] app\ui\editor\editor_tabs.py:52 — definir/revisar FunctionDef: EditorTabs._mark_dirty
03311. [x] app\ui\editor\editor_tabs.py:52 — revisar facet 'assinatura/args consistentes' em EditorTabs._mark_dirty
03312. [x] app\ui\editor\editor_tabs.py:52 — revisar facet 'docstring em português' em EditorTabs._mark_dirty
03313. [x] app\ui\editor\editor_tabs.py:52 — revisar facet 'nomenclatura clara (PEP8)' em EditorTabs._mark_dirty
03314. [x] app\ui\editor\editor_tabs.py:52 — revisar facet 'type hints presentes' em EditorTabs._mark_dirty
03315. [x] app\ui\editor\editor_tabs.py:52 — revisar facet 'tratamento de erros adequado' em EditorTabs._mark_dirty
03316. [x] app\ui\editor\editor_tabs.py:52 — revisar facet 'sem comentários inline desnecessários' em EditorTabs._mark_dirty
03317. [x] app\ui\editor\editor_tabs.py:52 — revisar facet 'não imprime side-effects na UI/IO' em EditorTabs._mark_dirty
03318. [x] app\ui\editor\editor_tabs.py:52 — revisar facet 'thread-safety revisada' em EditorTabs._mark_dirty
03319. [x] app\ui\editor\editor_tabs.py:52 — revisar facet 'performance (sem loops O(n^2))' em EditorTabs._mark_dirty
03320. [x] app\ui\editor\editor_tabs.py:52 — revisar facet 'coberto por testes' em EditorTabs._mark_dirty
03321. [x] app\ui\editor\editor_tabs.py:53 — controle if em EditorTabs._mark_dirty
03322. [x] app\ui\editor\editor_tabs.py:54 — return em EditorTabs._mark_dirty
03323. [x] app\ui\editor\editor_tabs.py:55 — atribuição: EditorTabs._mark_dirty ← base
03324. [x] app\ui\editor\editor_tabs.py:59 — definir/revisar FunctionDef: EditorTabs.find_tab_by_path
03325. [x] app\ui\editor\editor_tabs.py:59 — revisar facet 'assinatura/args consistentes' em EditorTabs.find_tab_by_path
03326. [x] app\ui\editor\editor_tabs.py:59 — revisar facet 'docstring em português' em EditorTabs.find_tab_by_path
03327. [x] app\ui\editor\editor_tabs.py:59 — revisar facet 'nomenclatura clara (PEP8)' em EditorTabs.find_tab_by_path
03328. [x] app\ui\editor\editor_tabs.py:59 — revisar facet 'type hints presentes' em EditorTabs.find_tab_by_path
03329. [x] app\ui\editor\editor_tabs.py:59 — revisar facet 'tratamento de erros adequado' em EditorTabs.find_tab_by_path
03330. [x] app\ui\editor\editor_tabs.py:59 — revisar facet 'sem comentários inline desnecessários' em EditorTabs.find_tab_by_path
03331. [x] app\ui\editor\editor_tabs.py:59 — revisar facet 'não imprime side-effects na UI/IO' em EditorTabs.find_tab_by_path
03332. [x] app\ui\editor\editor_tabs.py:59 — revisar facet 'thread-safety revisada' em EditorTabs.find_tab_by_path
03333. [x] app\ui\editor\editor_tabs.py:59 — revisar facet 'performance (sem loops O(n^2))' em EditorTabs.find_tab_by_path
03334. [x] app\ui\editor\editor_tabs.py:59 — revisar facet 'coberto por testes' em EditorTabs.find_tab_by_path
03335. [x] app\ui\editor\editor_tabs.py:60 — controle for em EditorTabs.find_tab_by_path
03336. [x] app\ui\editor\editor_tabs.py:61 — atribuição: EditorTabs.find_tab_by_path ← tab
03337. [x] app\ui\editor\editor_tabs.py:62 — controle if em EditorTabs.find_tab_by_path
03338. [x] app\ui\editor\editor_tabs.py:63 — return em EditorTabs.find_tab_by_path
03339. [x] app\ui\editor\editor_tabs.py:64 — return em EditorTabs.find_tab_by_path
03340. [x] app\ui\editor\editor_tabs.py:66 — definir/revisar FunctionDef: EditorTabs.current_editor
03341. [x] app\ui\editor\editor_tabs.py:66 — revisar facet 'assinatura/args consistentes' em EditorTabs.current_editor
03342. [x] app\ui\editor\editor_tabs.py:66 — revisar facet 'docstring em português' em EditorTabs.current_editor
03343. [x] app\ui\editor\editor_tabs.py:66 — revisar facet 'nomenclatura clara (PEP8)' em EditorTabs.current_editor
03344. [x] app\ui\editor\editor_tabs.py:66 — revisar facet 'type hints presentes' em EditorTabs.current_editor
03345. [x] app\ui\editor\editor_tabs.py:66 — revisar facet 'tratamento de erros adequado' em EditorTabs.current_editor
03346. [x] app\ui\editor\editor_tabs.py:66 — revisar facet 'sem comentários inline desnecessários' em EditorTabs.current_editor
03347. [x] app\ui\editor\editor_tabs.py:66 — revisar facet 'não imprime side-effects na UI/IO' em EditorTabs.current_editor
03348. [x] app\ui\editor\editor_tabs.py:66 — revisar facet 'thread-safety revisada' em EditorTabs.current_editor
03349. [x] app\ui\editor\editor_tabs.py:66 — revisar facet 'performance (sem loops O(n^2))' em EditorTabs.current_editor
03350. [x] app\ui\editor\editor_tabs.py:66 — revisar facet 'coberto por testes' em EditorTabs.current_editor
03351. [x] app\ui\editor\editor_tabs.py:67 — atribuição: EditorTabs.current_editor ← w
03352. [x] app\ui\editor\editor_tabs.py:68 — return em EditorTabs.current_editor
03353. [x] app\ui\editor\editor_tabs.py:71 — definir/revisar FunctionDef: EditorTabs._handle_close_request
03354. [x] app\ui\editor\editor_tabs.py:71 — revisar facet 'assinatura/args consistentes' em EditorTabs._handle_close_request
03355. [x] app\ui\editor\editor_tabs.py:71 — revisar facet 'docstring em português' em EditorTabs._handle_close_request
03356. [x] app\ui\editor\editor_tabs.py:71 — revisar facet 'nomenclatura clara (PEP8)' em EditorTabs._handle_close_request
03357. [x] app\ui\editor\editor_tabs.py:71 — revisar facet 'type hints presentes' em EditorTabs._handle_close_request
03358. [x] app\ui\editor\editor_tabs.py:71 — revisar facet 'tratamento de erros adequado' em EditorTabs._handle_close_request
03359. [x] app\ui\editor\editor_tabs.py:71 — revisar facet 'sem comentários inline desnecessários' em EditorTabs._handle_close_request
03360. [x] app\ui\editor\editor_tabs.py:71 — revisar facet 'não imprime side-effects na UI/IO' em EditorTabs._handle_close_request
03361. [x] app\ui\editor\editor_tabs.py:71 — revisar facet 'thread-safety revisada' em EditorTabs._handle_close_request
03362. [x] app\ui\editor\editor_tabs.py:71 — revisar facet 'performance (sem loops O(n^2))' em EditorTabs._handle_close_request
03363. [x] app\ui\editor\editor_tabs.py:71 — revisar facet 'coberto por testes' em EditorTabs._handle_close_request
03364. [x] app\ui\editor\editor_tabs.py:75 — definir/revisar FunctionDef: EditorTabs._close_tab
03365. [x] app\ui\editor\editor_tabs.py:75 — revisar facet 'assinatura/args consistentes' em EditorTabs._close_tab
03366. [x] app\ui\editor\editor_tabs.py:75 — revisar facet 'docstring em português' em EditorTabs._close_tab
03367. [x] app\ui\editor\editor_tabs.py:75 — revisar facet 'nomenclatura clara (PEP8)' em EditorTabs._close_tab
03368. [x] app\ui\editor\editor_tabs.py:75 — revisar facet 'type hints presentes' em EditorTabs._close_tab
03369. [x] app\ui\editor\editor_tabs.py:75 — revisar facet 'tratamento de erros adequado' em EditorTabs._close_tab
03370. [x] app\ui\editor\editor_tabs.py:75 — revisar facet 'sem comentários inline desnecessários' em EditorTabs._close_tab
03371. [x] app\ui\editor\editor_tabs.py:75 — revisar facet 'não imprime side-effects na UI/IO' em EditorTabs._close_tab
03372. [x] app\ui\editor\editor_tabs.py:75 — revisar facet 'thread-safety revisada' em EditorTabs._close_tab
03373. [x] app\ui\editor\editor_tabs.py:75 — revisar facet 'performance (sem loops O(n^2))' em EditorTabs._close_tab
03374. [x] app\ui\editor\editor_tabs.py:75 — revisar facet 'coberto por testes' em EditorTabs._close_tab
03375. [x] app\ui\editor\editor_tabs.py:76 — atribuição: EditorTabs._close_tab ← tab
03376. [x] app\ui\editor\editor_tabs.py:77 — controle if em EditorTabs._close_tab
03377. [x] app\ui\editor\editor_tabs.py:78 — atribuição: EditorTabs._close_tab ← answer
03378. [x] app\ui\editor\editor_tabs.py:85 — controle if em EditorTabs._close_tab
03379. [x] app\ui\editor\editor_tabs.py:86 — controle if em EditorTabs._close_tab
03380. [x] app\ui\editor\editor_tabs.py:87 — atribuição: EditorTabs._close_tab ← ?
03381. [x] app\ui\editor\editor_tabs.py:90 — controle if em EditorTabs._close_tab
03382. [x] app\ui\editor\editor_tabs.py:91 — return em EditorTabs._close_tab
03383. [x] app\ui\editor\editor_tabs.py:92 — atribuição: EditorTabs._close_tab ← ?
03384. [x] app\ui\editor\editor_tabs.py:94 — controle if em EditorTabs._close_tab
03385. [x] app\ui\editor\editor_tabs.py:95 — return em EditorTabs._close_tab
03386. [x] app\ui\editor\editor_tabs.py:98 — definir/revisar FunctionDef: EditorTabs.open_dialog
03387. [x] app\ui\editor\editor_tabs.py:98 — revisar facet 'assinatura/args consistentes' em EditorTabs.open_dialog
03388. [x] app\ui\editor\editor_tabs.py:98 — revisar facet 'docstring em português' em EditorTabs.open_dialog
03389. [x] app\ui\editor\editor_tabs.py:98 — revisar facet 'nomenclatura clara (PEP8)' em EditorTabs.open_dialog
03390. [x] app\ui\editor\editor_tabs.py:98 — revisar facet 'type hints presentes' em EditorTabs.open_dialog
03391. [x] app\ui\editor\editor_tabs.py:98 — revisar facet 'tratamento de erros adequado' em EditorTabs.open_dialog
03392. [x] app\ui\editor\editor_tabs.py:98 — revisar facet 'sem comentários inline desnecessários' em EditorTabs.open_dialog
03393. [x] app\ui\editor\editor_tabs.py:98 — revisar facet 'não imprime side-effects na UI/IO' em EditorTabs.open_dialog
03394. [x] app\ui\editor\editor_tabs.py:98 — revisar facet 'thread-safety revisada' em EditorTabs.open_dialog
03395. [x] app\ui\editor\editor_tabs.py:98 — revisar facet 'performance (sem loops O(n^2))' em EditorTabs.open_dialog
03396. [x] app\ui\editor\editor_tabs.py:98 — revisar facet 'coberto por testes' em EditorTabs.open_dialog
03397. [x] app\ui\editor\editor_tabs.py:99 — atribuição: EditorTabs.open_dialog ← ?
03398. [x] app\ui\editor\editor_tabs.py:102 — controle for em EditorTabs.open_dialog
03399. [x] app\ui\editor\editor_tabs.py:105 — definir/revisar FunctionDef: EditorTabs.save_current
03400. [x] app\ui\editor\editor_tabs.py:105 — revisar facet 'assinatura/args consistentes' em EditorTabs.save_current
03401. [x] app\ui\editor\editor_tabs.py:105 — revisar facet 'docstring em português' em EditorTabs.save_current
03402. [x] app\ui\editor\editor_tabs.py:105 — revisar facet 'nomenclatura clara (PEP8)' em EditorTabs.save_current
03403. [x] app\ui\editor\editor_tabs.py:105 — revisar facet 'type hints presentes' em EditorTabs.save_current
03404. [x] app\ui\editor\editor_tabs.py:105 — revisar facet 'tratamento de erros adequado' em EditorTabs.save_current
03405. [x] app\ui\editor\editor_tabs.py:105 — revisar facet 'sem comentários inline desnecessários' em EditorTabs.save_current
03406. [x] app\ui\editor\editor_tabs.py:105 — revisar facet 'não imprime side-effects na UI/IO' em EditorTabs.save_current
03407. [x] app\ui\editor\editor_tabs.py:105 — revisar facet 'thread-safety revisada' em EditorTabs.save_current
03408. [x] app\ui\editor\editor_tabs.py:105 — revisar facet 'performance (sem loops O(n^2))' em EditorTabs.save_current
03409. [x] app\ui\editor\editor_tabs.py:105 — revisar facet 'coberto por testes' em EditorTabs.save_current
03410. [x] app\ui\editor\editor_tabs.py:106 — atribuição: EditorTabs.save_current ← tab
03411. [x] app\ui\editor\editor_tabs.py:107 — controle if em EditorTabs.save_current
03412. [x] app\ui\editor\editor_tabs.py:108 — controle if em EditorTabs.save_current
03413. [x] app\ui\editor\editor_tabs.py:109 — atribuição: EditorTabs.save_current ← ?
03414. [x] app\ui\editor\editor_tabs.py:112 — controle if em EditorTabs.save_current
03415. [x] app\ui\editor\editor_tabs.py:113 — return em EditorTabs.save_current
03416. [x] app\ui\editor\editor_tabs.py:114 — atribuição: EditorTabs.save_current ← ?
03417. [x] Existência e estrutura do módulo: app\ui\editor\editor_widget.py
03418. [x] app\ui\editor\editor_widget.py:3 — import: __future__
03419. [x] app\ui\editor\editor_widget.py:5 — import: PySide6.QtCore
03420. [x] app\ui\editor\editor_widget.py:6 — import: PySide6.QtGui
03421. [x] app\ui\editor\editor_widget.py:7 — import: PySide6.QtWidgets
03422. [x] app\ui\editor\editor_widget.py:9 — import: app.ui.editor.code_editor
03423. [x] app\ui\editor\editor_widget.py:10 — import: app.ui.editor.find_replace_bar
03424. [x] app\ui\editor\editor_widget.py:11 — import: app.ui.editor.highlighter
03425. [x] app\ui\editor\editor_widget.py:14 — definir/revisar ClassDef: EditorWidget
03426. [x] app\ui\editor\editor_widget.py:15 — atribuição: EditorWidget ← modified_changed
03427. [x] app\ui\editor\editor_widget.py:16 — atribuição: EditorWidget ← saved
03428. [x] app\ui\editor\editor_widget.py:17 — atribuição: EditorWidget ← theme_changed
03429. [x] app\ui\editor\editor_widget.py:19 — definir/revisar FunctionDef: EditorWidget.__init__
03430. [x] app\ui\editor\editor_widget.py:19 — revisar facet 'assinatura/args consistentes' em EditorWidget.__init__
03431. [x] app\ui\editor\editor_widget.py:19 — revisar facet 'docstring em português' em EditorWidget.__init__
03432. [x] app\ui\editor\editor_widget.py:19 — revisar facet 'nomenclatura clara (PEP8)' em EditorWidget.__init__
03433. [x] app\ui\editor\editor_widget.py:19 — revisar facet 'type hints presentes' em EditorWidget.__init__
03434. [x] app\ui\editor\editor_widget.py:19 — revisar facet 'tratamento de erros adequado' em EditorWidget.__init__
03435. [x] app\ui\editor\editor_widget.py:19 — revisar facet 'sem comentários inline desnecessários' em EditorWidget.__init__
03436. [x] app\ui\editor\editor_widget.py:19 — revisar facet 'não imprime side-effects na UI/IO' em EditorWidget.__init__
03437. [x] app\ui\editor\editor_widget.py:19 — revisar facet 'thread-safety revisada' em EditorWidget.__init__
03438. [x] app\ui\editor\editor_widget.py:19 — revisar facet 'performance (sem loops O(n^2))' em EditorWidget.__init__
03439. [x] app\ui\editor\editor_widget.py:19 — revisar facet 'coberto por testes' em EditorWidget.__init__
03440. [x] app\ui\editor\editor_widget.py:21 — atribuição: EditorWidget.__init__ ← ?
03441. [x] app\ui\editor\editor_widget.py:22 — atribuição: EditorWidget.__init__ ← ?
03442. [x] app\ui\editor\editor_widget.py:24 — import: app.ui.editor.themes
03443. [x] app\ui\editor\editor_widget.py:26 — atribuição: EditorWidget.__init__ ← ?
03444. [x] app\ui\editor\editor_widget.py:27 — atribuição: EditorWidget.__init__ ← ?
03445. [x] app\ui\editor\editor_widget.py:28 — atribuição: EditorWidget.__init__ ← ?
03446. [x] app\ui\editor\editor_widget.py:30 — atribuição: EditorWidget.__init__ ← ?
03447. [x] app\ui\editor\editor_widget.py:31 — atribuição: EditorWidget.__init__ ← ?
03448. [x] app\ui\editor\editor_widget.py:33 — atribuição: EditorWidget.__init__ ← layout
03449. [x] app\ui\editor\editor_widget.py:43 — definir/revisar FunctionDef: EditorWidget.set_content
03450. [x] app\ui\editor\editor_widget.py:43 — revisar facet 'assinatura/args consistentes' em EditorWidget.set_content
03451. [x] app\ui\editor\editor_widget.py:43 — revisar facet 'docstring em português' em EditorWidget.set_content
03452. [x] app\ui\editor\editor_widget.py:43 — revisar facet 'nomenclatura clara (PEP8)' em EditorWidget.set_content
03453. [x] app\ui\editor\editor_widget.py:43 — revisar facet 'type hints presentes' em EditorWidget.set_content
03454. [x] app\ui\editor\editor_widget.py:43 — revisar facet 'tratamento de erros adequado' em EditorWidget.set_content
03455. [x] app\ui\editor\editor_widget.py:43 — revisar facet 'sem comentários inline desnecessários' em EditorWidget.set_content
03456. [x] app\ui\editor\editor_widget.py:43 — revisar facet 'não imprime side-effects na UI/IO' em EditorWidget.set_content
03457. [x] app\ui\editor\editor_widget.py:43 — revisar facet 'thread-safety revisada' em EditorWidget.set_content
03458. [x] app\ui\editor\editor_widget.py:43 — revisar facet 'performance (sem loops O(n^2))' em EditorWidget.set_content
03459. [x] app\ui\editor\editor_widget.py:43 — revisar facet 'coberto por testes' em EditorWidget.set_content
03460. [x] app\ui\editor\editor_widget.py:47 — definir/revisar FunctionDef: EditorWidget.text
03461. [x] app\ui\editor\editor_widget.py:47 — revisar facet 'assinatura/args consistentes' em EditorWidget.text
03462. [x] app\ui\editor\editor_widget.py:47 — revisar facet 'docstring em português' em EditorWidget.text
03463. [x] app\ui\editor\editor_widget.py:47 — revisar facet 'nomenclatura clara (PEP8)' em EditorWidget.text
03464. [x] app\ui\editor\editor_widget.py:47 — revisar facet 'type hints presentes' em EditorWidget.text
03465. [x] app\ui\editor\editor_widget.py:47 — revisar facet 'tratamento de erros adequado' em EditorWidget.text
03466. [x] app\ui\editor\editor_widget.py:47 — revisar facet 'sem comentários inline desnecessários' em EditorWidget.text
03467. [x] app\ui\editor\editor_widget.py:47 — revisar facet 'não imprime side-effects na UI/IO' em EditorWidget.text
03468. [x] app\ui\editor\editor_widget.py:47 — revisar facet 'thread-safety revisada' em EditorWidget.text
03469. [x] app\ui\editor\editor_widget.py:47 — revisar facet 'performance (sem loops O(n^2))' em EditorWidget.text
03470. [x] app\ui\editor\editor_widget.py:47 — revisar facet 'coberto por testes' em EditorWidget.text
03471. [x] app\ui\editor\editor_widget.py:48 — return em EditorWidget.text
03472. [x] app\ui\editor\editor_widget.py:50 — definir/revisar FunctionDef: EditorWidget.is_modified
03473. [x] app\ui\editor\editor_widget.py:50 — revisar facet 'assinatura/args consistentes' em EditorWidget.is_modified
03474. [x] app\ui\editor\editor_widget.py:50 — revisar facet 'docstring em português' em EditorWidget.is_modified
03475. [x] app\ui\editor\editor_widget.py:50 — revisar facet 'nomenclatura clara (PEP8)' em EditorWidget.is_modified
03476. [x] app\ui\editor\editor_widget.py:50 — revisar facet 'type hints presentes' em EditorWidget.is_modified
03477. [x] app\ui\editor\editor_widget.py:50 — revisar facet 'tratamento de erros adequado' em EditorWidget.is_modified
03478. [x] app\ui\editor\editor_widget.py:50 — revisar facet 'sem comentários inline desnecessários' em EditorWidget.is_modified
03479. [x] app\ui\editor\editor_widget.py:50 — revisar facet 'não imprime side-effects na UI/IO' em EditorWidget.is_modified
03480. [x] app\ui\editor\editor_widget.py:50 — revisar facet 'thread-safety revisada' em EditorWidget.is_modified
03481. [x] app\ui\editor\editor_widget.py:50 — revisar facet 'performance (sem loops O(n^2))' em EditorWidget.is_modified
03482. [x] app\ui\editor\editor_widget.py:50 — revisar facet 'coberto por testes' em EditorWidget.is_modified
03483. [x] app\ui\editor\editor_widget.py:51 — return em EditorWidget.is_modified
03484. [x] app\ui\editor\editor_widget.py:53 — definir/revisar FunctionDef: EditorWidget.set_readonly
03485. [x] app\ui\editor\editor_widget.py:53 — revisar facet 'assinatura/args consistentes' em EditorWidget.set_readonly
03486. [x] app\ui\editor\editor_widget.py:53 — revisar facet 'docstring em português' em EditorWidget.set_readonly
03487. [x] app\ui\editor\editor_widget.py:53 — revisar facet 'nomenclatura clara (PEP8)' em EditorWidget.set_readonly
03488. [x] app\ui\editor\editor_widget.py:53 — revisar facet 'type hints presentes' em EditorWidget.set_readonly
03489. [x] app\ui\editor\editor_widget.py:53 — revisar facet 'tratamento de erros adequado' em EditorWidget.set_readonly
03490. [x] app\ui\editor\editor_widget.py:53 — revisar facet 'sem comentários inline desnecessários' em EditorWidget.set_readonly
03491. [x] app\ui\editor\editor_widget.py:53 — revisar facet 'não imprime side-effects na UI/IO' em EditorWidget.set_readonly
03492. [x] app\ui\editor\editor_widget.py:53 — revisar facet 'thread-safety revisada' em EditorWidget.set_readonly
03493. [x] app\ui\editor\editor_widget.py:53 — revisar facet 'performance (sem loops O(n^2))' em EditorWidget.set_readonly
03494. [x] app\ui\editor\editor_widget.py:53 — revisar facet 'coberto por testes' em EditorWidget.set_readonly
03495. [x] app\ui\editor\editor_widget.py:54 — atribuição: EditorWidget.set_readonly ← ?
03496. [x] app\ui\editor\editor_widget.py:57 — definir/revisar FunctionDef: EditorWidget.set_variables
03497. [x] app\ui\editor\editor_widget.py:57 — revisar facet 'assinatura/args consistentes' em EditorWidget.set_variables
03498. [x] app\ui\editor\editor_widget.py:57 — revisar facet 'docstring em português' em EditorWidget.set_variables
03499. [x] app\ui\editor\editor_widget.py:57 — revisar facet 'nomenclatura clara (PEP8)' em EditorWidget.set_variables
03500. [x] app\ui\editor\editor_widget.py:57 — revisar facet 'type hints presentes' em EditorWidget.set_variables
03501. [x] app\ui\editor\editor_widget.py:57 — revisar facet 'tratamento de erros adequado' em EditorWidget.set_variables
03502. [x] app\ui\editor\editor_widget.py:57 — revisar facet 'sem comentários inline desnecessários' em EditorWidget.set_variables
03503. [x] app\ui\editor\editor_widget.py:57 — revisar facet 'não imprime side-effects na UI/IO' em EditorWidget.set_variables
03504. [x] app\ui\editor\editor_widget.py:57 — revisar facet 'thread-safety revisada' em EditorWidget.set_variables
03505. [x] app\ui\editor\editor_widget.py:57 — revisar facet 'performance (sem loops O(n^2))' em EditorWidget.set_variables
03506. [x] app\ui\editor\editor_widget.py:57 — revisar facet 'coberto por testes' em EditorWidget.set_variables
03507. [x] app\ui\editor\editor_widget.py:60 — definir/revisar FunctionDef: EditorWidget.set_theme
03508. [x] app\ui\editor\editor_widget.py:60 — revisar facet 'assinatura/args consistentes' em EditorWidget.set_theme
03509. [x] app\ui\editor\editor_widget.py:60 — revisar facet 'docstring em português' em EditorWidget.set_theme
03510. [x] app\ui\editor\editor_widget.py:60 — revisar facet 'nomenclatura clara (PEP8)' em EditorWidget.set_theme
03511. [x] app\ui\editor\editor_widget.py:60 — revisar facet 'type hints presentes' em EditorWidget.set_theme
03512. [x] app\ui\editor\editor_widget.py:60 — revisar facet 'tratamento de erros adequado' em EditorWidget.set_theme
03513. [x] app\ui\editor\editor_widget.py:60 — revisar facet 'sem comentários inline desnecessários' em EditorWidget.set_theme
03514. [x] app\ui\editor\editor_widget.py:60 — revisar facet 'não imprime side-effects na UI/IO' em EditorWidget.set_theme
03515. [x] app\ui\editor\editor_widget.py:60 — revisar facet 'thread-safety revisada' em EditorWidget.set_theme
03516. [x] app\ui\editor\editor_widget.py:60 — revisar facet 'performance (sem loops O(n^2))' em EditorWidget.set_theme
03517. [x] app\ui\editor\editor_widget.py:60 — revisar facet 'coberto por testes' em EditorWidget.set_theme
03518. [x] app\ui\editor\editor_widget.py:61 — atribuição: EditorWidget.set_theme ← ?
03519. [x] app\ui\editor\editor_widget.py:67 — definir/revisar FunctionDef: EditorWidget.zoom
03520. [x] app\ui\editor\editor_widget.py:67 — revisar facet 'assinatura/args consistentes' em EditorWidget.zoom
03521. [x] app\ui\editor\editor_widget.py:67 — revisar facet 'docstring em português' em EditorWidget.zoom
03522. [x] app\ui\editor\editor_widget.py:67 — revisar facet 'nomenclatura clara (PEP8)' em EditorWidget.zoom
03523. [x] app\ui\editor\editor_widget.py:67 — revisar facet 'type hints presentes' em EditorWidget.zoom
03524. [x] app\ui\editor\editor_widget.py:67 — revisar facet 'tratamento de erros adequado' em EditorWidget.zoom
03525. [x] app\ui\editor\editor_widget.py:67 — revisar facet 'sem comentários inline desnecessários' em EditorWidget.zoom
03526. [x] app\ui\editor\editor_widget.py:67 — revisar facet 'não imprime side-effects na UI/IO' em EditorWidget.zoom
03527. [x] app\ui\editor\editor_widget.py:67 — revisar facet 'thread-safety revisada' em EditorWidget.zoom
03528. [x] app\ui\editor\editor_widget.py:67 — revisar facet 'performance (sem loops O(n^2))' em EditorWidget.zoom
03529. [x] app\ui\editor\editor_widget.py:67 — revisar facet 'coberto por testes' em EditorWidget.zoom
03530. [x] app\ui\editor\editor_widget.py:70 — definir/revisar FunctionDef: EditorWidget.zoom_reset
03531. [x] app\ui\editor\editor_widget.py:70 — revisar facet 'assinatura/args consistentes' em EditorWidget.zoom_reset
03532. [x] app\ui\editor\editor_widget.py:70 — revisar facet 'docstring em português' em EditorWidget.zoom_reset
03533. [x] app\ui\editor\editor_widget.py:70 — revisar facet 'nomenclatura clara (PEP8)' em EditorWidget.zoom_reset
03534. [x] app\ui\editor\editor_widget.py:70 — revisar facet 'type hints presentes' em EditorWidget.zoom_reset
03535. [x] app\ui\editor\editor_widget.py:70 — revisar facet 'tratamento de erros adequado' em EditorWidget.zoom_reset
03536. [x] app\ui\editor\editor_widget.py:70 — revisar facet 'sem comentários inline desnecessários' em EditorWidget.zoom_reset
03537. [x] app\ui\editor\editor_widget.py:70 — revisar facet 'não imprime side-effects na UI/IO' em EditorWidget.zoom_reset
03538. [x] app\ui\editor\editor_widget.py:70 — revisar facet 'thread-safety revisada' em EditorWidget.zoom_reset
03539. [x] app\ui\editor\editor_widget.py:70 — revisar facet 'performance (sem loops O(n^2))' em EditorWidget.zoom_reset
03540. [x] app\ui\editor\editor_widget.py:70 — revisar facet 'coberto por testes' em EditorWidget.zoom_reset
03541. [x] app\ui\editor\editor_widget.py:74 — definir/revisar FunctionDef: EditorWidget.save
03542. [x] app\ui\editor\editor_widget.py:74 — revisar facet 'assinatura/args consistentes' em EditorWidget.save
03543. [x] app\ui\editor\editor_widget.py:74 — revisar facet 'docstring em português' em EditorWidget.save
03544. [x] app\ui\editor\editor_widget.py:74 — revisar facet 'nomenclatura clara (PEP8)' em EditorWidget.save
03545. [x] app\ui\editor\editor_widget.py:74 — revisar facet 'type hints presentes' em EditorWidget.save
03546. [x] app\ui\editor\editor_widget.py:74 — revisar facet 'tratamento de erros adequado' em EditorWidget.save
03547. [x] app\ui\editor\editor_widget.py:74 — revisar facet 'sem comentários inline desnecessários' em EditorWidget.save
03548. [x] app\ui\editor\editor_widget.py:74 — revisar facet 'não imprime side-effects na UI/IO' em EditorWidget.save
03549. [x] app\ui\editor\editor_widget.py:74 — revisar facet 'thread-safety revisada' em EditorWidget.save
03550. [x] app\ui\editor\editor_widget.py:74 — revisar facet 'performance (sem loops O(n^2))' em EditorWidget.save
03551. [x] app\ui\editor\editor_widget.py:74 — revisar facet 'coberto por testes' em EditorWidget.save
03552. [x] app\ui\editor\editor_widget.py:75 — controle if em EditorWidget.save
03553. [x] app\ui\editor\editor_widget.py:76 — return em EditorWidget.save
03554. [x] app\ui\editor\editor_widget.py:77 — controle with em EditorWidget.save
03555. [x] app\ui\editor\editor_widget.py:82 — definir/revisar FunctionDef: EditorWidget.load_file
03556. [x] app\ui\editor\editor_widget.py:82 — revisar facet 'assinatura/args consistentes' em EditorWidget.load_file
03557. [x] app\ui\editor\editor_widget.py:82 — revisar facet 'docstring em português' em EditorWidget.load_file
03558. [x] app\ui\editor\editor_widget.py:82 — revisar facet 'nomenclatura clara (PEP8)' em EditorWidget.load_file
03559. [x] app\ui\editor\editor_widget.py:82 — revisar facet 'type hints presentes' em EditorWidget.load_file
03560. [x] app\ui\editor\editor_widget.py:82 — revisar facet 'tratamento de erros adequado' em EditorWidget.load_file
03561. [x] app\ui\editor\editor_widget.py:82 — revisar facet 'sem comentários inline desnecessários' em EditorWidget.load_file
03562. [x] app\ui\editor\editor_widget.py:82 — revisar facet 'não imprime side-effects na UI/IO' em EditorWidget.load_file
03563. [x] app\ui\editor\editor_widget.py:82 — revisar facet 'thread-safety revisada' em EditorWidget.load_file
03564. [x] app\ui\editor\editor_widget.py:82 — revisar facet 'performance (sem loops O(n^2))' em EditorWidget.load_file
03565. [x] app\ui\editor\editor_widget.py:82 — revisar facet 'coberto por testes' em EditorWidget.load_file
03566. [x] app\ui\editor\editor_widget.py:83 — controle with em EditorWidget.load_file
03567. [x] app\ui\editor\editor_widget.py:85 — atribuição: EditorWidget.load_file ← ?
03568. [x] app\ui\editor\editor_widget.py:88 — definir/revisar FunctionDef: EditorWidget._on_text_changed
03569. [x] app\ui\editor\editor_widget.py:88 — revisar facet 'assinatura/args consistentes' em EditorWidget._on_text_changed
03570. [x] app\ui\editor\editor_widget.py:88 — revisar facet 'docstring em português' em EditorWidget._on_text_changed
03571. [x] app\ui\editor\editor_widget.py:88 — revisar facet 'nomenclatura clara (PEP8)' em EditorWidget._on_text_changed
03572. [x] app\ui\editor\editor_widget.py:88 — revisar facet 'type hints presentes' em EditorWidget._on_text_changed
03573. [x] app\ui\editor\editor_widget.py:88 — revisar facet 'tratamento de erros adequado' em EditorWidget._on_text_changed
03574. [x] app\ui\editor\editor_widget.py:88 — revisar facet 'sem comentários inline desnecessários' em EditorWidget._on_text_changed
03575. [x] app\ui\editor\editor_widget.py:88 — revisar facet 'não imprime side-effects na UI/IO' em EditorWidget._on_text_changed
03576. [x] app\ui\editor\editor_widget.py:88 — revisar facet 'thread-safety revisada' em EditorWidget._on_text_changed
03577. [x] app\ui\editor\editor_widget.py:88 — revisar facet 'performance (sem loops O(n^2))' em EditorWidget._on_text_changed
03578. [x] app\ui\editor\editor_widget.py:88 — revisar facet 'coberto por testes' em EditorWidget._on_text_changed
03579. [x] app\ui\editor\editor_widget.py:91 — definir/revisar FunctionDef: EditorWidget._on_modification
03580. [x] app\ui\editor\editor_widget.py:91 — revisar facet 'assinatura/args consistentes' em EditorWidget._on_modification
03581. [x] app\ui\editor\editor_widget.py:91 — revisar facet 'docstring em português' em EditorWidget._on_modification
03582. [x] app\ui\editor\editor_widget.py:91 — revisar facet 'nomenclatura clara (PEP8)' em EditorWidget._on_modification
03583. [x] app\ui\editor\editor_widget.py:91 — revisar facet 'type hints presentes' em EditorWidget._on_modification
03584. [x] app\ui\editor\editor_widget.py:91 — revisar facet 'tratamento de erros adequado' em EditorWidget._on_modification
03585. [x] app\ui\editor\editor_widget.py:91 — revisar facet 'sem comentários inline desnecessários' em EditorWidget._on_modification
03586. [x] app\ui\editor\editor_widget.py:91 — revisar facet 'não imprime side-effects na UI/IO' em EditorWidget._on_modification
03587. [x] app\ui\editor\editor_widget.py:91 — revisar facet 'thread-safety revisada' em EditorWidget._on_modification
03588. [x] app\ui\editor\editor_widget.py:91 — revisar facet 'performance (sem loops O(n^2))' em EditorWidget._on_modification
03589. [x] app\ui\editor\editor_widget.py:91 — revisar facet 'coberto por testes' em EditorWidget._on_modification
03590. [x] app\ui\editor\editor_widget.py:94 — definir/revisar FunctionDef: EditorWidget.keyPressEvent
03591. [x] app\ui\editor\editor_widget.py:94 — revisar facet 'assinatura/args consistentes' em EditorWidget.keyPressEvent
03592. [x] app\ui\editor\editor_widget.py:94 — revisar facet 'docstring em português' em EditorWidget.keyPressEvent
03593. [x] app\ui\editor\editor_widget.py:94 — revisar facet 'nomenclatura clara (PEP8)' em EditorWidget.keyPressEvent
03594. [x] app\ui\editor\editor_widget.py:94 — revisar facet 'type hints presentes' em EditorWidget.keyPressEvent
03595. [x] app\ui\editor\editor_widget.py:94 — revisar facet 'tratamento de erros adequado' em EditorWidget.keyPressEvent
03596. [x] app\ui\editor\editor_widget.py:94 — revisar facet 'sem comentários inline desnecessários' em EditorWidget.keyPressEvent
03597. [x] app\ui\editor\editor_widget.py:94 — revisar facet 'não imprime side-effects na UI/IO' em EditorWidget.keyPressEvent
03598. [x] app\ui\editor\editor_widget.py:94 — revisar facet 'thread-safety revisada' em EditorWidget.keyPressEvent
03599. [x] app\ui\editor\editor_widget.py:94 — revisar facet 'performance (sem loops O(n^2))' em EditorWidget.keyPressEvent
03600. [x] app\ui\editor\editor_widget.py:94 — revisar facet 'coberto por testes' em EditorWidget.keyPressEvent
03601. [x] app\ui\editor\editor_widget.py:95 — controle if em EditorWidget.keyPressEvent
03602. [x] app\ui\editor\editor_widget.py:97 — return em EditorWidget.keyPressEvent
03603. [x] Existência e estrutura do módulo: app\ui\editor\find_replace_bar.py
03604. [x] app\ui\editor\find_replace_bar.py:3 — import: __future__
03605. [x] app\ui\editor\find_replace_bar.py:5 — import: PySide6.QtCore
03606. [x] app\ui\editor\find_replace_bar.py:6 — import: PySide6.QtGui
03607. [x] app\ui\editor\find_replace_bar.py:7 — import: PySide6.QtWidgets
03608. [x] app\ui\editor\find_replace_bar.py:17 — definir/revisar ClassDef: FindReplaceBar
03609. [x] app\ui\editor\find_replace_bar.py:20 — atribuição: FindReplaceBar ← find_next
03610. [x] app\ui\editor\find_replace_bar.py:21 — atribuição: FindReplaceBar ← replace_one
03611. [x] app\ui\editor\find_replace_bar.py:22 — atribuição: FindReplaceBar ← replace_all
03612. [x] app\ui\editor\find_replace_bar.py:23 — atribuição: FindReplaceBar ← closed
03613. [x] app\ui\editor\find_replace_bar.py:25 — definir/revisar FunctionDef: FindReplaceBar.__init__
03614. [x] app\ui\editor\find_replace_bar.py:25 — revisar facet 'assinatura/args consistentes' em FindReplaceBar.__init__
03615. [x] app\ui\editor\find_replace_bar.py:25 — revisar facet 'docstring em português' em FindReplaceBar.__init__
03616. [x] app\ui\editor\find_replace_bar.py:25 — revisar facet 'nomenclatura clara (PEP8)' em FindReplaceBar.__init__
03617. [x] app\ui\editor\find_replace_bar.py:25 — revisar facet 'type hints presentes' em FindReplaceBar.__init__
03618. [x] app\ui\editor\find_replace_bar.py:25 — revisar facet 'tratamento de erros adequado' em FindReplaceBar.__init__
03619. [x] app\ui\editor\find_replace_bar.py:25 — revisar facet 'sem comentários inline desnecessários' em FindReplaceBar.__init__
03620. [x] app\ui\editor\find_replace_bar.py:25 — revisar facet 'não imprime side-effects na UI/IO' em FindReplaceBar.__init__
03621. [x] app\ui\editor\find_replace_bar.py:25 — revisar facet 'thread-safety revisada' em FindReplaceBar.__init__
03622. [x] app\ui\editor\find_replace_bar.py:25 — revisar facet 'performance (sem loops O(n^2))' em FindReplaceBar.__init__
03623. [x] app\ui\editor\find_replace_bar.py:25 — revisar facet 'coberto por testes' em FindReplaceBar.__init__
03624. [x] app\ui\editor\find_replace_bar.py:29 — atribuição: FindReplaceBar.__init__ ← ?
03625. [x] app\ui\editor\find_replace_bar.py:32 — atribuição: FindReplaceBar.__init__ ← ?
03626. [x] app\ui\editor\find_replace_bar.py:35 — atribuição: FindReplaceBar.__init__ ← ?
03627. [x] app\ui\editor\find_replace_bar.py:36 — atribuição: FindReplaceBar.__init__ ← ?
03628. [x] app\ui\editor\find_replace_bar.py:38 — atribuição: FindReplaceBar.__init__ ← btn_find
03629. [x] app\ui\editor\find_replace_bar.py:39 — atribuição: FindReplaceBar.__init__ ← btn_replace
03630. [x] app\ui\editor\find_replace_bar.py:40 — atribuição: FindReplaceBar.__init__ ← btn_all
03631. [x] app\ui\editor\find_replace_bar.py:41 — atribuição: FindReplaceBar.__init__ ← btn_close
03632. [x] app\ui\editor\find_replace_bar.py:43 — atribuição: FindReplaceBar.__init__ ← row
03633. [x] app\ui\editor\find_replace_bar.py:45 — controle for em FindReplaceBar.__init__
03634. [x] app\ui\editor\find_replace_bar.py:67 — definir/revisar FunctionDef: FindReplaceBar._emit_find
03635. [x] app\ui\editor\find_replace_bar.py:67 — revisar facet 'assinatura/args consistentes' em FindReplaceBar._emit_find
03636. [x] app\ui\editor\find_replace_bar.py:67 — revisar facet 'docstring em português' em FindReplaceBar._emit_find
03637. [x] app\ui\editor\find_replace_bar.py:67 — revisar facet 'nomenclatura clara (PEP8)' em FindReplaceBar._emit_find
03638. [x] app\ui\editor\find_replace_bar.py:67 — revisar facet 'type hints presentes' em FindReplaceBar._emit_find
03639. [x] app\ui\editor\find_replace_bar.py:67 — revisar facet 'tratamento de erros adequado' em FindReplaceBar._emit_find
03640. [x] app\ui\editor\find_replace_bar.py:67 — revisar facet 'sem comentários inline desnecessários' em FindReplaceBar._emit_find
03641. [x] app\ui\editor\find_replace_bar.py:67 — revisar facet 'não imprime side-effects na UI/IO' em FindReplaceBar._emit_find
03642. [x] app\ui\editor\find_replace_bar.py:67 — revisar facet 'thread-safety revisada' em FindReplaceBar._emit_find
03643. [x] app\ui\editor\find_replace_bar.py:67 — revisar facet 'performance (sem loops O(n^2))' em FindReplaceBar._emit_find
03644. [x] app\ui\editor\find_replace_bar.py:67 — revisar facet 'coberto por testes' em FindReplaceBar._emit_find
03645. [x] app\ui\editor\find_replace_bar.py:68 — atribuição: FindReplaceBar._emit_find ← text
03646. [x] app\ui\editor\find_replace_bar.py:69 — controle if em FindReplaceBar._emit_find
03647. [x] app\ui\editor\find_replace_bar.py:72 — definir/revisar FunctionDef: FindReplaceBar._close
03648. [x] app\ui\editor\find_replace_bar.py:72 — revisar facet 'assinatura/args consistentes' em FindReplaceBar._close
03649. [x] app\ui\editor\find_replace_bar.py:72 — revisar facet 'docstring em português' em FindReplaceBar._close
03650. [x] app\ui\editor\find_replace_bar.py:72 — revisar facet 'nomenclatura clara (PEP8)' em FindReplaceBar._close
03651. [x] app\ui\editor\find_replace_bar.py:72 — revisar facet 'type hints presentes' em FindReplaceBar._close
03652. [x] app\ui\editor\find_replace_bar.py:72 — revisar facet 'tratamento de erros adequado' em FindReplaceBar._close
03653. [x] app\ui\editor\find_replace_bar.py:72 — revisar facet 'sem comentários inline desnecessários' em FindReplaceBar._close
03654. [x] app\ui\editor\find_replace_bar.py:72 — revisar facet 'não imprime side-effects na UI/IO' em FindReplaceBar._close
03655. [x] app\ui\editor\find_replace_bar.py:72 — revisar facet 'thread-safety revisada' em FindReplaceBar._close
03656. [x] app\ui\editor\find_replace_bar.py:72 — revisar facet 'performance (sem loops O(n^2))' em FindReplaceBar._close
03657. [x] app\ui\editor\find_replace_bar.py:72 — revisar facet 'coberto por testes' em FindReplaceBar._close
03658. [x] app\ui\editor\find_replace_bar.py:76 — definir/revisar FunctionDef: FindReplaceBar.show_bar
03659. [x] app\ui\editor\find_replace_bar.py:76 — revisar facet 'assinatura/args consistentes' em FindReplaceBar.show_bar
03660. [x] app\ui\editor\find_replace_bar.py:76 — revisar facet 'docstring em português' em FindReplaceBar.show_bar
03661. [x] app\ui\editor\find_replace_bar.py:76 — revisar facet 'nomenclatura clara (PEP8)' em FindReplaceBar.show_bar
03662. [x] app\ui\editor\find_replace_bar.py:76 — revisar facet 'type hints presentes' em FindReplaceBar.show_bar
03663. [x] app\ui\editor\find_replace_bar.py:76 — revisar facet 'tratamento de erros adequado' em FindReplaceBar.show_bar
03664. [x] app\ui\editor\find_replace_bar.py:76 — revisar facet 'sem comentários inline desnecessários' em FindReplaceBar.show_bar
03665. [x] app\ui\editor\find_replace_bar.py:76 — revisar facet 'não imprime side-effects na UI/IO' em FindReplaceBar.show_bar
03666. [x] app\ui\editor\find_replace_bar.py:76 — revisar facet 'thread-safety revisada' em FindReplaceBar.show_bar
03667. [x] app\ui\editor\find_replace_bar.py:76 — revisar facet 'performance (sem loops O(n^2))' em FindReplaceBar.show_bar
03668. [x] app\ui\editor\find_replace_bar.py:76 — revisar facet 'coberto por testes' em FindReplaceBar.show_bar
03669. [x] app\ui\editor\find_replace_bar.py:82 — definir/revisar ClassDef: FindReplaceController
03670. [x] app\ui\editor\find_replace_bar.py:85 — definir/revisar FunctionDef: FindReplaceController.__init__
03671. [x] app\ui\editor\find_replace_bar.py:85 — revisar facet 'assinatura/args consistentes' em FindReplaceController.__init__
03672. [x] app\ui\editor\find_replace_bar.py:85 — revisar facet 'docstring em português' em FindReplaceController.__init__
03673. [x] app\ui\editor\find_replace_bar.py:85 — revisar facet 'nomenclatura clara (PEP8)' em FindReplaceController.__init__
03674. [x] app\ui\editor\find_replace_bar.py:85 — revisar facet 'type hints presentes' em FindReplaceController.__init__
03675. [x] app\ui\editor\find_replace_bar.py:85 — revisar facet 'tratamento de erros adequado' em FindReplaceController.__init__
03676. [x] app\ui\editor\find_replace_bar.py:85 — revisar facet 'sem comentários inline desnecessários' em FindReplaceController.__init__
03677. [x] app\ui\editor\find_replace_bar.py:85 — revisar facet 'não imprime side-effects na UI/IO' em FindReplaceController.__init__
03678. [x] app\ui\editor\find_replace_bar.py:85 — revisar facet 'thread-safety revisada' em FindReplaceController.__init__
03679. [x] app\ui\editor\find_replace_bar.py:85 — revisar facet 'performance (sem loops O(n^2))' em FindReplaceController.__init__
03680. [x] app\ui\editor\find_replace_bar.py:85 — revisar facet 'coberto por testes' em FindReplaceController.__init__
03681. [x] app\ui\editor\find_replace_bar.py:86 — atribuição: FindReplaceController.__init__ ← ?
03682. [x] app\ui\editor\find_replace_bar.py:87 — atribuição: FindReplaceController.__init__ ← ?
03683. [x] app\ui\editor\find_replace_bar.py:88 — atribuição: FindReplaceController.__init__ ← ?
03684. [x] app\ui\editor\find_replace_bar.py:94 — definir/revisar FunctionDef: FindReplaceController.find
03685. [x] app\ui\editor\find_replace_bar.py:94 — revisar facet 'assinatura/args consistentes' em FindReplaceController.find
03686. [x] app\ui\editor\find_replace_bar.py:94 — revisar facet 'docstring em português' em FindReplaceController.find
03687. [x] app\ui\editor\find_replace_bar.py:94 — revisar facet 'nomenclatura clara (PEP8)' em FindReplaceController.find
03688. [x] app\ui\editor\find_replace_bar.py:94 — revisar facet 'type hints presentes' em FindReplaceController.find
03689. [x] app\ui\editor\find_replace_bar.py:94 — revisar facet 'tratamento de erros adequado' em FindReplaceController.find
03690. [x] app\ui\editor\find_replace_bar.py:94 — revisar facet 'sem comentários inline desnecessários' em FindReplaceController.find
03691. [x] app\ui\editor\find_replace_bar.py:94 — revisar facet 'não imprime side-effects na UI/IO' em FindReplaceController.find
03692. [x] app\ui\editor\find_replace_bar.py:94 — revisar facet 'thread-safety revisada' em FindReplaceController.find
03693. [x] app\ui\editor\find_replace_bar.py:94 — revisar facet 'performance (sem loops O(n^2))' em FindReplaceController.find
03694. [x] app\ui\editor\find_replace_bar.py:94 — revisar facet 'coberto por testes' em FindReplaceController.find
03695. [x] app\ui\editor\find_replace_bar.py:95 — atribuição: FindReplaceController.find ← ?
03696. [x] app\ui\editor\find_replace_bar.py:96 — atribuição: FindReplaceController.find ← flags
03697. [x] app\ui\editor\find_replace_bar.py:97 — controle if em FindReplaceController.find
03698. [x] app\ui\editor\find_replace_bar.py:99 — controle if em FindReplaceController.find
03699. [x] app\ui\editor\find_replace_bar.py:100 — atribuição: FindReplaceController.find ← cursor
03700. [x] app\ui\editor\find_replace_bar.py:103 — atribuição: FindReplaceController.find ← found
03701. [x] app\ui\editor\find_replace_bar.py:108 — definir/revisar FunctionDef: FindReplaceController.replace_current
03702. [x] app\ui\editor\find_replace_bar.py:108 — revisar facet 'assinatura/args consistentes' em FindReplaceController.replace_current
03703. [x] app\ui\editor\find_replace_bar.py:108 — revisar facet 'docstring em português' em FindReplaceController.replace_current
03704. [x] app\ui\editor\find_replace_bar.py:108 — revisar facet 'nomenclatura clara (PEP8)' em FindReplaceController.replace_current
03705. [x] app\ui\editor\find_replace_bar.py:108 — revisar facet 'type hints presentes' em FindReplaceController.replace_current
03706. [x] app\ui\editor\find_replace_bar.py:108 — revisar facet 'tratamento de erros adequado' em FindReplaceController.replace_current
03707. [x] app\ui\editor\find_replace_bar.py:108 — revisar facet 'sem comentários inline desnecessários' em FindReplaceController.replace_current
03708. [x] app\ui\editor\find_replace_bar.py:108 — revisar facet 'não imprime side-effects na UI/IO' em FindReplaceController.replace_current
03709. [x] app\ui\editor\find_replace_bar.py:108 — revisar facet 'thread-safety revisada' em FindReplaceController.replace_current
03710. [x] app\ui\editor\find_replace_bar.py:108 — revisar facet 'performance (sem loops O(n^2))' em FindReplaceController.replace_current
03711. [x] app\ui\editor\find_replace_bar.py:108 — revisar facet 'coberto por testes' em FindReplaceController.replace_current
03712. [x] app\ui\editor\find_replace_bar.py:109 — atribuição: FindReplaceController.replace_current ← cursor
03713. [x] app\ui\editor\find_replace_bar.py:110 — atribuição: FindReplaceController.replace_current ← selected
03714. [x] app\ui\editor\find_replace_bar.py:111 — atribuição: FindReplaceController.replace_current ← matches
03715. [x] app\ui\editor\find_replace_bar.py:115 — controle if em FindReplaceController.replace_current
03716. [x] app\ui\editor\find_replace_bar.py:119 — definir/revisar FunctionDef: FindReplaceController.replace_everywhere
03717. [x] app\ui\editor\find_replace_bar.py:119 — revisar facet 'assinatura/args consistentes' em FindReplaceController.replace_everywhere
03718. [x] app\ui\editor\find_replace_bar.py:119 — revisar facet 'docstring em português' em FindReplaceController.replace_everywhere
03719. [x] app\ui\editor\find_replace_bar.py:119 — revisar facet 'nomenclatura clara (PEP8)' em FindReplaceController.replace_everywhere
03720. [x] app\ui\editor\find_replace_bar.py:119 — revisar facet 'type hints presentes' em FindReplaceController.replace_everywhere
03721. [x] app\ui\editor\find_replace_bar.py:119 — revisar facet 'tratamento de erros adequado' em FindReplaceController.replace_everywhere
03722. [x] app\ui\editor\find_replace_bar.py:119 — revisar facet 'sem comentários inline desnecessários' em FindReplaceController.replace_everywhere
03723. [x] app\ui\editor\find_replace_bar.py:119 — revisar facet 'não imprime side-effects na UI/IO' em FindReplaceController.replace_everywhere
03724. [x] app\ui\editor\find_replace_bar.py:119 — revisar facet 'thread-safety revisada' em FindReplaceController.replace_everywhere
03725. [x] app\ui\editor\find_replace_bar.py:119 — revisar facet 'performance (sem loops O(n^2))' em FindReplaceController.replace_everywhere
03726. [x] app\ui\editor\find_replace_bar.py:119 — revisar facet 'coberto por testes' em FindReplaceController.replace_everywhere
03727. [x] app\ui\editor\find_replace_bar.py:120 — atribuição: FindReplaceController.replace_everywhere ← text
03728. [x] app\ui\editor\find_replace_bar.py:121 — controle if em FindReplaceController.replace_everywhere
03729. [x] app\ui\editor\find_replace_bar.py:122 — return em FindReplaceController.replace_everywhere
03730. [x] app\ui\editor\find_replace_bar.py:123 — controle if em FindReplaceController.replace_everywhere
03731. [x] app\ui\editor\find_replace_bar.py:124 — atribuição: FindReplaceController.replace_everywhere ← count
03732. [x] app\ui\editor\find_replace_bar.py:125 — atribuição: FindReplaceController.replace_everywhere ← text
03733. [x] app\ui\editor\find_replace_bar.py:127 — atribuição: FindReplaceController.replace_everywhere ← count
03734. [x] app\ui\editor\find_replace_bar.py:128 — atribuição: FindReplaceController.replace_everywhere ← text
03735. [x] app\ui\editor\find_replace_bar.py:133 — definir/revisar FunctionDef: FindReplaceController._ci_replace
03736. [x] app\ui\editor\find_replace_bar.py:133 — revisar facet 'assinatura/args consistentes' em FindReplaceController._ci_replace
03737. [x] app\ui\editor\find_replace_bar.py:133 — revisar facet 'docstring em português' em FindReplaceController._ci_replace
03738. [x] app\ui\editor\find_replace_bar.py:133 — revisar facet 'nomenclatura clara (PEP8)' em FindReplaceController._ci_replace
03739. [x] app\ui\editor\find_replace_bar.py:133 — revisar facet 'type hints presentes' em FindReplaceController._ci_replace
03740. [x] app\ui\editor\find_replace_bar.py:133 — revisar facet 'tratamento de erros adequado' em FindReplaceController._ci_replace
03741. [x] app\ui\editor\find_replace_bar.py:133 — revisar facet 'sem comentários inline desnecessários' em FindReplaceController._ci_replace
03742. [x] app\ui\editor\find_replace_bar.py:133 — revisar facet 'não imprime side-effects na UI/IO' em FindReplaceController._ci_replace
03743. [x] app\ui\editor\find_replace_bar.py:133 — revisar facet 'thread-safety revisada' em FindReplaceController._ci_replace
03744. [x] app\ui\editor\find_replace_bar.py:133 — revisar facet 'performance (sem loops O(n^2))' em FindReplaceController._ci_replace
03745. [x] app\ui\editor\find_replace_bar.py:133 — revisar facet 'coberto por testes' em FindReplaceController._ci_replace
03746. [x] app\ui\editor\find_replace_bar.py:134 — import: re
03747. [x] app\ui\editor\find_replace_bar.py:136 — return em FindReplaceController._ci_replace
03748. [x] Existência e estrutura do módulo: app\ui\editor\highlighter.py
03749. [x] app\ui\editor\highlighter.py:3 — import: __future__
03750. [x] app\ui\editor\highlighter.py:5 — import: re
03751. [x] app\ui\editor\highlighter.py:7 — import: PySide6.QtGui
03752. [x] app\ui\editor\highlighter.py:9 — atribuição:  ← CMG_KEYWORDS
03753. [x] app\ui\editor\highlighter.py:27 — atribuição:  ← TOKEN_RE
03754. [x] app\ui\editor\highlighter.py:28 — atribuição:  ← KEYWORD_RE
03755. [x] app\ui\editor\highlighter.py:29 — atribuição:  ← COMMENT_RE
03756. [x] app\ui\editor\highlighter.py:30 — atribuição:  ← NUMBER_RE
03757. [x] app\ui\editor\highlighter.py:31 — atribuição:  ← STRING_RE
03758. [x] app\ui\editor\highlighter.py:34 — definir/revisar FunctionDef: token_var_id
03759. [x] app\ui\editor\highlighter.py:34 — revisar facet 'assinatura/args consistentes' em token_var_id
03760. [x] app\ui\editor\highlighter.py:34 — revisar facet 'docstring em português' em token_var_id
03761. [x] app\ui\editor\highlighter.py:34 — revisar facet 'nomenclatura clara (PEP8)' em token_var_id
03762. [x] app\ui\editor\highlighter.py:34 — revisar facet 'type hints presentes' em token_var_id
03763. [x] app\ui\editor\highlighter.py:34 — revisar facet 'tratamento de erros adequado' em token_var_id
03764. [x] app\ui\editor\highlighter.py:34 — revisar facet 'sem comentários inline desnecessários' em token_var_id
03765. [x] app\ui\editor\highlighter.py:34 — revisar facet 'não imprime side-effects na UI/IO' em token_var_id
03766. [x] app\ui\editor\highlighter.py:34 — revisar facet 'thread-safety revisada' em token_var_id
03767. [x] app\ui\editor\highlighter.py:34 — revisar facet 'performance (sem loops O(n^2))' em token_var_id
03768. [x] app\ui\editor\highlighter.py:34 — revisar facet 'coberto por testes' em token_var_id
03769. [x] app\ui\editor\highlighter.py:36 — atribuição: token_var_id ← prefix
03770. [x] app\ui\editor\highlighter.py:37 — return em token_var_id
03771. [x] app\ui\editor\highlighter.py:40 — definir/revisar FunctionDef: var_label
03772. [x] app\ui\editor\highlighter.py:40 — revisar facet 'assinatura/args consistentes' em var_label
03773. [x] app\ui\editor\highlighter.py:40 — revisar facet 'docstring em português' em var_label
03774. [x] app\ui\editor\highlighter.py:40 — revisar facet 'nomenclatura clara (PEP8)' em var_label
03775. [x] app\ui\editor\highlighter.py:40 — revisar facet 'type hints presentes' em var_label
03776. [x] app\ui\editor\highlighter.py:40 — revisar facet 'tratamento de erros adequado' em var_label
03777. [x] app\ui\editor\highlighter.py:40 — revisar facet 'sem comentários inline desnecessários' em var_label
03778. [x] app\ui\editor\highlighter.py:40 — revisar facet 'não imprime side-effects na UI/IO' em var_label
03779. [x] app\ui\editor\highlighter.py:40 — revisar facet 'thread-safety revisada' em var_label
03780. [x] app\ui\editor\highlighter.py:40 — revisar facet 'performance (sem loops O(n^2))' em var_label
03781. [x] app\ui\editor\highlighter.py:40 — revisar facet 'coberto por testes' em var_label
03782. [x] app\ui\editor\highlighter.py:41 — controle if em var_label
03783. [x] app\ui\editor\highlighter.py:42 — return em var_label
03784. [x] app\ui\editor\highlighter.py:43 — return em var_label
03785. [x] app\ui\editor\highlighter.py:46 — definir/revisar ClassDef: DatHighlighter
03786. [x] app\ui\editor\highlighter.py:49 — definir/revisar FunctionDef: DatHighlighter.__init__
03787. [x] app\ui\editor\highlighter.py:49 — revisar facet 'assinatura/args consistentes' em DatHighlighter.__init__
03788. [x] app\ui\editor\highlighter.py:49 — revisar facet 'docstring em português' em DatHighlighter.__init__
03789. [x] app\ui\editor\highlighter.py:49 — revisar facet 'nomenclatura clara (PEP8)' em DatHighlighter.__init__
03790. [x] app\ui\editor\highlighter.py:49 — revisar facet 'type hints presentes' em DatHighlighter.__init__
03791. [x] app\ui\editor\highlighter.py:49 — revisar facet 'tratamento de erros adequado' em DatHighlighter.__init__
03792. [x] app\ui\editor\highlighter.py:49 — revisar facet 'sem comentários inline desnecessários' em DatHighlighter.__init__
03793. [x] app\ui\editor\highlighter.py:49 — revisar facet 'não imprime side-effects na UI/IO' em DatHighlighter.__init__
03794. [x] app\ui\editor\highlighter.py:49 — revisar facet 'thread-safety revisada' em DatHighlighter.__init__
03795. [x] app\ui\editor\highlighter.py:49 — revisar facet 'performance (sem loops O(n^2))' em DatHighlighter.__init__
03796. [x] app\ui\editor\highlighter.py:49 — revisar facet 'coberto por testes' em DatHighlighter.__init__
03797. [x] app\ui\editor\highlighter.py:51 — atribuição: DatHighlighter.__init__ ← ?
03798. [x] app\ui\editor\highlighter.py:52 — atribuição: DatHighlighter.__init__ ← ?
03799. [x] app\ui\editor\highlighter.py:55 — definir/revisar FunctionDef: DatHighlighter._rebuild_formats
03800. [x] app\ui\editor\highlighter.py:55 — revisar facet 'assinatura/args consistentes' em DatHighlighter._rebuild_formats
03801. [x] app\ui\editor\highlighter.py:55 — revisar facet 'docstring em português' em DatHighlighter._rebuild_formats
03802. [x] app\ui\editor\highlighter.py:55 — revisar facet 'nomenclatura clara (PEP8)' em DatHighlighter._rebuild_formats
03803. [x] app\ui\editor\highlighter.py:55 — revisar facet 'type hints presentes' em DatHighlighter._rebuild_formats
03804. [x] app\ui\editor\highlighter.py:55 — revisar facet 'tratamento de erros adequado' em DatHighlighter._rebuild_formats
03805. [x] app\ui\editor\highlighter.py:55 — revisar facet 'sem comentários inline desnecessários' em DatHighlighter._rebuild_formats
03806. [x] app\ui\editor\highlighter.py:55 — revisar facet 'não imprime side-effects na UI/IO' em DatHighlighter._rebuild_formats
03807. [x] app\ui\editor\highlighter.py:55 — revisar facet 'thread-safety revisada' em DatHighlighter._rebuild_formats
03808. [x] app\ui\editor\highlighter.py:55 — revisar facet 'performance (sem loops O(n^2))' em DatHighlighter._rebuild_formats
03809. [x] app\ui\editor\highlighter.py:55 — revisar facet 'coberto por testes' em DatHighlighter._rebuild_formats
03810. [x] app\ui\editor\highlighter.py:56 — import: app.ui.editor.themes
03811. [x] app\ui\editor\highlighter.py:58 — atribuição: DatHighlighter._rebuild_formats ← colors
03812. [x] app\ui\editor\highlighter.py:60 — atribuição: DatHighlighter._rebuild_formats ← ?
03813. [x] app\ui\editor\highlighter.py:64 — atribuição: DatHighlighter._rebuild_formats ← ?
03814. [x] app\ui\editor\highlighter.py:68 — atribuição: DatHighlighter._rebuild_formats ← ?
03815. [x] app\ui\editor\highlighter.py:72 — atribuição: DatHighlighter._rebuild_formats ← ?
03816. [x] app\ui\editor\highlighter.py:77 — atribuição: DatHighlighter._rebuild_formats ← ?
03817. [x] app\ui\editor\highlighter.py:81 — atribuição: DatHighlighter._rebuild_formats ← ?
03818. [x] app\ui\editor\highlighter.py:84 — atribuição: DatHighlighter._rebuild_formats ← ?
03819. [x] app\ui\editor\highlighter.py:87 — definir/revisar FunctionDef: DatHighlighter.apply_theme
03820. [x] app\ui\editor\highlighter.py:87 — revisar facet 'assinatura/args consistentes' em DatHighlighter.apply_theme
03821. [x] app\ui\editor\highlighter.py:87 — revisar facet 'docstring em português' em DatHighlighter.apply_theme
03822. [x] app\ui\editor\highlighter.py:87 — revisar facet 'nomenclatura clara (PEP8)' em DatHighlighter.apply_theme
03823. [x] app\ui\editor\highlighter.py:87 — revisar facet 'type hints presentes' em DatHighlighter.apply_theme
03824. [x] app\ui\editor\highlighter.py:87 — revisar facet 'tratamento de erros adequado' em DatHighlighter.apply_theme
03825. [x] app\ui\editor\highlighter.py:87 — revisar facet 'sem comentários inline desnecessários' em DatHighlighter.apply_theme
03826. [x] app\ui\editor\highlighter.py:87 — revisar facet 'não imprime side-effects na UI/IO' em DatHighlighter.apply_theme
03827. [x] app\ui\editor\highlighter.py:87 — revisar facet 'thread-safety revisada' em DatHighlighter.apply_theme
03828. [x] app\ui\editor\highlighter.py:87 — revisar facet 'performance (sem loops O(n^2))' em DatHighlighter.apply_theme
03829. [x] app\ui\editor\highlighter.py:87 — revisar facet 'coberto por testes' em DatHighlighter.apply_theme
03830. [x] app\ui\editor\highlighter.py:91 — definir/revisar FunctionDef: DatHighlighter.set_variables
03831. [x] app\ui\editor\highlighter.py:91 — revisar facet 'assinatura/args consistentes' em DatHighlighter.set_variables
03832. [x] app\ui\editor\highlighter.py:91 — revisar facet 'docstring em português' em DatHighlighter.set_variables
03833. [x] app\ui\editor\highlighter.py:91 — revisar facet 'nomenclatura clara (PEP8)' em DatHighlighter.set_variables
03834. [x] app\ui\editor\highlighter.py:91 — revisar facet 'type hints presentes' em DatHighlighter.set_variables
03835. [x] app\ui\editor\highlighter.py:91 — revisar facet 'tratamento de erros adequado' em DatHighlighter.set_variables
03836. [x] app\ui\editor\highlighter.py:91 — revisar facet 'sem comentários inline desnecessários' em DatHighlighter.set_variables
03837. [x] app\ui\editor\highlighter.py:91 — revisar facet 'não imprime side-effects na UI/IO' em DatHighlighter.set_variables
03838. [x] app\ui\editor\highlighter.py:91 — revisar facet 'thread-safety revisada' em DatHighlighter.set_variables
03839. [x] app\ui\editor\highlighter.py:91 — revisar facet 'performance (sem loops O(n^2))' em DatHighlighter.set_variables
03840. [x] app\ui\editor\highlighter.py:91 — revisar facet 'coberto por testes' em DatHighlighter.set_variables
03841. [x] app\ui\editor\highlighter.py:92 — atribuição: DatHighlighter.set_variables ← ?
03842. [x] app\ui\editor\highlighter.py:95 — definir/revisar FunctionDef: DatHighlighter.highlightBlock
03843. [x] app\ui\editor\highlighter.py:95 — revisar facet 'assinatura/args consistentes' em DatHighlighter.highlightBlock
03844. [x] app\ui\editor\highlighter.py:95 — revisar facet 'docstring em português' em DatHighlighter.highlightBlock
03845. [x] app\ui\editor\highlighter.py:95 — revisar facet 'nomenclatura clara (PEP8)' em DatHighlighter.highlightBlock
03846. [x] app\ui\editor\highlighter.py:95 — revisar facet 'type hints presentes' em DatHighlighter.highlightBlock
03847. [x] app\ui\editor\highlighter.py:95 — revisar facet 'tratamento de erros adequado' em DatHighlighter.highlightBlock
03848. [x] app\ui\editor\highlighter.py:95 — revisar facet 'sem comentários inline desnecessários' em DatHighlighter.highlightBlock
03849. [x] app\ui\editor\highlighter.py:95 — revisar facet 'não imprime side-effects na UI/IO' em DatHighlighter.highlightBlock
03850. [x] app\ui\editor\highlighter.py:95 — revisar facet 'thread-safety revisada' em DatHighlighter.highlightBlock
03851. [x] app\ui\editor\highlighter.py:95 — revisar facet 'performance (sem loops O(n^2))' em DatHighlighter.highlightBlock
03852. [x] app\ui\editor\highlighter.py:95 — revisar facet 'coberto por testes' em DatHighlighter.highlightBlock
03853. [x] app\ui\editor\highlighter.py:96 — atribuição: DatHighlighter.highlightBlock ← comment_ranges
03854. [x] app\ui\editor\highlighter.py:98 — definir/revisar FunctionDef: DatHighlighter.highlightBlock.in_comment
03855. [x] app\ui\editor\highlighter.py:98 — revisar facet 'assinatura/args consistentes' em DatHighlighter.highlightBlock.in_comment
03856. [x] app\ui\editor\highlighter.py:98 — revisar facet 'docstring em português' em DatHighlighter.highlightBlock.in_comment
03857. [x] app\ui\editor\highlighter.py:98 — revisar facet 'nomenclatura clara (PEP8)' em DatHighlighter.highlightBlock.in_comment
03858. [x] app\ui\editor\highlighter.py:98 — revisar facet 'type hints presentes' em DatHighlighter.highlightBlock.in_comment
03859. [x] app\ui\editor\highlighter.py:98 — revisar facet 'tratamento de erros adequado' em DatHighlighter.highlightBlock.in_comment
03860. [x] app\ui\editor\highlighter.py:98 — revisar facet 'sem comentários inline desnecessários' em DatHighlighter.highlightBlock.in_comment
03861. [x] app\ui\editor\highlighter.py:98 — revisar facet 'não imprime side-effects na UI/IO' em DatHighlighter.highlightBlock.in_comment
03862. [x] app\ui\editor\highlighter.py:98 — revisar facet 'thread-safety revisada' em DatHighlighter.highlightBlock.in_comment
03863. [x] app\ui\editor\highlighter.py:98 — revisar facet 'performance (sem loops O(n^2))' em DatHighlighter.highlightBlock.in_comment
03864. [x] app\ui\editor\highlighter.py:98 — revisar facet 'coberto por testes' em DatHighlighter.highlightBlock.in_comment
03865. [x] app\ui\editor\highlighter.py:99 — return em DatHighlighter.highlightBlock.in_comment
03866. [x] app\ui\editor\highlighter.py:101 — controle for em DatHighlighter.highlightBlock
03867. [x] app\ui\editor\highlighter.py:104 — controle for em DatHighlighter.highlightBlock
03868. [x] app\ui\editor\highlighter.py:105 — controle if em DatHighlighter.highlightBlock
03869. [x] app\ui\editor\highlighter.py:107 — atribuição: DatHighlighter.highlightBlock ← kw
03870. [x] app\ui\editor\highlighter.py:108 — atribuição: DatHighlighter.highlightBlock ← fmt
03871. [x] app\ui\editor\highlighter.py:111 — controle for em DatHighlighter.highlightBlock
03872. [x] app\ui\editor\highlighter.py:112 — controle if em DatHighlighter.highlightBlock
03873. [x] app\ui\editor\highlighter.py:116 — controle for em DatHighlighter.highlightBlock
03874. [x] app\ui\editor\highlighter.py:117 — controle if em DatHighlighter.highlightBlock
03875. [x] app\ui\editor\highlighter.py:119 — atribuição: DatHighlighter.highlightBlock ← color
03876. [x] app\ui\editor\highlighter.py:122 — controle for em DatHighlighter.highlightBlock
03877. [x] app\ui\editor\highlighter.py:123 — controle if em DatHighlighter.highlightBlock
03878. [x] Existência e estrutura do módulo: app\ui\editor\themes.py
03879. [x] app\ui\editor\themes.py:3 — import: __future__
03880. [x] app\ui\editor\themes.py:5 — import: PySide6.QtGui
03881. [x] app\ui\editor\themes.py:6 — import: PySide6.QtCore
03882. [x] app\ui\editor\themes.py:8 — atribuição:  ← DRACULA
03883. [x] app\ui\editor\themes.py:26 — atribuição:  ← LIGHT
03884. [x] app\ui\editor\themes.py:44 — atribuição:  ← THEMES
03885. [x] app\ui\editor\themes.py:48 — atribuição:  ← DEFAULT_THEME
03886. [x] app\ui\editor\themes.py:51 — definir/revisar FunctionDef: theme_colors
03887. [x] app\ui\editor\themes.py:51 — revisar facet 'assinatura/args consistentes' em theme_colors
03888. [x] app\ui\editor\themes.py:51 — revisar facet 'docstring em português' em theme_colors
03889. [x] app\ui\editor\themes.py:51 — revisar facet 'nomenclatura clara (PEP8)' em theme_colors
03890. [x] app\ui\editor\themes.py:51 — revisar facet 'type hints presentes' em theme_colors
03891. [x] app\ui\editor\themes.py:51 — revisar facet 'tratamento de erros adequado' em theme_colors
03892. [x] app\ui\editor\themes.py:51 — revisar facet 'sem comentários inline desnecessários' em theme_colors
03893. [x] app\ui\editor\themes.py:51 — revisar facet 'não imprime side-effects na UI/IO' em theme_colors
03894. [x] app\ui\editor\themes.py:51 — revisar facet 'thread-safety revisada' em theme_colors
03895. [x] app\ui\editor\themes.py:51 — revisar facet 'performance (sem loops O(n^2))' em theme_colors
03896. [x] app\ui\editor\themes.py:51 — revisar facet 'coberto por testes' em theme_colors
03897. [x] app\ui\editor\themes.py:52 — return em theme_colors
03898. [x] app\ui\editor\themes.py:55 — definir/revisar FunctionDef: theme_qcolor
03899. [x] app\ui\editor\themes.py:55 — revisar facet 'assinatura/args consistentes' em theme_qcolor
03900. [x] app\ui\editor\themes.py:55 — revisar facet 'docstring em português' em theme_qcolor
03901. [x] app\ui\editor\themes.py:55 — revisar facet 'nomenclatura clara (PEP8)' em theme_qcolor
03902. [x] app\ui\editor\themes.py:55 — revisar facet 'type hints presentes' em theme_qcolor
03903. [x] app\ui\editor\themes.py:55 — revisar facet 'tratamento de erros adequado' em theme_qcolor
03904. [x] app\ui\editor\themes.py:55 — revisar facet 'sem comentários inline desnecessários' em theme_qcolor
03905. [x] app\ui\editor\themes.py:55 — revisar facet 'não imprime side-effects na UI/IO' em theme_qcolor
03906. [x] app\ui\editor\themes.py:55 — revisar facet 'thread-safety revisada' em theme_qcolor
03907. [x] app\ui\editor\themes.py:55 — revisar facet 'performance (sem loops O(n^2))' em theme_qcolor
03908. [x] app\ui\editor\themes.py:55 — revisar facet 'coberto por testes' em theme_qcolor
03909. [x] app\ui\editor\themes.py:56 — return em theme_qcolor
03910. [x] app\ui\editor\themes.py:59 — definir/revisar FunctionDef: saved_theme
03911. [x] app\ui\editor\themes.py:59 — revisar facet 'assinatura/args consistentes' em saved_theme
03912. [x] app\ui\editor\themes.py:59 — revisar facet 'docstring em português' em saved_theme
03913. [x] app\ui\editor\themes.py:59 — revisar facet 'nomenclatura clara (PEP8)' em saved_theme
03914. [x] app\ui\editor\themes.py:59 — revisar facet 'type hints presentes' em saved_theme
03915. [x] app\ui\editor\themes.py:59 — revisar facet 'tratamento de erros adequado' em saved_theme
03916. [x] app\ui\editor\themes.py:59 — revisar facet 'sem comentários inline desnecessários' em saved_theme
03917. [x] app\ui\editor\themes.py:59 — revisar facet 'não imprime side-effects na UI/IO' em saved_theme
03918. [x] app\ui\editor\themes.py:59 — revisar facet 'thread-safety revisada' em saved_theme
03919. [x] app\ui\editor\themes.py:59 — revisar facet 'performance (sem loops O(n^2))' em saved_theme
03920. [x] app\ui\editor\themes.py:59 — revisar facet 'coberto por testes' em saved_theme
03921. [x] app\ui\editor\themes.py:60 — atribuição: saved_theme ← settings
03922. [x] app\ui\editor\themes.py:61 — return em saved_theme
03923. [x] app\ui\editor\themes.py:64 — definir/revisar FunctionDef: persist_theme
03924. [x] app\ui\editor\themes.py:64 — revisar facet 'assinatura/args consistentes' em persist_theme
03925. [x] app\ui\editor\themes.py:64 — revisar facet 'docstring em português' em persist_theme
03926. [x] app\ui\editor\themes.py:64 — revisar facet 'nomenclatura clara (PEP8)' em persist_theme
03927. [x] app\ui\editor\themes.py:64 — revisar facet 'type hints presentes' em persist_theme
03928. [x] app\ui\editor\themes.py:64 — revisar facet 'tratamento de erros adequado' em persist_theme
03929. [x] app\ui\editor\themes.py:64 — revisar facet 'sem comentários inline desnecessários' em persist_theme
03930. [x] app\ui\editor\themes.py:64 — revisar facet 'não imprime side-effects na UI/IO' em persist_theme
03931. [x] app\ui\editor\themes.py:64 — revisar facet 'thread-safety revisada' em persist_theme
03932. [x] app\ui\editor\themes.py:64 — revisar facet 'performance (sem loops O(n^2))' em persist_theme
03933. [x] app\ui\editor\themes.py:64 — revisar facet 'coberto por testes' em persist_theme
03934. [x] app\ui\editor\themes.py:65 — atribuição: persist_theme ← settings
03935. [x] app\ui\editor\themes.py:69 — atribuição:  ← DEFAULT_FONT_SCALE
03936. [x] app\ui\editor\themes.py:70 — atribuição:  ← MIN_FONT_SCALE
03937. [x] app\ui\editor\themes.py:71 — atribuição:  ← MAX_FONT_SCALE
03938. [x] app\ui\editor\themes.py:72 — atribuição:  ← ZOOM_STEP
03939. [x] app\ui\editor\themes.py:75 — definir/revisar FunctionDef: _clamp_scale
03940. [x] app\ui\editor\themes.py:75 — revisar facet 'assinatura/args consistentes' em _clamp_scale
03941. [x] app\ui\editor\themes.py:75 — revisar facet 'docstring em português' em _clamp_scale
03942. [x] app\ui\editor\themes.py:75 — revisar facet 'nomenclatura clara (PEP8)' em _clamp_scale
03943. [x] app\ui\editor\themes.py:75 — revisar facet 'type hints presentes' em _clamp_scale
03944. [x] app\ui\editor\themes.py:75 — revisar facet 'tratamento de erros adequado' em _clamp_scale
03945. [x] app\ui\editor\themes.py:75 — revisar facet 'sem comentários inline desnecessários' em _clamp_scale
03946. [x] app\ui\editor\themes.py:75 — revisar facet 'não imprime side-effects na UI/IO' em _clamp_scale
03947. [x] app\ui\editor\themes.py:75 — revisar facet 'thread-safety revisada' em _clamp_scale
03948. [x] app\ui\editor\themes.py:75 — revisar facet 'performance (sem loops O(n^2))' em _clamp_scale
03949. [x] app\ui\editor\themes.py:75 — revisar facet 'coberto por testes' em _clamp_scale
03950. [x] app\ui\editor\themes.py:76 — try em _clamp_scale
03951. [x] app\ui\editor\themes.py:77 — atribuição: _clamp_scale ← scale
03952. [x] app\ui\editor\themes.py:79 — atribuição: _clamp_scale ← scale
03953. [x] app\ui\editor\themes.py:80 — return em _clamp_scale
03954. [x] app\ui\editor\themes.py:83 — definir/revisar FunctionDef: saved_font_scale
03955. [x] app\ui\editor\themes.py:83 — revisar facet 'assinatura/args consistentes' em saved_font_scale
03956. [x] app\ui\editor\themes.py:83 — revisar facet 'docstring em português' em saved_font_scale
03957. [x] app\ui\editor\themes.py:83 — revisar facet 'nomenclatura clara (PEP8)' em saved_font_scale
03958. [x] app\ui\editor\themes.py:83 — revisar facet 'type hints presentes' em saved_font_scale
03959. [x] app\ui\editor\themes.py:83 — revisar facet 'tratamento de erros adequado' em saved_font_scale
03960. [x] app\ui\editor\themes.py:83 — revisar facet 'sem comentários inline desnecessários' em saved_font_scale
03961. [x] app\ui\editor\themes.py:83 — revisar facet 'não imprime side-effects na UI/IO' em saved_font_scale
03962. [x] app\ui\editor\themes.py:83 — revisar facet 'thread-safety revisada' em saved_font_scale
03963. [x] app\ui\editor\themes.py:83 — revisar facet 'performance (sem loops O(n^2))' em saved_font_scale
03964. [x] app\ui\editor\themes.py:83 — revisar facet 'coberto por testes' em saved_font_scale
03965. [x] app\ui\editor\themes.py:84 — atribuição: saved_font_scale ← settings
03966. [x] app\ui\editor\themes.py:85 — return em saved_font_scale
03967. [x] app\ui\editor\themes.py:88 — definir/revisar FunctionDef: persist_font_scale
03968. [x] app\ui\editor\themes.py:88 — revisar facet 'assinatura/args consistentes' em persist_font_scale
03969. [x] app\ui\editor\themes.py:88 — revisar facet 'docstring em português' em persist_font_scale
03970. [x] app\ui\editor\themes.py:88 — revisar facet 'nomenclatura clara (PEP8)' em persist_font_scale
03971. [x] app\ui\editor\themes.py:88 — revisar facet 'type hints presentes' em persist_font_scale
03972. [x] app\ui\editor\themes.py:88 — revisar facet 'tratamento de erros adequado' em persist_font_scale
03973. [x] app\ui\editor\themes.py:88 — revisar facet 'sem comentários inline desnecessários' em persist_font_scale
03974. [x] app\ui\editor\themes.py:88 — revisar facet 'não imprime side-effects na UI/IO' em persist_font_scale
03975. [x] app\ui\editor\themes.py:88 — revisar facet 'thread-safety revisada' em persist_font_scale
03976. [x] app\ui\editor\themes.py:88 — revisar facet 'performance (sem loops O(n^2))' em persist_font_scale
03977. [x] app\ui\editor\themes.py:88 — revisar facet 'coberto por testes' em persist_font_scale
03978. [x] app\ui\editor\themes.py:89 — atribuição: persist_font_scale ← settings
03979. [x] app\ui\editor\themes.py:93 — atribuição:  ← DEFAULT_SYSTEM_SCALE
03980. [x] app\ui\editor\themes.py:96 — definir/revisar FunctionDef: saved_system_scale
03981. [x] app\ui\editor\themes.py:96 — revisar facet 'assinatura/args consistentes' em saved_system_scale
03982. [x] app\ui\editor\themes.py:96 — revisar facet 'docstring em português' em saved_system_scale
03983. [x] app\ui\editor\themes.py:96 — revisar facet 'nomenclatura clara (PEP8)' em saved_system_scale
03984. [x] app\ui\editor\themes.py:96 — revisar facet 'type hints presentes' em saved_system_scale
03985. [x] app\ui\editor\themes.py:96 — revisar facet 'tratamento de erros adequado' em saved_system_scale
03986. [x] app\ui\editor\themes.py:96 — revisar facet 'sem comentários inline desnecessários' em saved_system_scale
03987. [x] app\ui\editor\themes.py:96 — revisar facet 'não imprime side-effects na UI/IO' em saved_system_scale
03988. [x] app\ui\editor\themes.py:96 — revisar facet 'thread-safety revisada' em saved_system_scale
03989. [x] app\ui\editor\themes.py:96 — revisar facet 'performance (sem loops O(n^2))' em saved_system_scale
03990. [x] app\ui\editor\themes.py:96 — revisar facet 'coberto por testes' em saved_system_scale
03991. [x] app\ui\editor\themes.py:97 — atribuição: saved_system_scale ← settings
03992. [x] app\ui\editor\themes.py:98 — return em saved_system_scale
03993. [x] app\ui\editor\themes.py:101 — definir/revisar FunctionDef: persist_system_scale
03994. [x] app\ui\editor\themes.py:101 — revisar facet 'assinatura/args consistentes' em persist_system_scale
03995. [x] app\ui\editor\themes.py:101 — revisar facet 'docstring em português' em persist_system_scale
03996. [x] app\ui\editor\themes.py:101 — revisar facet 'nomenclatura clara (PEP8)' em persist_system_scale
03997. [x] app\ui\editor\themes.py:101 — revisar facet 'type hints presentes' em persist_system_scale
03998. [x] app\ui\editor\themes.py:101 — revisar facet 'tratamento de erros adequado' em persist_system_scale
03999. [x] app\ui\editor\themes.py:101 — revisar facet 'sem comentários inline desnecessários' em persist_system_scale
04000. [x] app\ui\editor\themes.py:101 — revisar facet 'não imprime side-effects na UI/IO' em persist_system_scale
04001. [x] app\ui\editor\themes.py:101 — revisar facet 'thread-safety revisada' em persist_system_scale
04002. [x] app\ui\editor\themes.py:101 — revisar facet 'performance (sem loops O(n^2))' em persist_system_scale
04003. [x] app\ui\editor\themes.py:101 — revisar facet 'coberto por testes' em persist_system_scale
04004. [x] app\ui\editor\themes.py:102 — atribuição: persist_system_scale ← settings
04005. [x] Existência e estrutura do módulo: app\ui\main_window.py
04006. [x] app\ui\main_window.py:3 — import: __future__
04007. [x] app\ui\main_window.py:5 — import: PySide6.QtCore
04008. [x] app\ui\main_window.py:6 — import: PySide6.QtGui
04009. [x] app\ui\main_window.py:7 — import: PySide6.QtWidgets
04010. [x] app\ui\main_window.py:23 — import: app.container
04011. [x] app\ui\main_window.py:24 — import: app.core.parsing
04012. [x] app\ui\main_window.py:25 — import: app.domain.entities
04013. [x] app\ui\main_window.py:26 — import: app.domain.events
04014. [x] app\ui\main_window.py:33 — import: app.ui.editor.editor_tabs
04015. [x] app\ui\main_window.py:34 — import: app.ui.widgets.experiments_panel
04016. [x] app\ui\main_window.py:35 — import: app.ui.widgets.logs_panel
04017. [x] app\ui\main_window.py:36 — import: app.ui.widgets.preview_panel
04018. [x] app\ui\main_window.py:37 — import: app.ui.widgets.variables_panel
04019. [x] app\ui\main_window.py:40 — definir/revisar ClassDef: _SampleInputDialog
04020. [x] app\ui\main_window.py:43 — definir/revisar FunctionDef: _SampleInputDialog.__init__
04021. [x] app\ui\main_window.py:43 — revisar facet 'assinatura/args consistentes' em _SampleInputDialog.__init__
04022. [x] app\ui\main_window.py:43 — revisar facet 'docstring em português' em _SampleInputDialog.__init__
04023. [x] app\ui\main_window.py:43 — revisar facet 'nomenclatura clara (PEP8)' em _SampleInputDialog.__init__
04024. [x] app\ui\main_window.py:43 — revisar facet 'type hints presentes' em _SampleInputDialog.__init__
04025. [x] app\ui\main_window.py:43 — revisar facet 'tratamento de erros adequado' em _SampleInputDialog.__init__
04026. [x] app\ui\main_window.py:43 — revisar facet 'sem comentários inline desnecessários' em _SampleInputDialog.__init__
04027. [x] app\ui\main_window.py:43 — revisar facet 'não imprime side-effects na UI/IO' em _SampleInputDialog.__init__
04028. [x] app\ui\main_window.py:43 — revisar facet 'thread-safety revisada' em _SampleInputDialog.__init__
04029. [x] app\ui\main_window.py:43 — revisar facet 'performance (sem loops O(n^2))' em _SampleInputDialog.__init__
04030. [x] app\ui\main_window.py:43 — revisar facet 'coberto por testes' em _SampleInputDialog.__init__
04031. [x] app\ui\main_window.py:47 — atribuição: _SampleInputDialog.__init__ ← form
04032. [x] app\ui\main_window.py:48 — atribuição: _SampleInputDialog.__init__ ← ?
04033. [x] app\ui\main_window.py:51 — atribuição: _SampleInputDialog.__init__ ← ?
04034. [x] app\ui\main_window.py:52 — atribuição: _SampleInputDialog.__init__ ← ?
04035. [x] app\ui\main_window.py:58 — atribuição: _SampleInputDialog.__init__ ← lay
04036. [x] app\ui\main_window.py:60 — atribuição: _SampleInputDialog.__init__ ← buttons
04037. [x] app\ui\main_window.py:67 — definir/revisar FunctionDef: _SampleInputDialog.result_values
04038. [x] app\ui\main_window.py:67 — revisar facet 'assinatura/args consistentes' em _SampleInputDialog.result_values
04039. [x] app\ui\main_window.py:67 — revisar facet 'docstring em português' em _SampleInputDialog.result_values
04040. [x] app\ui\main_window.py:67 — revisar facet 'nomenclatura clara (PEP8)' em _SampleInputDialog.result_values
04041. [x] app\ui\main_window.py:67 — revisar facet 'type hints presentes' em _SampleInputDialog.result_values
04042. [x] app\ui\main_window.py:67 — revisar facet 'tratamento de erros adequado' em _SampleInputDialog.result_values
04043. [x] app\ui\main_window.py:67 — revisar facet 'sem comentários inline desnecessários' em _SampleInputDialog.result_values
04044. [x] app\ui\main_window.py:67 — revisar facet 'não imprime side-effects na UI/IO' em _SampleInputDialog.result_values
04045. [x] app\ui\main_window.py:67 — revisar facet 'thread-safety revisada' em _SampleInputDialog.result_values
04046. [x] app\ui\main_window.py:67 — revisar facet 'performance (sem loops O(n^2))' em _SampleInputDialog.result_values
04047. [x] app\ui\main_window.py:67 — revisar facet 'coberto por testes' em _SampleInputDialog.result_values
04048. [x] app\ui\main_window.py:68 — return em _SampleInputDialog.result_values
04049. [x] app\ui\main_window.py:75 — definir/revisar ClassDef: _StrategyCombo
04050. [x] app\ui\main_window.py:78 — definir/revisar FunctionDef: _StrategyCombo.__init__
04051. [x] app\ui\main_window.py:78 — revisar facet 'assinatura/args consistentes' em _StrategyCombo.__init__
04052. [x] app\ui\main_window.py:78 — revisar facet 'docstring em português' em _StrategyCombo.__init__
04053. [x] app\ui\main_window.py:78 — revisar facet 'nomenclatura clara (PEP8)' em _StrategyCombo.__init__
04054. [x] app\ui\main_window.py:78 — revisar facet 'type hints presentes' em _StrategyCombo.__init__
04055. [x] app\ui\main_window.py:78 — revisar facet 'tratamento de erros adequado' em _StrategyCombo.__init__
04056. [x] app\ui\main_window.py:78 — revisar facet 'sem comentários inline desnecessários' em _StrategyCombo.__init__
04057. [x] app\ui\main_window.py:78 — revisar facet 'não imprime side-effects na UI/IO' em _StrategyCombo.__init__
04058. [x] app\ui\main_window.py:78 — revisar facet 'thread-safety revisada' em _StrategyCombo.__init__
04059. [x] app\ui\main_window.py:78 — revisar facet 'performance (sem loops O(n^2))' em _StrategyCombo.__init__
04060. [x] app\ui\main_window.py:78 — revisar facet 'coberto por testes' em _StrategyCombo.__init__
04061. [x] app\ui\main_window.py:79 — import: PySide6.QtWidgets
04062. [x] app\ui\main_window.py:82 — atribuição: _StrategyCombo.__init__ ← ?
04063. [x] app\ui\main_window.py:84 — atribuição: _StrategyCombo.__init__ ← lay
04064. [x] app\ui\main_window.py:88 — definir/revisar FunctionDef: _StrategyCombo.currentText
04065. [x] app\ui\main_window.py:88 — revisar facet 'assinatura/args consistentes' em _StrategyCombo.currentText
04066. [x] app\ui\main_window.py:88 — revisar facet 'docstring em português' em _StrategyCombo.currentText
04067. [x] app\ui\main_window.py:88 — revisar facet 'nomenclatura clara (PEP8)' em _StrategyCombo.currentText
04068. [x] app\ui\main_window.py:88 — revisar facet 'type hints presentes' em _StrategyCombo.currentText
04069. [x] app\ui\main_window.py:88 — revisar facet 'tratamento de erros adequado' em _StrategyCombo.currentText
04070. [x] app\ui\main_window.py:88 — revisar facet 'sem comentários inline desnecessários' em _StrategyCombo.currentText
04071. [x] app\ui\main_window.py:88 — revisar facet 'não imprime side-effects na UI/IO' em _StrategyCombo.currentText
04072. [x] app\ui\main_window.py:88 — revisar facet 'thread-safety revisada' em _StrategyCombo.currentText
04073. [x] app\ui\main_window.py:88 — revisar facet 'performance (sem loops O(n^2))' em _StrategyCombo.currentText
04074. [x] app\ui\main_window.py:88 — revisar facet 'coberto por testes' em _StrategyCombo.currentText
04075. [x] app\ui\main_window.py:89 — return em _StrategyCombo.currentText
04076. [x] app\ui\main_window.py:92 — definir/revisar ClassDef: MainWindow
04077. [x] app\ui\main_window.py:93 — definir/revisar FunctionDef: MainWindow.__init__
04078. [x] app\ui\main_window.py:93 — revisar facet 'assinatura/args consistentes' em MainWindow.__init__
04079. [x] app\ui\main_window.py:93 — revisar facet 'docstring em português' em MainWindow.__init__
04080. [x] app\ui\main_window.py:93 — revisar facet 'nomenclatura clara (PEP8)' em MainWindow.__init__
04081. [x] app\ui\main_window.py:93 — revisar facet 'type hints presentes' em MainWindow.__init__
04082. [x] app\ui\main_window.py:93 — revisar facet 'tratamento de erros adequado' em MainWindow.__init__
04083. [x] app\ui\main_window.py:93 — revisar facet 'sem comentários inline desnecessários' em MainWindow.__init__
04084. [x] app\ui\main_window.py:93 — revisar facet 'não imprime side-effects na UI/IO' em MainWindow.__init__
04085. [x] app\ui\main_window.py:93 — revisar facet 'thread-safety revisada' em MainWindow.__init__
04086. [x] app\ui\main_window.py:93 — revisar facet 'performance (sem loops O(n^2))' em MainWindow.__init__
04087. [x] app\ui\main_window.py:93 — revisar facet 'coberto por testes' em MainWindow.__init__
04088. [x] app\ui\main_window.py:95 — atribuição: MainWindow.__init__ ← ?
04089. [x] app\ui\main_window.py:96 — atribuição: MainWindow.__init__ ← ?
04090. [x] app\ui\main_window.py:102 — import: PySide6.QtWidgets
04091. [x] app\ui\main_window.py:104 — import: app.ui.editor.themes
04092. [x] app\ui\main_window.py:106 — atribuição: MainWindow.__init__ ← ?
04093. [x] app\ui\main_window.py:107 — atribuição: MainWindow.__init__ ← ?
04094. [x] app\ui\main_window.py:108 — controle if em MainWindow.__init__
04095. [x] app\ui\main_window.py:112 — atribuição: MainWindow.__init__ ← ?
04096. [x] app\ui\main_window.py:113 — atribuição: MainWindow.__init__ ← ?
04097. [x] app\ui\main_window.py:114 — atribuição: MainWindow.__init__ ← ?
04098. [x] app\ui\main_window.py:115 — atribuição: MainWindow.__init__ ← ?
04099. [x] app\ui\main_window.py:118 — import: app.ui.models.repository_paged_model
04100. [x] app\ui\main_window.py:119 — import: app.ui.widgets.experiments_panel
04101. [x] app\ui\main_window.py:121 — atribuição: MainWindow.__init__ ← ?
04102. [x] app\ui\main_window.py:122 — atribuição: MainWindow.__init__ ← ?
04103. [x] app\ui\main_window.py:124 — atribuição: MainWindow.__init__ ← tabs
04104. [x] app\ui\main_window.py:134 — atribuição: MainWindow.__init__ ← ?
04105. [x] app\ui\main_window.py:135 — atribuição: MainWindow.__init__ ← ?
04106. [x] app\ui\main_window.py:148 — definir/revisar FunctionDef: MainWindow._add_dock
04107. [x] app\ui\main_window.py:148 — revisar facet 'assinatura/args consistentes' em MainWindow._add_dock
04108. [x] app\ui\main_window.py:148 — revisar facet 'docstring em português' em MainWindow._add_dock
04109. [x] app\ui\main_window.py:148 — revisar facet 'nomenclatura clara (PEP8)' em MainWindow._add_dock
04110. [x] app\ui\main_window.py:148 — revisar facet 'type hints presentes' em MainWindow._add_dock
04111. [x] app\ui\main_window.py:148 — revisar facet 'tratamento de erros adequado' em MainWindow._add_dock
04112. [x] app\ui\main_window.py:148 — revisar facet 'sem comentários inline desnecessários' em MainWindow._add_dock
04113. [x] app\ui\main_window.py:148 — revisar facet 'não imprime side-effects na UI/IO' em MainWindow._add_dock
04114. [x] app\ui\main_window.py:148 — revisar facet 'thread-safety revisada' em MainWindow._add_dock
04115. [x] app\ui\main_window.py:148 — revisar facet 'performance (sem loops O(n^2))' em MainWindow._add_dock
04116. [x] app\ui\main_window.py:148 — revisar facet 'coberto por testes' em MainWindow._add_dock
04117. [x] app\ui\main_window.py:149 — atribuição: MainWindow._add_dock ← dock
04118. [x] app\ui\main_window.py:152 — return em MainWindow._add_dock
04119. [x] app\ui\main_window.py:154 — definir/revisar FunctionDef: MainWindow._build_menus
04120. [x] app\ui\main_window.py:154 — revisar facet 'assinatura/args consistentes' em MainWindow._build_menus
04121. [x] app\ui\main_window.py:154 — revisar facet 'docstring em português' em MainWindow._build_menus
04122. [x] app\ui\main_window.py:154 — revisar facet 'nomenclatura clara (PEP8)' em MainWindow._build_menus
04123. [x] app\ui\main_window.py:154 — revisar facet 'type hints presentes' em MainWindow._build_menus
04124. [x] app\ui\main_window.py:154 — revisar facet 'tratamento de erros adequado' em MainWindow._build_menus
04125. [x] app\ui\main_window.py:154 — revisar facet 'sem comentários inline desnecessários' em MainWindow._build_menus
04126. [x] app\ui\main_window.py:154 — revisar facet 'não imprime side-effects na UI/IO' em MainWindow._build_menus
04127. [x] app\ui\main_window.py:154 — revisar facet 'thread-safety revisada' em MainWindow._build_menus
04128. [x] app\ui\main_window.py:154 — revisar facet 'performance (sem loops O(n^2))' em MainWindow._build_menus
04129. [x] app\ui\main_window.py:154 — revisar facet 'coberto por testes' em MainWindow._build_menus
04130. [x] app\ui\main_window.py:155 — atribuição: MainWindow._build_menus ← menu_file
04131. [x] app\ui\main_window.py:156 — atribuição: MainWindow._build_menus ← act_new
04132. [x] app\ui\main_window.py:158 — atribuição: MainWindow._build_menus ← act_open
04133. [x] app\ui\main_window.py:160 — atribuição: MainWindow._build_menus ← act_save
04134. [x] app\ui\main_window.py:165 — atribuição: MainWindow._build_menus ← menu_tools
04135. [x] app\ui\main_window.py:166 — atribuição: MainWindow._build_menus ← act_preview
04136. [x] app\ui\main_window.py:168 — atribuição: MainWindow._build_menus ← act_export_builder
04137. [x] app\ui\main_window.py:170 — atribuição: MainWindow._build_menus ← act_logs
04138. [x] app\ui\main_window.py:175 — atribuição: MainWindow._build_menus ← menu_view
04139. [x] app\ui\main_window.py:176 — atribuição: MainWindow._build_menus ← ?
04140. [x] app\ui\main_window.py:177 — import: app.ui.editor.themes
04141. [x] app\ui\main_window.py:179 — controle for em MainWindow._build_menus
04142. [x] app\ui\main_window.py:183 — atribuição: MainWindow._build_menus ← act_theme
04143. [x] app\ui\main_window.py:191 — atribuição: MainWindow._build_menus ← act_zoom_in
04144. [x] app\ui\main_window.py:195 — atribuição: MainWindow._build_menus ← act_zoom_out
04145. [x] app\ui\main_window.py:199 — atribuição: MainWindow._build_menus ← act_zoom_reset
04146. [x] app\ui\main_window.py:205 — atribuição: MainWindow._build_menus ← act_sys_in
04147. [x] app\ui\main_window.py:208 — atribuição: MainWindow._build_menus ← act_sys_out
04148. [x] app\ui\main_window.py:211 — atribuição: MainWindow._build_menus ← act_sys_reset
04149. [x] app\ui\main_window.py:215 — definir/revisar FunctionDef: MainWindow._set_theme
04150. [x] app\ui\main_window.py:215 — revisar facet 'assinatura/args consistentes' em MainWindow._set_theme
04151. [x] app\ui\main_window.py:215 — revisar facet 'docstring em português' em MainWindow._set_theme
04152. [x] app\ui\main_window.py:215 — revisar facet 'nomenclatura clara (PEP8)' em MainWindow._set_theme
04153. [x] app\ui\main_window.py:215 — revisar facet 'type hints presentes' em MainWindow._set_theme
04154. [x] app\ui\main_window.py:215 — revisar facet 'tratamento de erros adequado' em MainWindow._set_theme
04155. [x] app\ui\main_window.py:215 — revisar facet 'sem comentários inline desnecessários' em MainWindow._set_theme
04156. [x] app\ui\main_window.py:215 — revisar facet 'não imprime side-effects na UI/IO' em MainWindow._set_theme
04157. [x] app\ui\main_window.py:215 — revisar facet 'thread-safety revisada' em MainWindow._set_theme
04158. [x] app\ui\main_window.py:215 — revisar facet 'performance (sem loops O(n^2))' em MainWindow._set_theme
04159. [x] app\ui\main_window.py:215 — revisar facet 'coberto por testes' em MainWindow._set_theme
04160. [x] app\ui\main_window.py:216 — import: app.ui.editor.themes
04161. [x] app\ui\main_window.py:218 — controle for em MainWindow._set_theme
04162. [x] app\ui\main_window.py:219 — atribuição: MainWindow._set_theme ← tab
04163. [x] app\ui\main_window.py:220 — controle if em MainWindow._set_theme
04164. [x] app\ui\main_window.py:225 — definir/revisar FunctionDef: MainWindow._zoom_editors
04165. [x] app\ui\main_window.py:225 — revisar facet 'assinatura/args consistentes' em MainWindow._zoom_editors
04166. [x] app\ui\main_window.py:225 — revisar facet 'docstring em português' em MainWindow._zoom_editors
04167. [x] app\ui\main_window.py:225 — revisar facet 'nomenclatura clara (PEP8)' em MainWindow._zoom_editors
04168. [x] app\ui\main_window.py:225 — revisar facet 'type hints presentes' em MainWindow._zoom_editors
04169. [x] app\ui\main_window.py:225 — revisar facet 'tratamento de erros adequado' em MainWindow._zoom_editors
04170. [x] app\ui\main_window.py:225 — revisar facet 'sem comentários inline desnecessários' em MainWindow._zoom_editors
04171. [x] app\ui\main_window.py:225 — revisar facet 'não imprime side-effects na UI/IO' em MainWindow._zoom_editors
04172. [x] app\ui\main_window.py:225 — revisar facet 'thread-safety revisada' em MainWindow._zoom_editors
04173. [x] app\ui\main_window.py:225 — revisar facet 'performance (sem loops O(n^2))' em MainWindow._zoom_editors
04174. [x] app\ui\main_window.py:225 — revisar facet 'coberto por testes' em MainWindow._zoom_editors
04175. [x] app\ui\main_window.py:226 — controle for em MainWindow._zoom_editors
04176. [x] app\ui\main_window.py:227 — atribuição: MainWindow._zoom_editors ← tab
04177. [x] app\ui\main_window.py:228 — controle if em MainWindow._zoom_editors
04178. [x] app\ui\main_window.py:231 — definir/revisar FunctionDef: MainWindow._reset_zoom_editors
04179. [x] app\ui\main_window.py:231 — revisar facet 'assinatura/args consistentes' em MainWindow._reset_zoom_editors
04180. [x] app\ui\main_window.py:231 — revisar facet 'docstring em português' em MainWindow._reset_zoom_editors
04181. [x] app\ui\main_window.py:231 — revisar facet 'nomenclatura clara (PEP8)' em MainWindow._reset_zoom_editors
04182. [x] app\ui\main_window.py:231 — revisar facet 'type hints presentes' em MainWindow._reset_zoom_editors
04183. [x] app\ui\main_window.py:231 — revisar facet 'tratamento de erros adequado' em MainWindow._reset_zoom_editors
04184. [x] app\ui\main_window.py:231 — revisar facet 'sem comentários inline desnecessários' em MainWindow._reset_zoom_editors
04185. [x] app\ui\main_window.py:231 — revisar facet 'não imprime side-effects na UI/IO' em MainWindow._reset_zoom_editors
04186. [x] app\ui\main_window.py:231 — revisar facet 'thread-safety revisada' em MainWindow._reset_zoom_editors
04187. [x] app\ui\main_window.py:231 — revisar facet 'performance (sem loops O(n^2))' em MainWindow._reset_zoom_editors
04188. [x] app\ui\main_window.py:231 — revisar facet 'coberto por testes' em MainWindow._reset_zoom_editors
04189. [x] app\ui\main_window.py:232 — controle for em MainWindow._reset_zoom_editors
04190. [x] app\ui\main_window.py:233 — atribuição: MainWindow._reset_zoom_editors ← tab
04191. [x] app\ui\main_window.py:234 — controle if em MainWindow._reset_zoom_editors
04192. [x] app\ui\main_window.py:238 — definir/revisar FunctionDef: MainWindow._apply_system_font
04193. [x] app\ui\main_window.py:238 — revisar facet 'assinatura/args consistentes' em MainWindow._apply_system_font
04194. [x] app\ui\main_window.py:238 — revisar facet 'docstring em português' em MainWindow._apply_system_font
04195. [x] app\ui\main_window.py:238 — revisar facet 'nomenclatura clara (PEP8)' em MainWindow._apply_system_font
04196. [x] app\ui\main_window.py:238 — revisar facet 'type hints presentes' em MainWindow._apply_system_font
04197. [x] app\ui\main_window.py:238 — revisar facet 'tratamento de erros adequado' em MainWindow._apply_system_font
04198. [x] app\ui\main_window.py:238 — revisar facet 'sem comentários inline desnecessários' em MainWindow._apply_system_font
04199. [x] app\ui\main_window.py:238 — revisar facet 'não imprime side-effects na UI/IO' em MainWindow._apply_system_font
04200. [x] app\ui\main_window.py:238 — revisar facet 'thread-safety revisada' em MainWindow._apply_system_font
04201. [x] app\ui\main_window.py:238 — revisar facet 'performance (sem loops O(n^2))' em MainWindow._apply_system_font
04202. [x] app\ui\main_window.py:238 — revisar facet 'coberto por testes' em MainWindow._apply_system_font
04203. [x] app\ui\main_window.py:239 — import: PySide6.QtGui
04204. [x] app\ui\main_window.py:240 — import: PySide6.QtWidgets
04205. [x] app\ui\main_window.py:242 — atribuição: MainWindow._apply_system_font ← app
04206. [x] app\ui\main_window.py:243 — atribuição: MainWindow._apply_system_font ← base
04207. [x] app\ui\main_window.py:244 — atribuição: MainWindow._apply_system_font ← font
04208. [x] app\ui\main_window.py:248 — definir/revisar FunctionDef: MainWindow._change_system_font
04209. [x] app\ui\main_window.py:248 — revisar facet 'assinatura/args consistentes' em MainWindow._change_system_font
04210. [x] app\ui\main_window.py:248 — revisar facet 'docstring em português' em MainWindow._change_system_font
04211. [x] app\ui\main_window.py:248 — revisar facet 'nomenclatura clara (PEP8)' em MainWindow._change_system_font
04212. [x] app\ui\main_window.py:248 — revisar facet 'type hints presentes' em MainWindow._change_system_font
04213. [x] app\ui\main_window.py:248 — revisar facet 'tratamento de erros adequado' em MainWindow._change_system_font
04214. [x] app\ui\main_window.py:248 — revisar facet 'sem comentários inline desnecessários' em MainWindow._change_system_font
04215. [x] app\ui\main_window.py:248 — revisar facet 'não imprime side-effects na UI/IO' em MainWindow._change_system_font
04216. [x] app\ui\main_window.py:248 — revisar facet 'thread-safety revisada' em MainWindow._change_system_font
04217. [x] app\ui\main_window.py:248 — revisar facet 'performance (sem loops O(n^2))' em MainWindow._change_system_font
04218. [x] app\ui\main_window.py:248 — revisar facet 'coberto por testes' em MainWindow._change_system_font
04219. [x] app\ui\main_window.py:249 — import: app.ui.editor.themes
04220. [x] app\ui\main_window.py:251 — controle if em MainWindow._change_system_font
04221. [x] app\ui\main_window.py:252 — atribuição: MainWindow._change_system_font ← ?
04222. [x] app\ui\main_window.py:254 — atribuição: MainWindow._change_system_font ← ?
04223. [x] app\ui\main_window.py:258 — definir/revisar FunctionDef: MainWindow._reset_system_font
04224. [x] app\ui\main_window.py:258 — revisar facet 'assinatura/args consistentes' em MainWindow._reset_system_font
04225. [x] app\ui\main_window.py:258 — revisar facet 'docstring em português' em MainWindow._reset_system_font
04226. [x] app\ui\main_window.py:258 — revisar facet 'nomenclatura clara (PEP8)' em MainWindow._reset_system_font
04227. [x] app\ui\main_window.py:258 — revisar facet 'type hints presentes' em MainWindow._reset_system_font
04228. [x] app\ui\main_window.py:258 — revisar facet 'tratamento de erros adequado' em MainWindow._reset_system_font
04229. [x] app\ui\main_window.py:258 — revisar facet 'sem comentários inline desnecessários' em MainWindow._reset_system_font
04230. [x] app\ui\main_window.py:258 — revisar facet 'não imprime side-effects na UI/IO' em MainWindow._reset_system_font
04231. [x] app\ui\main_window.py:258 — revisar facet 'thread-safety revisada' em MainWindow._reset_system_font
04232. [x] app\ui\main_window.py:258 — revisar facet 'performance (sem loops O(n^2))' em MainWindow._reset_system_font
04233. [x] app\ui\main_window.py:258 — revisar facet 'coberto por testes' em MainWindow._reset_system_font
04234. [x] app\ui\main_window.py:259 — import: app.ui.editor.themes
04235. [x] app\ui\main_window.py:261 — atribuição: MainWindow._reset_system_font ← ?
04236. [x] app\ui\main_window.py:266 — definir/revisar FunctionDef: MainWindow._open_batch_export
04237. [x] app\ui\main_window.py:266 — revisar facet 'assinatura/args consistentes' em MainWindow._open_batch_export
04238. [x] app\ui\main_window.py:266 — revisar facet 'docstring em português' em MainWindow._open_batch_export
04239. [x] app\ui\main_window.py:266 — revisar facet 'nomenclatura clara (PEP8)' em MainWindow._open_batch_export
04240. [x] app\ui\main_window.py:266 — revisar facet 'type hints presentes' em MainWindow._open_batch_export
04241. [x] app\ui\main_window.py:266 — revisar facet 'tratamento de erros adequado' em MainWindow._open_batch_export
04242. [x] app\ui\main_window.py:266 — revisar facet 'sem comentários inline desnecessários' em MainWindow._open_batch_export
04243. [x] app\ui\main_window.py:266 — revisar facet 'não imprime side-effects na UI/IO' em MainWindow._open_batch_export
04244. [x] app\ui\main_window.py:266 — revisar facet 'thread-safety revisada' em MainWindow._open_batch_export
04245. [x] app\ui\main_window.py:266 — revisar facet 'performance (sem loops O(n^2))' em MainWindow._open_batch_export
04246. [x] app\ui\main_window.py:266 — revisar facet 'coberto por testes' em MainWindow._open_batch_export
04247. [x] app\ui\main_window.py:267 — atribuição: MainWindow._open_batch_export ← container
04248. [x] app\ui\main_window.py:268 — atribuição: MainWindow._open_batch_export ← batches
04249. [x] app\ui\main_window.py:269 — atribuição: MainWindow._open_batch_export ← versions
04250. [x] app\ui\main_window.py:270 — controle for em MainWindow._open_batch_export
04251. [x] app\ui\main_window.py:271 — atribuição: MainWindow._open_batch_export ← template_id
04252. [x] app\ui\main_window.py:272 — atribuição: MainWindow._open_batch_export ← versions_list
04253. [x] app\ui\main_window.py:273 — controle for em MainWindow._open_batch_export
04254. [x] app\ui\main_window.py:275 — controle if em MainWindow._open_batch_export
04255. [x] app\ui\main_window.py:279 — return em MainWindow._open_batch_export
04256. [x] app\ui\main_window.py:280 — controle if em MainWindow._open_batch_export
04257. [x] app\ui\main_window.py:284 — return em MainWindow._open_batch_export
04258. [x] app\ui\main_window.py:286 — import: app.ui.widgets.batch_export_dialog
04259. [x] app\ui\main_window.py:288 — atribuição: MainWindow._open_batch_export ← dialog
04260. [x] app\ui\main_window.py:292 — definir/revisar FunctionDef: MainWindow._start_batch_export
04261. [x] app\ui\main_window.py:292 — revisar facet 'assinatura/args consistentes' em MainWindow._start_batch_export
04262. [x] app\ui\main_window.py:292 — revisar facet 'docstring em português' em MainWindow._start_batch_export
04263. [x] app\ui\main_window.py:292 — revisar facet 'nomenclatura clara (PEP8)' em MainWindow._start_batch_export
04264. [x] app\ui\main_window.py:292 — revisar facet 'type hints presentes' em MainWindow._start_batch_export
04265. [x] app\ui\main_window.py:292 — revisar facet 'tratamento de erros adequado' em MainWindow._start_batch_export
04266. [x] app\ui\main_window.py:292 — revisar facet 'sem comentários inline desnecessários' em MainWindow._start_batch_export
04267. [x] app\ui\main_window.py:292 — revisar facet 'não imprime side-effects na UI/IO' em MainWindow._start_batch_export
04268. [x] app\ui\main_window.py:292 — revisar facet 'thread-safety revisada' em MainWindow._start_batch_export
04269. [x] app\ui\main_window.py:292 — revisar facet 'performance (sem loops O(n^2))' em MainWindow._start_batch_export
04270. [x] app\ui\main_window.py:292 — revisar facet 'coberto por testes' em MainWindow._start_batch_export
04271. [x] app\ui\main_window.py:293 — import: PySide6.QtWidgets
04272. [x] app\ui\main_window.py:295 — import: app.workers.batch_export_worker
04273. [x] app\ui\main_window.py:297 — atribuição: MainWindow._start_batch_export ← ?
04274. [x] app\ui\main_window.py:298 — atribuição: MainWindow._start_batch_export ← ?
04275. [x] app\ui\main_window.py:306 — atribuição: MainWindow._start_batch_export ← progress_dialog
04276. [x] app\ui\main_window.py:310 — atribuição: MainWindow._start_batch_export ← ?
04277. [x] app\ui\main_window.py:318 — definir/revisar FunctionDef: MainWindow._on_batch_export_done
04278. [x] app\ui\main_window.py:318 — revisar facet 'assinatura/args consistentes' em MainWindow._on_batch_export_done
04279. [x] app\ui\main_window.py:318 — revisar facet 'docstring em português' em MainWindow._on_batch_export_done
04280. [x] app\ui\main_window.py:318 — revisar facet 'nomenclatura clara (PEP8)' em MainWindow._on_batch_export_done
04281. [x] app\ui\main_window.py:318 — revisar facet 'type hints presentes' em MainWindow._on_batch_export_done
04282. [x] app\ui\main_window.py:318 — revisar facet 'tratamento de erros adequado' em MainWindow._on_batch_export_done
04283. [x] app\ui\main_window.py:318 — revisar facet 'sem comentários inline desnecessários' em MainWindow._on_batch_export_done
04284. [x] app\ui\main_window.py:318 — revisar facet 'não imprime side-effects na UI/IO' em MainWindow._on_batch_export_done
04285. [x] app\ui\main_window.py:318 — revisar facet 'thread-safety revisada' em MainWindow._on_batch_export_done
04286. [x] app\ui\main_window.py:318 — revisar facet 'performance (sem loops O(n^2))' em MainWindow._on_batch_export_done
04287. [x] app\ui\main_window.py:318 — revisar facet 'coberto por testes' em MainWindow._on_batch_export_done
04288. [x] app\ui\main_window.py:319 — controle if em MainWindow._on_batch_export_done
04289. [x] app\ui\main_window.py:322 — atribuição: MainWindow._on_batch_export_done ← container
04290. [x] app\ui\main_window.py:324 — import: app.ui.widgets.export_done_dialog
04291. [x] app\ui\main_window.py:326 — atribuição: MainWindow._on_batch_export_done ← dialog
04292. [x] app\ui\main_window.py:329 — definir/revisar FunctionDef: MainWindow._on_batch_export_failed
04293. [x] app\ui\main_window.py:329 — revisar facet 'assinatura/args consistentes' em MainWindow._on_batch_export_failed
04294. [x] app\ui\main_window.py:329 — revisar facet 'docstring em português' em MainWindow._on_batch_export_failed
04295. [x] app\ui\main_window.py:329 — revisar facet 'nomenclatura clara (PEP8)' em MainWindow._on_batch_export_failed
04296. [x] app\ui\main_window.py:329 — revisar facet 'type hints presentes' em MainWindow._on_batch_export_failed
04297. [x] app\ui\main_window.py:329 — revisar facet 'tratamento de erros adequado' em MainWindow._on_batch_export_failed
04298. [x] app\ui\main_window.py:329 — revisar facet 'sem comentários inline desnecessários' em MainWindow._on_batch_export_failed
04299. [x] app\ui\main_window.py:329 — revisar facet 'não imprime side-effects na UI/IO' em MainWindow._on_batch_export_failed
04300. [x] app\ui\main_window.py:329 — revisar facet 'thread-safety revisada' em MainWindow._on_batch_export_failed
04301. [x] app\ui\main_window.py:329 — revisar facet 'performance (sem loops O(n^2))' em MainWindow._on_batch_export_failed
04302. [x] app\ui\main_window.py:329 — revisar facet 'coberto por testes' em MainWindow._on_batch_export_failed
04303. [x] app\ui\main_window.py:330 — controle if em MainWindow._on_batch_export_failed
04304. [x] app\ui\main_window.py:335 — definir/revisar FunctionDef: MainWindow._wire_events
04305. [x] app\ui\main_window.py:335 — revisar facet 'assinatura/args consistentes' em MainWindow._wire_events
04306. [x] app\ui\main_window.py:335 — revisar facet 'docstring em português' em MainWindow._wire_events
04307. [x] app\ui\main_window.py:335 — revisar facet 'nomenclatura clara (PEP8)' em MainWindow._wire_events
04308. [x] app\ui\main_window.py:335 — revisar facet 'type hints presentes' em MainWindow._wire_events
04309. [x] app\ui\main_window.py:335 — revisar facet 'tratamento de erros adequado' em MainWindow._wire_events
04310. [x] app\ui\main_window.py:335 — revisar facet 'sem comentários inline desnecessários' em MainWindow._wire_events
04311. [x] app\ui\main_window.py:335 — revisar facet 'não imprime side-effects na UI/IO' em MainWindow._wire_events
04312. [x] app\ui\main_window.py:335 — revisar facet 'thread-safety revisada' em MainWindow._wire_events
04313. [x] app\ui\main_window.py:335 — revisar facet 'performance (sem loops O(n^2))' em MainWindow._wire_events
04314. [x] app\ui\main_window.py:335 — revisar facet 'coberto por testes' em MainWindow._wire_events
04315. [x] app\ui\main_window.py:336 — atribuição: MainWindow._wire_events ← bus
04316. [x] app\ui\main_window.py:355 — definir/revisar FunctionDef: MainWindow._compare_experiments
04317. [x] app\ui\main_window.py:355 — revisar facet 'assinatura/args consistentes' em MainWindow._compare_experiments
04318. [x] app\ui\main_window.py:355 — revisar facet 'docstring em português' em MainWindow._compare_experiments
04319. [x] app\ui\main_window.py:355 — revisar facet 'nomenclatura clara (PEP8)' em MainWindow._compare_experiments
04320. [x] app\ui\main_window.py:355 — revisar facet 'type hints presentes' em MainWindow._compare_experiments
04321. [x] app\ui\main_window.py:355 — revisar facet 'tratamento de erros adequado' em MainWindow._compare_experiments
04322. [x] app\ui\main_window.py:355 — revisar facet 'sem comentários inline desnecessários' em MainWindow._compare_experiments
04323. [x] app\ui\main_window.py:355 — revisar facet 'não imprime side-effects na UI/IO' em MainWindow._compare_experiments
04324. [x] app\ui\main_window.py:355 — revisar facet 'thread-safety revisada' em MainWindow._compare_experiments
04325. [x] app\ui\main_window.py:355 — revisar facet 'performance (sem loops O(n^2))' em MainWindow._compare_experiments
04326. [x] app\ui\main_window.py:355 — revisar facet 'coberto por testes' em MainWindow._compare_experiments
04327. [x] app\ui\main_window.py:357 — atribuição: MainWindow._compare_experiments ← text
04328. [x] app\ui\main_window.py:358 — try em MainWindow._compare_experiments
04329. [x] app\ui\main_window.py:359 — atribuição: MainWindow._compare_experiments ← result
04330. [x] app\ui\main_window.py:366 — import: app.ui.widgets.comparison_dialog
04331. [x] app\ui\main_window.py:373 — definir/revisar FunctionDef: MainWindow._sync_variables
04332. [x] app\ui\main_window.py:373 — revisar facet 'assinatura/args consistentes' em MainWindow._sync_variables
04333. [x] app\ui\main_window.py:373 — revisar facet 'docstring em português' em MainWindow._sync_variables
04334. [x] app\ui\main_window.py:373 — revisar facet 'nomenclatura clara (PEP8)' em MainWindow._sync_variables
04335. [x] app\ui\main_window.py:373 — revisar facet 'type hints presentes' em MainWindow._sync_variables
04336. [x] app\ui\main_window.py:373 — revisar facet 'tratamento de erros adequado' em MainWindow._sync_variables
04337. [x] app\ui\main_window.py:373 — revisar facet 'sem comentários inline desnecessários' em MainWindow._sync_variables
04338. [x] app\ui\main_window.py:373 — revisar facet 'não imprime side-effects na UI/IO' em MainWindow._sync_variables
04339. [x] app\ui\main_window.py:373 — revisar facet 'thread-safety revisada' em MainWindow._sync_variables
04340. [x] app\ui\main_window.py:373 — revisar facet 'performance (sem loops O(n^2))' em MainWindow._sync_variables
04341. [x] app\ui\main_window.py:373 — revisar facet 'coberto por testes' em MainWindow._sync_variables
04342. [x] app\ui\main_window.py:374 — atribuição: MainWindow._sync_variables ← editor
04343. [x] app\ui\main_window.py:375 — controle if em MainWindow._sync_variables
04344. [x] app\ui\main_window.py:376 — return em MainWindow._sync_variables
04345. [x] app\ui\main_window.py:379 — definir/revisar FunctionDef: MainWindow._current_text
04346. [x] app\ui\main_window.py:379 — revisar facet 'assinatura/args consistentes' em MainWindow._current_text
04347. [x] app\ui\main_window.py:379 — revisar facet 'docstring em português' em MainWindow._current_text
04348. [x] app\ui\main_window.py:379 — revisar facet 'nomenclatura clara (PEP8)' em MainWindow._current_text
04349. [x] app\ui\main_window.py:379 — revisar facet 'type hints presentes' em MainWindow._current_text
04350. [x] app\ui\main_window.py:379 — revisar facet 'tratamento de erros adequado' em MainWindow._current_text
04351. [x] app\ui\main_window.py:379 — revisar facet 'sem comentários inline desnecessários' em MainWindow._current_text
04352. [x] app\ui\main_window.py:379 — revisar facet 'não imprime side-effects na UI/IO' em MainWindow._current_text
04353. [x] app\ui\main_window.py:379 — revisar facet 'thread-safety revisada' em MainWindow._current_text
04354. [x] app\ui\main_window.py:379 — revisar facet 'performance (sem loops O(n^2))' em MainWindow._current_text
04355. [x] app\ui\main_window.py:379 — revisar facet 'coberto por testes' em MainWindow._current_text
04356. [x] app\ui\main_window.py:380 — atribuição: MainWindow._current_text ← editor
04357. [x] app\ui\main_window.py:381 — return em MainWindow._current_text
04358. [x] app\ui\main_window.py:384 — definir/revisar FunctionDef: MainWindow._run_sampling
04359. [x] app\ui\main_window.py:384 — revisar facet 'assinatura/args consistentes' em MainWindow._run_sampling
04360. [x] app\ui\main_window.py:384 — revisar facet 'docstring em português' em MainWindow._run_sampling
04361. [x] app\ui\main_window.py:384 — revisar facet 'nomenclatura clara (PEP8)' em MainWindow._run_sampling
04362. [x] app\ui\main_window.py:384 — revisar facet 'type hints presentes' em MainWindow._run_sampling
04363. [x] app\ui\main_window.py:384 — revisar facet 'tratamento de erros adequado' em MainWindow._run_sampling
04364. [x] app\ui\main_window.py:384 — revisar facet 'sem comentários inline desnecessários' em MainWindow._run_sampling
04365. [x] app\ui\main_window.py:384 — revisar facet 'não imprime side-effects na UI/IO' em MainWindow._run_sampling
04366. [x] app\ui\main_window.py:384 — revisar facet 'thread-safety revisada' em MainWindow._run_sampling
04367. [x] app\ui\main_window.py:384 — revisar facet 'performance (sem loops O(n^2))' em MainWindow._run_sampling
04368. [x] app\ui\main_window.py:384 — revisar facet 'coberto por testes' em MainWindow._run_sampling
04369. [x] app\ui\main_window.py:385 — atribuição: MainWindow._run_sampling ← text
04370. [x] app\ui\main_window.py:386 — controle if em MainWindow._run_sampling
04371. [x] app\ui\main_window.py:388 — return em MainWindow._run_sampling
04372. [x] app\ui\main_window.py:390 — atribuição: MainWindow._run_sampling ← var_ids
04373. [x] app\ui\main_window.py:391 — controle if em MainWindow._run_sampling
04374. [x] app\ui\main_window.py:393 — return em MainWindow._run_sampling
04375. [x] app\ui\main_window.py:400 — atribuição: MainWindow._run_sampling ← missing
04376. [x] app\ui\main_window.py:401 — controle if em MainWindow._run_sampling
04377. [x] app\ui\main_window.py:408 — return em MainWindow._run_sampling
04378. [x] app\ui\main_window.py:410 — atribuição: MainWindow._run_sampling ← dialog
04379. [x] app\ui\main_window.py:411 — controle if em MainWindow._run_sampling
04380. [x] app\ui\main_window.py:412 — return em MainWindow._run_sampling
04381. [x] app\ui\main_window.py:413 — atribuição: MainWindow._run_sampling ← ?
04382. [x] app\ui\main_window.py:415 — atribuição: MainWindow._run_sampling ← request
04383. [x] app\ui\main_window.py:424 — import: app.workers.sampling_worker
04384. [x] app\ui\main_window.py:426 — atribuição: MainWindow._run_sampling ← ?
04385. [x] app\ui\main_window.py:434 — definir/revisar FunctionDef: MainWindow._on_sampling_completed
04386. [x] app\ui\main_window.py:434 — revisar facet 'assinatura/args consistentes' em MainWindow._on_sampling_completed
04387. [x] app\ui\main_window.py:434 — revisar facet 'docstring em português' em MainWindow._on_sampling_completed
04388. [x] app\ui\main_window.py:434 — revisar facet 'nomenclatura clara (PEP8)' em MainWindow._on_sampling_completed
04389. [x] app\ui\main_window.py:434 — revisar facet 'type hints presentes' em MainWindow._on_sampling_completed
04390. [x] app\ui\main_window.py:434 — revisar facet 'tratamento de erros adequado' em MainWindow._on_sampling_completed
04391. [x] app\ui\main_window.py:434 — revisar facet 'sem comentários inline desnecessários' em MainWindow._on_sampling_completed
04392. [x] app\ui\main_window.py:434 — revisar facet 'não imprime side-effects na UI/IO' em MainWindow._on_sampling_completed
04393. [x] app\ui\main_window.py:434 — revisar facet 'thread-safety revisada' em MainWindow._on_sampling_completed
04394. [x] app\ui\main_window.py:434 — revisar facet 'performance (sem loops O(n^2))' em MainWindow._on_sampling_completed
04395. [x] app\ui\main_window.py:434 — revisar facet 'coberto por testes' em MainWindow._on_sampling_completed
04396. [x] app\ui\main_window.py:435 — atribuição: MainWindow._on_sampling_completed ← ?
04397. [x] app\ui\main_window.py:439 — atribuição: MainWindow._on_sampling_completed ← specs
04398. [x] app\ui\main_window.py:440 — atribuição: MainWindow._on_sampling_completed ← names
04399. [x] app\ui\main_window.py:441 — controle for em MainWindow._on_sampling_completed
04400. [x] app\ui\main_window.py:442 — atribuição: MainWindow._on_sampling_completed ← editor
04401. [x] app\ui\main_window.py:443 — controle if em MainWindow._on_sampling_completed
04402. [x] app\ui\main_window.py:446 — import: time
04403. [x] app\ui\main_window.py:448 — atribuição: MainWindow._on_sampling_completed ← batch_id
04404. [x] app\ui\main_window.py:459 — definir/revisar FunctionDef: MainWindow._on_sampling_failed
04405. [x] app\ui\main_window.py:459 — revisar facet 'assinatura/args consistentes' em MainWindow._on_sampling_failed
04406. [x] app\ui\main_window.py:459 — revisar facet 'docstring em português' em MainWindow._on_sampling_failed
04407. [x] app\ui\main_window.py:459 — revisar facet 'nomenclatura clara (PEP8)' em MainWindow._on_sampling_failed
04408. [x] app\ui\main_window.py:459 — revisar facet 'type hints presentes' em MainWindow._on_sampling_failed
04409. [x] app\ui\main_window.py:459 — revisar facet 'tratamento de erros adequado' em MainWindow._on_sampling_failed
04410. [x] app\ui\main_window.py:459 — revisar facet 'sem comentários inline desnecessários' em MainWindow._on_sampling_failed
04411. [x] app\ui\main_window.py:459 — revisar facet 'não imprime side-effects na UI/IO' em MainWindow._on_sampling_failed
04412. [x] app\ui\main_window.py:459 — revisar facet 'thread-safety revisada' em MainWindow._on_sampling_failed
04413. [x] app\ui\main_window.py:459 — revisar facet 'performance (sem loops O(n^2))' em MainWindow._on_sampling_failed
04414. [x] app\ui\main_window.py:459 — revisar facet 'coberto por testes' em MainWindow._on_sampling_failed
04415. [x] app\ui\main_window.py:463 — definir/revisar FunctionDef: MainWindow._run_preview
04416. [x] app\ui\main_window.py:463 — revisar facet 'assinatura/args consistentes' em MainWindow._run_preview
04417. [x] app\ui\main_window.py:463 — revisar facet 'docstring em português' em MainWindow._run_preview
04418. [x] app\ui\main_window.py:463 — revisar facet 'nomenclatura clara (PEP8)' em MainWindow._run_preview
04419. [x] app\ui\main_window.py:463 — revisar facet 'type hints presentes' em MainWindow._run_preview
04420. [x] app\ui\main_window.py:463 — revisar facet 'tratamento de erros adequado' em MainWindow._run_preview
04421. [x] app\ui\main_window.py:463 — revisar facet 'sem comentários inline desnecessários' em MainWindow._run_preview
04422. [x] app\ui\main_window.py:463 — revisar facet 'não imprime side-effects na UI/IO' em MainWindow._run_preview
04423. [x] app\ui\main_window.py:463 — revisar facet 'thread-safety revisada' em MainWindow._run_preview
04424. [x] app\ui\main_window.py:463 — revisar facet 'performance (sem loops O(n^2))' em MainWindow._run_preview
04425. [x] app\ui\main_window.py:463 — revisar facet 'coberto por testes' em MainWindow._run_preview
04426. [x] app\ui\main_window.py:464 — atribuição: MainWindow._run_preview ← text
04427. [x] app\ui\main_window.py:465 — controle if em MainWindow._run_preview
04428. [x] app\ui\main_window.py:466 — return em MainWindow._run_preview
04429. [x] app\ui\main_window.py:467 — atribuição: MainWindow._run_preview ← specs
04430. [x] app\ui\main_window.py:468 — import: app.services.preview_service
04431. [x] app\ui\main_window.py:470 — atribuição: MainWindow._run_preview ← svc
04432. [x] app\ui\main_window.py:471 — try em MainWindow._run_preview
04433. [x] app\ui\main_window.py:477 — definir/revisar FunctionDef: MainWindow.set_status
04434. [x] app\ui\main_window.py:477 — revisar facet 'assinatura/args consistentes' em MainWindow.set_status
04435. [x] app\ui\main_window.py:477 — revisar facet 'docstring em português' em MainWindow.set_status
04436. [x] app\ui\main_window.py:477 — revisar facet 'nomenclatura clara (PEP8)' em MainWindow.set_status
04437. [x] app\ui\main_window.py:477 — revisar facet 'type hints presentes' em MainWindow.set_status
04438. [x] app\ui\main_window.py:477 — revisar facet 'tratamento de erros adequado' em MainWindow.set_status
04439. [x] app\ui\main_window.py:477 — revisar facet 'sem comentários inline desnecessários' em MainWindow.set_status
04440. [x] app\ui\main_window.py:477 — revisar facet 'não imprime side-effects na UI/IO' em MainWindow.set_status
04441. [x] app\ui\main_window.py:477 — revisar facet 'thread-safety revisada' em MainWindow.set_status
04442. [x] app\ui\main_window.py:477 — revisar facet 'performance (sem loops O(n^2))' em MainWindow.set_status
04443. [x] app\ui\main_window.py:477 — revisar facet 'coberto por testes' em MainWindow.set_status
04444. [x] app\ui\main_window.py:480 — definir/revisar FunctionDef: MainWindow.set_progress
04445. [x] app\ui\main_window.py:480 — revisar facet 'assinatura/args consistentes' em MainWindow.set_progress
04446. [x] app\ui\main_window.py:480 — revisar facet 'docstring em português' em MainWindow.set_progress
04447. [x] app\ui\main_window.py:480 — revisar facet 'nomenclatura clara (PEP8)' em MainWindow.set_progress
04448. [x] app\ui\main_window.py:480 — revisar facet 'type hints presentes' em MainWindow.set_progress
04449. [x] app\ui\main_window.py:480 — revisar facet 'tratamento de erros adequado' em MainWindow.set_progress
04450. [x] app\ui\main_window.py:480 — revisar facet 'sem comentários inline desnecessários' em MainWindow.set_progress
04451. [x] app\ui\main_window.py:480 — revisar facet 'não imprime side-effects na UI/IO' em MainWindow.set_progress
04452. [x] app\ui\main_window.py:480 — revisar facet 'thread-safety revisada' em MainWindow.set_progress
04453. [x] app\ui\main_window.py:480 — revisar facet 'performance (sem loops O(n^2))' em MainWindow.set_progress
04454. [x] app\ui\main_window.py:480 — revisar facet 'coberto por testes' em MainWindow.set_progress
04455. [x] app\ui\main_window.py:485 — definir/revisar FunctionDef: MainWindow.closeEvent
04456. [x] app\ui\main_window.py:485 — revisar facet 'assinatura/args consistentes' em MainWindow.closeEvent
04457. [x] app\ui\main_window.py:485 — revisar facet 'docstring em português' em MainWindow.closeEvent
04458. [x] app\ui\main_window.py:485 — revisar facet 'nomenclatura clara (PEP8)' em MainWindow.closeEvent
04459. [x] app\ui\main_window.py:485 — revisar facet 'type hints presentes' em MainWindow.closeEvent
04460. [x] app\ui\main_window.py:485 — revisar facet 'tratamento de erros adequado' em MainWindow.closeEvent
04461. [x] app\ui\main_window.py:485 — revisar facet 'sem comentários inline desnecessários' em MainWindow.closeEvent
04462. [x] app\ui\main_window.py:485 — revisar facet 'não imprime side-effects na UI/IO' em MainWindow.closeEvent
04463. [x] app\ui\main_window.py:485 — revisar facet 'thread-safety revisada' em MainWindow.closeEvent
04464. [x] app\ui\main_window.py:485 — revisar facet 'performance (sem loops O(n^2))' em MainWindow.closeEvent
04465. [x] app\ui\main_window.py:485 — revisar facet 'coberto por testes' em MainWindow.closeEvent
04466. [x] Existência e estrutura do módulo: app\ui\models\__init__.py
04467. [x] Existência e estrutura do módulo: app\ui\models\experiments_table_model.py
04468. [x] app\ui\models\experiments_table_model.py:3 — import: __future__
04469. [x] app\ui\models\experiments_table_model.py:5 — import: PySide6.QtCore
04470. [x] app\ui\models\experiments_table_model.py:8 — definir/revisar ClassDef: PagedExperimentsModel
04471. [x] app\ui\models\experiments_table_model.py:9 — definir/revisar FunctionDef: PagedExperimentsModel.__init__
04472. [x] app\ui\models\experiments_table_model.py:9 — revisar facet 'assinatura/args consistentes' em PagedExperimentsModel.__init__
04473. [x] app\ui\models\experiments_table_model.py:9 — revisar facet 'docstring em português' em PagedExperimentsModel.__init__
04474. [x] app\ui\models\experiments_table_model.py:9 — revisar facet 'nomenclatura clara (PEP8)' em PagedExperimentsModel.__init__
04475. [x] app\ui\models\experiments_table_model.py:9 — revisar facet 'type hints presentes' em PagedExperimentsModel.__init__
04476. [x] app\ui\models\experiments_table_model.py:9 — revisar facet 'tratamento de erros adequado' em PagedExperimentsModel.__init__
04477. [x] app\ui\models\experiments_table_model.py:9 — revisar facet 'sem comentários inline desnecessários' em PagedExperimentsModel.__init__
04478. [x] app\ui\models\experiments_table_model.py:9 — revisar facet 'não imprime side-effects na UI/IO' em PagedExperimentsModel.__init__
04479. [x] app\ui\models\experiments_table_model.py:9 — revisar facet 'thread-safety revisada' em PagedExperimentsModel.__init__
04480. [x] app\ui\models\experiments_table_model.py:9 — revisar facet 'performance (sem loops O(n^2))' em PagedExperimentsModel.__init__
04481. [x] app\ui\models\experiments_table_model.py:9 — revisar facet 'coberto por testes' em PagedExperimentsModel.__init__
04482. [x] app\ui\models\experiments_table_model.py:13 — atribuição: PagedExperimentsModel.__init__ ← ?
04483. [x] app\ui\models\experiments_table_model.py:14 — atribuição: PagedExperimentsModel.__init__ ← ?
04484. [x] app\ui\models\experiments_table_model.py:16 — definir/revisar FunctionDef: PagedExperimentsModel.set_data
04485. [x] app\ui\models\experiments_table_model.py:16 — revisar facet 'assinatura/args consistentes' em PagedExperimentsModel.set_data
04486. [x] app\ui\models\experiments_table_model.py:16 — revisar facet 'docstring em português' em PagedExperimentsModel.set_data
04487. [x] app\ui\models\experiments_table_model.py:16 — revisar facet 'nomenclatura clara (PEP8)' em PagedExperimentsModel.set_data
04488. [x] app\ui\models\experiments_table_model.py:16 — revisar facet 'type hints presentes' em PagedExperimentsModel.set_data
04489. [x] app\ui\models\experiments_table_model.py:16 — revisar facet 'tratamento de erros adequado' em PagedExperimentsModel.set_data
04490. [x] app\ui\models\experiments_table_model.py:16 — revisar facet 'sem comentários inline desnecessários' em PagedExperimentsModel.set_data
04491. [x] app\ui\models\experiments_table_model.py:16 — revisar facet 'não imprime side-effects na UI/IO' em PagedExperimentsModel.set_data
04492. [x] app\ui\models\experiments_table_model.py:16 — revisar facet 'thread-safety revisada' em PagedExperimentsModel.set_data
04493. [x] app\ui\models\experiments_table_model.py:16 — revisar facet 'performance (sem loops O(n^2))' em PagedExperimentsModel.set_data
04494. [x] app\ui\models\experiments_table_model.py:16 — revisar facet 'coberto por testes' em PagedExperimentsModel.set_data
04495. [x] app\ui\models\experiments_table_model.py:18 — atribuição: PagedExperimentsModel.set_data ← ?
04496. [x] app\ui\models\experiments_table_model.py:19 — atribuição: PagedExperimentsModel.set_data ← ?
04497. [x] app\ui\models\experiments_table_model.py:20 — atribuição: PagedExperimentsModel.set_data ← ?
04498. [x] app\ui\models\experiments_table_model.py:23 — definir/revisar FunctionDef: PagedExperimentsModel.rowCount
04499. [x] app\ui\models\experiments_table_model.py:23 — revisar facet 'assinatura/args consistentes' em PagedExperimentsModel.rowCount
04500. [x] app\ui\models\experiments_table_model.py:23 — revisar facet 'docstring em português' em PagedExperimentsModel.rowCount
04501. [x] app\ui\models\experiments_table_model.py:23 — revisar facet 'nomenclatura clara (PEP8)' em PagedExperimentsModel.rowCount
04502. [x] app\ui\models\experiments_table_model.py:23 — revisar facet 'type hints presentes' em PagedExperimentsModel.rowCount
04503. [x] app\ui\models\experiments_table_model.py:23 — revisar facet 'tratamento de erros adequado' em PagedExperimentsModel.rowCount
04504. [x] app\ui\models\experiments_table_model.py:23 — revisar facet 'sem comentários inline desnecessários' em PagedExperimentsModel.rowCount
04505. [x] app\ui\models\experiments_table_model.py:23 — revisar facet 'não imprime side-effects na UI/IO' em PagedExperimentsModel.rowCount
04506. [x] app\ui\models\experiments_table_model.py:23 — revisar facet 'thread-safety revisada' em PagedExperimentsModel.rowCount
04507. [x] app\ui\models\experiments_table_model.py:23 — revisar facet 'performance (sem loops O(n^2))' em PagedExperimentsModel.rowCount
04508. [x] app\ui\models\experiments_table_model.py:23 — revisar facet 'coberto por testes' em PagedExperimentsModel.rowCount
04509. [x] app\ui\models\experiments_table_model.py:24 — atribuição: PagedExperimentsModel.rowCount ← n
04510. [x] app\ui\models\experiments_table_model.py:25 — return em PagedExperimentsModel.rowCount
04511. [x] app\ui\models\experiments_table_model.py:27 — definir/revisar FunctionDef: PagedExperimentsModel.columnCount
04512. [x] app\ui\models\experiments_table_model.py:27 — revisar facet 'assinatura/args consistentes' em PagedExperimentsModel.columnCount
04513. [x] app\ui\models\experiments_table_model.py:27 — revisar facet 'docstring em português' em PagedExperimentsModel.columnCount
04514. [x] app\ui\models\experiments_table_model.py:27 — revisar facet 'nomenclatura clara (PEP8)' em PagedExperimentsModel.columnCount
04515. [x] app\ui\models\experiments_table_model.py:27 — revisar facet 'type hints presentes' em PagedExperimentsModel.columnCount
04516. [x] app\ui\models\experiments_table_model.py:27 — revisar facet 'tratamento de erros adequado' em PagedExperimentsModel.columnCount
04517. [x] app\ui\models\experiments_table_model.py:27 — revisar facet 'sem comentários inline desnecessários' em PagedExperimentsModel.columnCount
04518. [x] app\ui\models\experiments_table_model.py:27 — revisar facet 'não imprime side-effects na UI/IO' em PagedExperimentsModel.columnCount
04519. [x] app\ui\models\experiments_table_model.py:27 — revisar facet 'thread-safety revisada' em PagedExperimentsModel.columnCount
04520. [x] app\ui\models\experiments_table_model.py:27 — revisar facet 'performance (sem loops O(n^2))' em PagedExperimentsModel.columnCount
04521. [x] app\ui\models\experiments_table_model.py:27 — revisar facet 'coberto por testes' em PagedExperimentsModel.columnCount
04522. [x] app\ui\models\experiments_table_model.py:28 — return em PagedExperimentsModel.columnCount
04523. [x] app\ui\models\experiments_table_model.py:30 — definir/revisar FunctionDef: PagedExperimentsModel.headerData
04524. [x] app\ui\models\experiments_table_model.py:30 — revisar facet 'assinatura/args consistentes' em PagedExperimentsModel.headerData
04525. [x] app\ui\models\experiments_table_model.py:30 — revisar facet 'docstring em português' em PagedExperimentsModel.headerData
04526. [x] app\ui\models\experiments_table_model.py:30 — revisar facet 'nomenclatura clara (PEP8)' em PagedExperimentsModel.headerData
04527. [x] app\ui\models\experiments_table_model.py:30 — revisar facet 'type hints presentes' em PagedExperimentsModel.headerData
04528. [x] app\ui\models\experiments_table_model.py:30 — revisar facet 'tratamento de erros adequado' em PagedExperimentsModel.headerData
04529. [x] app\ui\models\experiments_table_model.py:30 — revisar facet 'sem comentários inline desnecessários' em PagedExperimentsModel.headerData
04530. [x] app\ui\models\experiments_table_model.py:30 — revisar facet 'não imprime side-effects na UI/IO' em PagedExperimentsModel.headerData
04531. [x] app\ui\models\experiments_table_model.py:30 — revisar facet 'thread-safety revisada' em PagedExperimentsModel.headerData
04532. [x] app\ui\models\experiments_table_model.py:30 — revisar facet 'performance (sem loops O(n^2))' em PagedExperimentsModel.headerData
04533. [x] app\ui\models\experiments_table_model.py:30 — revisar facet 'coberto por testes' em PagedExperimentsModel.headerData
04534. [x] app\ui\models\experiments_table_model.py:31 — controle if em PagedExperimentsModel.headerData
04535. [x] app\ui\models\experiments_table_model.py:32 — return em PagedExperimentsModel.headerData
04536. [x] app\ui\models\experiments_table_model.py:33 — controle if em PagedExperimentsModel.headerData
04537. [x] app\ui\models\experiments_table_model.py:34 — return em PagedExperimentsModel.headerData
04538. [x] app\ui\models\experiments_table_model.py:35 — return em PagedExperimentsModel.headerData
04539. [x] app\ui\models\experiments_table_model.py:37 — definir/revisar FunctionDef: PagedExperimentsModel.data
04540. [x] app\ui\models\experiments_table_model.py:37 — revisar facet 'assinatura/args consistentes' em PagedExperimentsModel.data
04541. [x] app\ui\models\experiments_table_model.py:37 — revisar facet 'docstring em português' em PagedExperimentsModel.data
04542. [x] app\ui\models\experiments_table_model.py:37 — revisar facet 'nomenclatura clara (PEP8)' em PagedExperimentsModel.data
04543. [x] app\ui\models\experiments_table_model.py:37 — revisar facet 'type hints presentes' em PagedExperimentsModel.data
04544. [x] app\ui\models\experiments_table_model.py:37 — revisar facet 'tratamento de erros adequado' em PagedExperimentsModel.data
04545. [x] app\ui\models\experiments_table_model.py:37 — revisar facet 'sem comentários inline desnecessários' em PagedExperimentsModel.data
04546. [x] app\ui\models\experiments_table_model.py:37 — revisar facet 'não imprime side-effects na UI/IO' em PagedExperimentsModel.data
04547. [x] app\ui\models\experiments_table_model.py:37 — revisar facet 'thread-safety revisada' em PagedExperimentsModel.data
04548. [x] app\ui\models\experiments_table_model.py:37 — revisar facet 'performance (sem loops O(n^2))' em PagedExperimentsModel.data
04549. [x] app\ui\models\experiments_table_model.py:37 — revisar facet 'coberto por testes' em PagedExperimentsModel.data
04550. [x] app\ui\models\experiments_table_model.py:38 — controle if em PagedExperimentsModel.data
04551. [x] app\ui\models\experiments_table_model.py:39 — return em PagedExperimentsModel.data
04552. [x] app\ui\models\experiments_table_model.py:40 — atribuição: PagedExperimentsModel.data ← row
04553. [x] app\ui\models\experiments_table_model.py:41 — atribuição: PagedExperimentsModel.data ← col
04554. [x] app\ui\models\experiments_table_model.py:42 — controle if em PagedExperimentsModel.data
04555. [x] app\ui\models\experiments_table_model.py:43 — return em PagedExperimentsModel.data
04556. [x] app\ui\models\experiments_table_model.py:44 — try em PagedExperimentsModel.data
04557. [x] app\ui\models\experiments_table_model.py:45 — return em PagedExperimentsModel.data
04558. [x] app\ui\models\experiments_table_model.py:47 — return em PagedExperimentsModel.data
04559. [x] app\ui\models\experiments_table_model.py:49 — definir/revisar FunctionDef: PagedExperimentsModel.next_page
04560. [x] app\ui\models\experiments_table_model.py:49 — revisar facet 'assinatura/args consistentes' em PagedExperimentsModel.next_page
04561. [x] app\ui\models\experiments_table_model.py:49 — revisar facet 'docstring em português' em PagedExperimentsModel.next_page
04562. [x] app\ui\models\experiments_table_model.py:49 — revisar facet 'nomenclatura clara (PEP8)' em PagedExperimentsModel.next_page
04563. [x] app\ui\models\experiments_table_model.py:49 — revisar facet 'type hints presentes' em PagedExperimentsModel.next_page
04564. [x] app\ui\models\experiments_table_model.py:49 — revisar facet 'tratamento de erros adequado' em PagedExperimentsModel.next_page
04565. [x] app\ui\models\experiments_table_model.py:49 — revisar facet 'sem comentários inline desnecessários' em PagedExperimentsModel.next_page
04566. [x] app\ui\models\experiments_table_model.py:49 — revisar facet 'não imprime side-effects na UI/IO' em PagedExperimentsModel.next_page
04567. [x] app\ui\models\experiments_table_model.py:49 — revisar facet 'thread-safety revisada' em PagedExperimentsModel.next_page
04568. [x] app\ui\models\experiments_table_model.py:49 — revisar facet 'performance (sem loops O(n^2))' em PagedExperimentsModel.next_page
04569. [x] app\ui\models\experiments_table_model.py:49 — revisar facet 'coberto por testes' em PagedExperimentsModel.next_page
04570. [x] app\ui\models\experiments_table_model.py:50 — controle if em PagedExperimentsModel.next_page
04571. [x] app\ui\models\experiments_table_model.py:55 — definir/revisar FunctionDef: PagedExperimentsModel.prev_page
04572. [x] app\ui\models\experiments_table_model.py:55 — revisar facet 'assinatura/args consistentes' em PagedExperimentsModel.prev_page
04573. [x] app\ui\models\experiments_table_model.py:55 — revisar facet 'docstring em português' em PagedExperimentsModel.prev_page
04574. [x] app\ui\models\experiments_table_model.py:55 — revisar facet 'nomenclatura clara (PEP8)' em PagedExperimentsModel.prev_page
04575. [x] app\ui\models\experiments_table_model.py:55 — revisar facet 'type hints presentes' em PagedExperimentsModel.prev_page
04576. [x] app\ui\models\experiments_table_model.py:55 — revisar facet 'tratamento de erros adequado' em PagedExperimentsModel.prev_page
04577. [x] app\ui\models\experiments_table_model.py:55 — revisar facet 'sem comentários inline desnecessários' em PagedExperimentsModel.prev_page
04578. [x] app\ui\models\experiments_table_model.py:55 — revisar facet 'não imprime side-effects na UI/IO' em PagedExperimentsModel.prev_page
04579. [x] app\ui\models\experiments_table_model.py:55 — revisar facet 'thread-safety revisada' em PagedExperimentsModel.prev_page
04580. [x] app\ui\models\experiments_table_model.py:55 — revisar facet 'performance (sem loops O(n^2))' em PagedExperimentsModel.prev_page
04581. [x] app\ui\models\experiments_table_model.py:55 — revisar facet 'coberto por testes' em PagedExperimentsModel.prev_page
04582. [x] app\ui\models\experiments_table_model.py:56 — controle if em PagedExperimentsModel.prev_page
04583. [x] app\ui\models\experiments_table_model.py:62 — definir/revisar FunctionDef: PagedExperimentsModel.current_page
04584. [x] app\ui\models\experiments_table_model.py:62 — revisar facet 'assinatura/args consistentes' em PagedExperimentsModel.current_page
04585. [x] app\ui\models\experiments_table_model.py:62 — revisar facet 'docstring em português' em PagedExperimentsModel.current_page
04586. [x] app\ui\models\experiments_table_model.py:62 — revisar facet 'nomenclatura clara (PEP8)' em PagedExperimentsModel.current_page
04587. [x] app\ui\models\experiments_table_model.py:62 — revisar facet 'type hints presentes' em PagedExperimentsModel.current_page
04588. [x] app\ui\models\experiments_table_model.py:62 — revisar facet 'tratamento de erros adequado' em PagedExperimentsModel.current_page
04589. [x] app\ui\models\experiments_table_model.py:62 — revisar facet 'sem comentários inline desnecessários' em PagedExperimentsModel.current_page
04590. [x] app\ui\models\experiments_table_model.py:62 — revisar facet 'não imprime side-effects na UI/IO' em PagedExperimentsModel.current_page
04591. [x] app\ui\models\experiments_table_model.py:62 — revisar facet 'thread-safety revisada' em PagedExperimentsModel.current_page
04592. [x] app\ui\models\experiments_table_model.py:62 — revisar facet 'performance (sem loops O(n^2))' em PagedExperimentsModel.current_page
04593. [x] app\ui\models\experiments_table_model.py:62 — revisar facet 'coberto por testes' em PagedExperimentsModel.current_page
04594. [x] app\ui\models\experiments_table_model.py:63 — return em PagedExperimentsModel.current_page
04595. [x] app\ui\models\experiments_table_model.py:66 — definir/revisar FunctionDef: PagedExperimentsModel.total_pages
04596. [x] app\ui\models\experiments_table_model.py:66 — revisar facet 'assinatura/args consistentes' em PagedExperimentsModel.total_pages
04597. [x] app\ui\models\experiments_table_model.py:66 — revisar facet 'docstring em português' em PagedExperimentsModel.total_pages
04598. [x] app\ui\models\experiments_table_model.py:66 — revisar facet 'nomenclatura clara (PEP8)' em PagedExperimentsModel.total_pages
04599. [x] app\ui\models\experiments_table_model.py:66 — revisar facet 'type hints presentes' em PagedExperimentsModel.total_pages
04600. [x] app\ui\models\experiments_table_model.py:66 — revisar facet 'tratamento de erros adequado' em PagedExperimentsModel.total_pages
04601. [x] app\ui\models\experiments_table_model.py:66 — revisar facet 'sem comentários inline desnecessários' em PagedExperimentsModel.total_pages
04602. [x] app\ui\models\experiments_table_model.py:66 — revisar facet 'não imprime side-effects na UI/IO' em PagedExperimentsModel.total_pages
04603. [x] app\ui\models\experiments_table_model.py:66 — revisar facet 'thread-safety revisada' em PagedExperimentsModel.total_pages
04604. [x] app\ui\models\experiments_table_model.py:66 — revisar facet 'performance (sem loops O(n^2))' em PagedExperimentsModel.total_pages
04605. [x] app\ui\models\experiments_table_model.py:66 — revisar facet 'coberto por testes' em PagedExperimentsModel.total_pages
04606. [x] app\ui\models\experiments_table_model.py:67 — controle if em PagedExperimentsModel.total_pages
04607. [x] app\ui\models\experiments_table_model.py:68 — return em PagedExperimentsModel.total_pages
04608. [x] app\ui\models\experiments_table_model.py:69 — return em PagedExperimentsModel.total_pages
04609. [x] Existência e estrutura do módulo: app\ui\models\repository_paged_model.py
04610. [x] app\ui\models\repository_paged_model.py:3 — import: __future__
04611. [x] app\ui\models\repository_paged_model.py:5 — import: PySide6.QtCore
04612. [x] app\ui\models\repository_paged_model.py:7 — import: app.infrastructure.experiment_repository
04613. [x] app\ui\models\repository_paged_model.py:10 — definir/revisar ClassDef: RepositoryPagedModel
04614. [x] app\ui\models\repository_paged_model.py:11 — definir/revisar FunctionDef: RepositoryPagedModel.__init__
04615. [x] app\ui\models\repository_paged_model.py:11 — revisar facet 'assinatura/args consistentes' em RepositoryPagedModel.__init__
04616. [x] app\ui\models\repository_paged_model.py:11 — revisar facet 'docstring em português' em RepositoryPagedModel.__init__
04617. [x] app\ui\models\repository_paged_model.py:11 — revisar facet 'nomenclatura clara (PEP8)' em RepositoryPagedModel.__init__
04618. [x] app\ui\models\repository_paged_model.py:11 — revisar facet 'type hints presentes' em RepositoryPagedModel.__init__
04619. [x] app\ui\models\repository_paged_model.py:11 — revisar facet 'tratamento de erros adequado' em RepositoryPagedModel.__init__
04620. [x] app\ui\models\repository_paged_model.py:11 — revisar facet 'sem comentários inline desnecessários' em RepositoryPagedModel.__init__
04621. [x] app\ui\models\repository_paged_model.py:11 — revisar facet 'não imprime side-effects na UI/IO' em RepositoryPagedModel.__init__
04622. [x] app\ui\models\repository_paged_model.py:11 — revisar facet 'thread-safety revisada' em RepositoryPagedModel.__init__
04623. [x] app\ui\models\repository_paged_model.py:11 — revisar facet 'performance (sem loops O(n^2))' em RepositoryPagedModel.__init__
04624. [x] app\ui\models\repository_paged_model.py:11 — revisar facet 'coberto por testes' em RepositoryPagedModel.__init__
04625. [x] app\ui\models\repository_paged_model.py:18 — atribuição: RepositoryPagedModel.__init__ ← ?
04626. [x] app\ui\models\repository_paged_model.py:19 — atribuição: RepositoryPagedModel.__init__ ← ?
04627. [x] app\ui\models\repository_paged_model.py:20 — atribuição: RepositoryPagedModel.__init__ ← ?
04628. [x] app\ui\models\repository_paged_model.py:23 — atribuição: RepositoryPagedModel.__init__ ← ?
04629. [x] app\ui\models\repository_paged_model.py:26 — definir/revisar FunctionDef: RepositoryPagedModel._reload
04630. [x] app\ui\models\repository_paged_model.py:26 — revisar facet 'assinatura/args consistentes' em RepositoryPagedModel._reload
04631. [x] app\ui\models\repository_paged_model.py:26 — revisar facet 'docstring em português' em RepositoryPagedModel._reload
04632. [x] app\ui\models\repository_paged_model.py:26 — revisar facet 'nomenclatura clara (PEP8)' em RepositoryPagedModel._reload
04633. [x] app\ui\models\repository_paged_model.py:26 — revisar facet 'type hints presentes' em RepositoryPagedModel._reload
04634. [x] app\ui\models\repository_paged_model.py:26 — revisar facet 'tratamento de erros adequado' em RepositoryPagedModel._reload
04635. [x] app\ui\models\repository_paged_model.py:26 — revisar facet 'sem comentários inline desnecessários' em RepositoryPagedModel._reload
04636. [x] app\ui\models\repository_paged_model.py:26 — revisar facet 'não imprime side-effects na UI/IO' em RepositoryPagedModel._reload
04637. [x] app\ui\models\repository_paged_model.py:26 — revisar facet 'thread-safety revisada' em RepositoryPagedModel._reload
04638. [x] app\ui\models\repository_paged_model.py:26 — revisar facet 'performance (sem loops O(n^2))' em RepositoryPagedModel._reload
04639. [x] app\ui\models\repository_paged_model.py:26 — revisar facet 'coberto por testes' em RepositoryPagedModel._reload
04640. [x] app\ui\models\repository_paged_model.py:28 — atribuição: RepositoryPagedModel._reload ← ?
04641. [x] app\ui\models\repository_paged_model.py:29 — atribuição: RepositoryPagedModel._reload ← ?
04642. [x] app\ui\models\repository_paged_model.py:30 — atribuição: RepositoryPagedModel._reload ← ?
04643. [x] app\ui\models\repository_paged_model.py:33 — definir/revisar FunctionDef: RepositoryPagedModel.rowCount
04644. [x] app\ui\models\repository_paged_model.py:33 — revisar facet 'assinatura/args consistentes' em RepositoryPagedModel.rowCount
04645. [x] app\ui\models\repository_paged_model.py:33 — revisar facet 'docstring em português' em RepositoryPagedModel.rowCount
04646. [x] app\ui\models\repository_paged_model.py:33 — revisar facet 'nomenclatura clara (PEP8)' em RepositoryPagedModel.rowCount
04647. [x] app\ui\models\repository_paged_model.py:33 — revisar facet 'type hints presentes' em RepositoryPagedModel.rowCount
04648. [x] app\ui\models\repository_paged_model.py:33 — revisar facet 'tratamento de erros adequado' em RepositoryPagedModel.rowCount
04649. [x] app\ui\models\repository_paged_model.py:33 — revisar facet 'sem comentários inline desnecessários' em RepositoryPagedModel.rowCount
04650. [x] app\ui\models\repository_paged_model.py:33 — revisar facet 'não imprime side-effects na UI/IO' em RepositoryPagedModel.rowCount
04651. [x] app\ui\models\repository_paged_model.py:33 — revisar facet 'thread-safety revisada' em RepositoryPagedModel.rowCount
04652. [x] app\ui\models\repository_paged_model.py:33 — revisar facet 'performance (sem loops O(n^2))' em RepositoryPagedModel.rowCount
04653. [x] app\ui\models\repository_paged_model.py:33 — revisar facet 'coberto por testes' em RepositoryPagedModel.rowCount
04654. [x] app\ui\models\repository_paged_model.py:34 — return em RepositoryPagedModel.rowCount
04655. [x] app\ui\models\repository_paged_model.py:36 — definir/revisar FunctionDef: RepositoryPagedModel.columnCount
04656. [x] app\ui\models\repository_paged_model.py:36 — revisar facet 'assinatura/args consistentes' em RepositoryPagedModel.columnCount
04657. [x] app\ui\models\repository_paged_model.py:36 — revisar facet 'docstring em português' em RepositoryPagedModel.columnCount
04658. [x] app\ui\models\repository_paged_model.py:36 — revisar facet 'nomenclatura clara (PEP8)' em RepositoryPagedModel.columnCount
04659. [x] app\ui\models\repository_paged_model.py:36 — revisar facet 'type hints presentes' em RepositoryPagedModel.columnCount
04660. [x] app\ui\models\repository_paged_model.py:36 — revisar facet 'tratamento de erros adequado' em RepositoryPagedModel.columnCount
04661. [x] app\ui\models\repository_paged_model.py:36 — revisar facet 'sem comentários inline desnecessários' em RepositoryPagedModel.columnCount
04662. [x] app\ui\models\repository_paged_model.py:36 — revisar facet 'não imprime side-effects na UI/IO' em RepositoryPagedModel.columnCount
04663. [x] app\ui\models\repository_paged_model.py:36 — revisar facet 'thread-safety revisada' em RepositoryPagedModel.columnCount
04664. [x] app\ui\models\repository_paged_model.py:36 — revisar facet 'performance (sem loops O(n^2))' em RepositoryPagedModel.columnCount
04665. [x] app\ui\models\repository_paged_model.py:36 — revisar facet 'coberto por testes' em RepositoryPagedModel.columnCount
04666. [x] app\ui\models\repository_paged_model.py:37 — return em RepositoryPagedModel.columnCount
04667. [x] app\ui\models\repository_paged_model.py:39 — definir/revisar FunctionDef: RepositoryPagedModel.headerData
04668. [x] app\ui\models\repository_paged_model.py:39 — revisar facet 'assinatura/args consistentes' em RepositoryPagedModel.headerData
04669. [x] app\ui\models\repository_paged_model.py:39 — revisar facet 'docstring em português' em RepositoryPagedModel.headerData
04670. [x] app\ui\models\repository_paged_model.py:39 — revisar facet 'nomenclatura clara (PEP8)' em RepositoryPagedModel.headerData
04671. [x] app\ui\models\repository_paged_model.py:39 — revisar facet 'type hints presentes' em RepositoryPagedModel.headerData
04672. [x] app\ui\models\repository_paged_model.py:39 — revisar facet 'tratamento de erros adequado' em RepositoryPagedModel.headerData
04673. [x] app\ui\models\repository_paged_model.py:39 — revisar facet 'sem comentários inline desnecessários' em RepositoryPagedModel.headerData
04674. [x] app\ui\models\repository_paged_model.py:39 — revisar facet 'não imprime side-effects na UI/IO' em RepositoryPagedModel.headerData
04675. [x] app\ui\models\repository_paged_model.py:39 — revisar facet 'thread-safety revisada' em RepositoryPagedModel.headerData
04676. [x] app\ui\models\repository_paged_model.py:39 — revisar facet 'performance (sem loops O(n^2))' em RepositoryPagedModel.headerData
04677. [x] app\ui\models\repository_paged_model.py:39 — revisar facet 'coberto por testes' em RepositoryPagedModel.headerData
04678. [x] app\ui\models\repository_paged_model.py:40 — controle if em RepositoryPagedModel.headerData
04679. [x] app\ui\models\repository_paged_model.py:41 — return em RepositoryPagedModel.headerData
04680. [x] app\ui\models\repository_paged_model.py:42 — controle if em RepositoryPagedModel.headerData
04681. [x] app\ui\models\repository_paged_model.py:43 — return em RepositoryPagedModel.headerData
04682. [x] app\ui\models\repository_paged_model.py:44 — return em RepositoryPagedModel.headerData
04683. [x] app\ui\models\repository_paged_model.py:46 — definir/revisar FunctionDef: RepositoryPagedModel.data
04684. [x] app\ui\models\repository_paged_model.py:46 — revisar facet 'assinatura/args consistentes' em RepositoryPagedModel.data
04685. [x] app\ui\models\repository_paged_model.py:46 — revisar facet 'docstring em português' em RepositoryPagedModel.data
04686. [x] app\ui\models\repository_paged_model.py:46 — revisar facet 'nomenclatura clara (PEP8)' em RepositoryPagedModel.data
04687. [x] app\ui\models\repository_paged_model.py:46 — revisar facet 'type hints presentes' em RepositoryPagedModel.data
04688. [x] app\ui\models\repository_paged_model.py:46 — revisar facet 'tratamento de erros adequado' em RepositoryPagedModel.data
04689. [x] app\ui\models\repository_paged_model.py:46 — revisar facet 'sem comentários inline desnecessários' em RepositoryPagedModel.data
04690. [x] app\ui\models\repository_paged_model.py:46 — revisar facet 'não imprime side-effects na UI/IO' em RepositoryPagedModel.data
04691. [x] app\ui\models\repository_paged_model.py:46 — revisar facet 'thread-safety revisada' em RepositoryPagedModel.data
04692. [x] app\ui\models\repository_paged_model.py:46 — revisar facet 'performance (sem loops O(n^2))' em RepositoryPagedModel.data
04693. [x] app\ui\models\repository_paged_model.py:46 — revisar facet 'coberto por testes' em RepositoryPagedModel.data
04694. [x] app\ui\models\repository_paged_model.py:47 — controle if em RepositoryPagedModel.data
04695. [x] app\ui\models\repository_paged_model.py:48 — return em RepositoryPagedModel.data
04696. [x] app\ui\models\repository_paged_model.py:49 — atribuição: RepositoryPagedModel.data ← row
04697. [x] app\ui\models\repository_paged_model.py:50 — atribuição: RepositoryPagedModel.data ← col
04698. [x] app\ui\models\repository_paged_model.py:51 — controle if em RepositoryPagedModel.data
04699. [x] app\ui\models\repository_paged_model.py:52 — return em RepositoryPagedModel.data
04700. [x] app\ui\models\repository_paged_model.py:53 — atribuição: RepositoryPagedModel.data ← var_id
04701. [x] app\ui\models\repository_paged_model.py:54 — atribuição: RepositoryPagedModel.data ← value
04702. [x] app\ui\models\repository_paged_model.py:55 — return em RepositoryPagedModel.data
04703. [x] app\ui\models\repository_paged_model.py:57 — definir/revisar FunctionDef: RepositoryPagedModel.next_page
04704. [x] app\ui\models\repository_paged_model.py:57 — revisar facet 'assinatura/args consistentes' em RepositoryPagedModel.next_page
04705. [x] app\ui\models\repository_paged_model.py:57 — revisar facet 'docstring em português' em RepositoryPagedModel.next_page
04706. [x] app\ui\models\repository_paged_model.py:57 — revisar facet 'nomenclatura clara (PEP8)' em RepositoryPagedModel.next_page
04707. [x] app\ui\models\repository_paged_model.py:57 — revisar facet 'type hints presentes' em RepositoryPagedModel.next_page
04708. [x] app\ui\models\repository_paged_model.py:57 — revisar facet 'tratamento de erros adequado' em RepositoryPagedModel.next_page
04709. [x] app\ui\models\repository_paged_model.py:57 — revisar facet 'sem comentários inline desnecessários' em RepositoryPagedModel.next_page
04710. [x] app\ui\models\repository_paged_model.py:57 — revisar facet 'não imprime side-effects na UI/IO' em RepositoryPagedModel.next_page
04711. [x] app\ui\models\repository_paged_model.py:57 — revisar facet 'thread-safety revisada' em RepositoryPagedModel.next_page
04712. [x] app\ui\models\repository_paged_model.py:57 — revisar facet 'performance (sem loops O(n^2))' em RepositoryPagedModel.next_page
04713. [x] app\ui\models\repository_paged_model.py:57 — revisar facet 'coberto por testes' em RepositoryPagedModel.next_page
04714. [x] app\ui\models\repository_paged_model.py:58 — controle if em RepositoryPagedModel.next_page
04715. [x] app\ui\models\repository_paged_model.py:62 — definir/revisar FunctionDef: RepositoryPagedModel.prev_page
04716. [x] app\ui\models\repository_paged_model.py:62 — revisar facet 'assinatura/args consistentes' em RepositoryPagedModel.prev_page
04717. [x] app\ui\models\repository_paged_model.py:62 — revisar facet 'docstring em português' em RepositoryPagedModel.prev_page
04718. [x] app\ui\models\repository_paged_model.py:62 — revisar facet 'nomenclatura clara (PEP8)' em RepositoryPagedModel.prev_page
04719. [x] app\ui\models\repository_paged_model.py:62 — revisar facet 'type hints presentes' em RepositoryPagedModel.prev_page
04720. [x] app\ui\models\repository_paged_model.py:62 — revisar facet 'tratamento de erros adequado' em RepositoryPagedModel.prev_page
04721. [x] app\ui\models\repository_paged_model.py:62 — revisar facet 'sem comentários inline desnecessários' em RepositoryPagedModel.prev_page
04722. [x] app\ui\models\repository_paged_model.py:62 — revisar facet 'não imprime side-effects na UI/IO' em RepositoryPagedModel.prev_page
04723. [x] app\ui\models\repository_paged_model.py:62 — revisar facet 'thread-safety revisada' em RepositoryPagedModel.prev_page
04724. [x] app\ui\models\repository_paged_model.py:62 — revisar facet 'performance (sem loops O(n^2))' em RepositoryPagedModel.prev_page
04725. [x] app\ui\models\repository_paged_model.py:62 — revisar facet 'coberto por testes' em RepositoryPagedModel.prev_page
04726. [x] app\ui\models\repository_paged_model.py:63 — controle if em RepositoryPagedModel.prev_page
04727. [x] app\ui\models\repository_paged_model.py:67 — definir/revisar FunctionDef: RepositoryPagedModel.refresh
04728. [x] app\ui\models\repository_paged_model.py:67 — revisar facet 'assinatura/args consistentes' em RepositoryPagedModel.refresh
04729. [x] app\ui\models\repository_paged_model.py:67 — revisar facet 'docstring em português' em RepositoryPagedModel.refresh
04730. [x] app\ui\models\repository_paged_model.py:67 — revisar facet 'nomenclatura clara (PEP8)' em RepositoryPagedModel.refresh
04731. [x] app\ui\models\repository_paged_model.py:67 — revisar facet 'type hints presentes' em RepositoryPagedModel.refresh
04732. [x] app\ui\models\repository_paged_model.py:67 — revisar facet 'tratamento de erros adequado' em RepositoryPagedModel.refresh
04733. [x] app\ui\models\repository_paged_model.py:67 — revisar facet 'sem comentários inline desnecessários' em RepositoryPagedModel.refresh
04734. [x] app\ui\models\repository_paged_model.py:67 — revisar facet 'não imprime side-effects na UI/IO' em RepositoryPagedModel.refresh
04735. [x] app\ui\models\repository_paged_model.py:67 — revisar facet 'thread-safety revisada' em RepositoryPagedModel.refresh
04736. [x] app\ui\models\repository_paged_model.py:67 — revisar facet 'performance (sem loops O(n^2))' em RepositoryPagedModel.refresh
04737. [x] app\ui\models\repository_paged_model.py:67 — revisar facet 'coberto por testes' em RepositoryPagedModel.refresh
04738. [x] app\ui\models\repository_paged_model.py:71 — definir/revisar FunctionDef: RepositoryPagedModel.current_page
04739. [x] app\ui\models\repository_paged_model.py:71 — revisar facet 'assinatura/args consistentes' em RepositoryPagedModel.current_page
04740. [x] app\ui\models\repository_paged_model.py:71 — revisar facet 'docstring em português' em RepositoryPagedModel.current_page
04741. [x] app\ui\models\repository_paged_model.py:71 — revisar facet 'nomenclatura clara (PEP8)' em RepositoryPagedModel.current_page
04742. [x] app\ui\models\repository_paged_model.py:71 — revisar facet 'type hints presentes' em RepositoryPagedModel.current_page
04743. [x] app\ui\models\repository_paged_model.py:71 — revisar facet 'tratamento de erros adequado' em RepositoryPagedModel.current_page
04744. [x] app\ui\models\repository_paged_model.py:71 — revisar facet 'sem comentários inline desnecessários' em RepositoryPagedModel.current_page
04745. [x] app\ui\models\repository_paged_model.py:71 — revisar facet 'não imprime side-effects na UI/IO' em RepositoryPagedModel.current_page
04746. [x] app\ui\models\repository_paged_model.py:71 — revisar facet 'thread-safety revisada' em RepositoryPagedModel.current_page
04747. [x] app\ui\models\repository_paged_model.py:71 — revisar facet 'performance (sem loops O(n^2))' em RepositoryPagedModel.current_page
04748. [x] app\ui\models\repository_paged_model.py:71 — revisar facet 'coberto por testes' em RepositoryPagedModel.current_page
04749. [x] app\ui\models\repository_paged_model.py:72 — return em RepositoryPagedModel.current_page
04750. [x] app\ui\models\repository_paged_model.py:75 — definir/revisar FunctionDef: RepositoryPagedModel.total_pages
04751. [x] app\ui\models\repository_paged_model.py:75 — revisar facet 'assinatura/args consistentes' em RepositoryPagedModel.total_pages
04752. [x] app\ui\models\repository_paged_model.py:75 — revisar facet 'docstring em português' em RepositoryPagedModel.total_pages
04753. [x] app\ui\models\repository_paged_model.py:75 — revisar facet 'nomenclatura clara (PEP8)' em RepositoryPagedModel.total_pages
04754. [x] app\ui\models\repository_paged_model.py:75 — revisar facet 'type hints presentes' em RepositoryPagedModel.total_pages
04755. [x] app\ui\models\repository_paged_model.py:75 — revisar facet 'tratamento de erros adequado' em RepositoryPagedModel.total_pages
04756. [x] app\ui\models\repository_paged_model.py:75 — revisar facet 'sem comentários inline desnecessários' em RepositoryPagedModel.total_pages
04757. [x] app\ui\models\repository_paged_model.py:75 — revisar facet 'não imprime side-effects na UI/IO' em RepositoryPagedModel.total_pages
04758. [x] app\ui\models\repository_paged_model.py:75 — revisar facet 'thread-safety revisada' em RepositoryPagedModel.total_pages
04759. [x] app\ui\models\repository_paged_model.py:75 — revisar facet 'performance (sem loops O(n^2))' em RepositoryPagedModel.total_pages
04760. [x] app\ui\models\repository_paged_model.py:75 — revisar facet 'coberto por testes' em RepositoryPagedModel.total_pages
04761. [x] app\ui\models\repository_paged_model.py:76 — controle if em RepositoryPagedModel.total_pages
04762. [x] app\ui\models\repository_paged_model.py:77 — return em RepositoryPagedModel.total_pages
04763. [x] app\ui\models\repository_paged_model.py:78 — return em RepositoryPagedModel.total_pages
04764. [x] app\ui\models\repository_paged_model.py:81 — definir/revisar FunctionDef: RepositoryPagedModel.total_rows
04765. [x] app\ui\models\repository_paged_model.py:81 — revisar facet 'assinatura/args consistentes' em RepositoryPagedModel.total_rows
04766. [x] app\ui\models\repository_paged_model.py:81 — revisar facet 'docstring em português' em RepositoryPagedModel.total_rows
04767. [x] app\ui\models\repository_paged_model.py:81 — revisar facet 'nomenclatura clara (PEP8)' em RepositoryPagedModel.total_rows
04768. [x] app\ui\models\repository_paged_model.py:81 — revisar facet 'type hints presentes' em RepositoryPagedModel.total_rows
04769. [x] app\ui\models\repository_paged_model.py:81 — revisar facet 'tratamento de erros adequado' em RepositoryPagedModel.total_rows
04770. [x] app\ui\models\repository_paged_model.py:81 — revisar facet 'sem comentários inline desnecessários' em RepositoryPagedModel.total_rows
04771. [x] app\ui\models\repository_paged_model.py:81 — revisar facet 'não imprime side-effects na UI/IO' em RepositoryPagedModel.total_rows
04772. [x] app\ui\models\repository_paged_model.py:81 — revisar facet 'thread-safety revisada' em RepositoryPagedModel.total_rows
04773. [x] app\ui\models\repository_paged_model.py:81 — revisar facet 'performance (sem loops O(n^2))' em RepositoryPagedModel.total_rows
04774. [x] app\ui\models\repository_paged_model.py:81 — revisar facet 'coberto por testes' em RepositoryPagedModel.total_rows
04775. [x] app\ui\models\repository_paged_model.py:82 — return em RepositoryPagedModel.total_rows
04776. [x] Existência e estrutura do módulo: app\ui\widgets\__init__.py
04777. [x] Existência e estrutura do módulo: app\ui\widgets\batch_comparison_dialog.py
04778. [x] app\ui\widgets\batch_comparison_dialog.py:3 — import: __future__
04779. [x] app\ui\widgets\batch_comparison_dialog.py:5 — import: PySide6.QtWidgets
04780. [x] app\ui\widgets\batch_comparison_dialog.py:13 — import: app.domain.batch_comparison
04781. [x] app\ui\widgets\batch_comparison_dialog.py:16 — definir/revisar ClassDef: BatchComparisonDialog
04782. [x] app\ui\widgets\batch_comparison_dialog.py:17 — definir/revisar FunctionDef: BatchComparisonDialog.__init__
04783. [x] app\ui\widgets\batch_comparison_dialog.py:17 — revisar facet 'assinatura/args consistentes' em BatchComparisonDialog.__init__
04784. [x] app\ui\widgets\batch_comparison_dialog.py:17 — revisar facet 'docstring em português' em BatchComparisonDialog.__init__
04785. [x] app\ui\widgets\batch_comparison_dialog.py:17 — revisar facet 'nomenclatura clara (PEP8)' em BatchComparisonDialog.__init__
04786. [x] app\ui\widgets\batch_comparison_dialog.py:17 — revisar facet 'type hints presentes' em BatchComparisonDialog.__init__
04787. [x] app\ui\widgets\batch_comparison_dialog.py:17 — revisar facet 'tratamento de erros adequado' em BatchComparisonDialog.__init__
04788. [x] app\ui\widgets\batch_comparison_dialog.py:17 — revisar facet 'sem comentários inline desnecessários' em BatchComparisonDialog.__init__
04789. [x] app\ui\widgets\batch_comparison_dialog.py:17 — revisar facet 'não imprime side-effects na UI/IO' em BatchComparisonDialog.__init__
04790. [x] app\ui\widgets\batch_comparison_dialog.py:17 — revisar facet 'thread-safety revisada' em BatchComparisonDialog.__init__
04791. [x] app\ui\widgets\batch_comparison_dialog.py:17 — revisar facet 'performance (sem loops O(n^2))' em BatchComparisonDialog.__init__
04792. [x] app\ui\widgets\batch_comparison_dialog.py:17 — revisar facet 'coberto por testes' em BatchComparisonDialog.__init__
04793. [x] app\ui\widgets\batch_comparison_dialog.py:22 — atribuição: BatchComparisonDialog.__init__ ← layout
04794. [x] app\ui\widgets\batch_comparison_dialog.py:24 — atribuição: BatchComparisonDialog.__init__ ← ?
04795. [x] app\ui\widgets\batch_comparison_dialog.py:25 — atribuição: BatchComparisonDialog.__init__ ← headers
04796. [x] app\ui\widgets\batch_comparison_dialog.py:32 — controle for em BatchComparisonDialog.__init__
04797. [x] app\ui\widgets\batch_comparison_dialog.py:33 — atribuição: BatchComparisonDialog.__init__ ← cells
04798. [x] app\ui\widgets\batch_comparison_dialog.py:42 — controle for em BatchComparisonDialog.__init__
04799. [x] app\ui\widgets\batch_comparison_dialog.py:46 — atribuição: BatchComparisonDialog.__init__ ← header
04800. [x] Existência e estrutura do módulo: app\ui\widgets\batch_export_dialog.py
04801. [x] app\ui\widgets\batch_export_dialog.py:3 — import: __future__
04802. [x] app\ui\widgets\batch_export_dialog.py:5 — import: pathlib
04803. [x] app\ui\widgets\batch_export_dialog.py:6 — import: typing
04804. [x] app\ui\widgets\batch_export_dialog.py:8 — import: PySide6.QtCore
04805. [x] app\ui\widgets\batch_export_dialog.py:9 — import: PySide6.QtWidgets
04806. [x] app\ui\widgets\batch_export_dialog.py:20 — import: app.services.batch_export_service
04807. [x] app\ui\widgets\batch_export_dialog.py:23 — definir/revisar ClassDef: BatchExportDialog
04808. [x] app\ui\widgets\batch_export_dialog.py:24 — atribuição: BatchExportDialog ← exportRequested
04809. [x] app\ui\widgets\batch_export_dialog.py:26 — definir/revisar FunctionDef: BatchExportDialog.__init__
04810. [x] app\ui\widgets\batch_export_dialog.py:26 — revisar facet 'assinatura/args consistentes' em BatchExportDialog.__init__
04811. [x] app\ui\widgets\batch_export_dialog.py:26 — revisar facet 'docstring em português' em BatchExportDialog.__init__
04812. [x] app\ui\widgets\batch_export_dialog.py:26 — revisar facet 'nomenclatura clara (PEP8)' em BatchExportDialog.__init__
04813. [x] app\ui\widgets\batch_export_dialog.py:26 — revisar facet 'type hints presentes' em BatchExportDialog.__init__
04814. [x] app\ui\widgets\batch_export_dialog.py:26 — revisar facet 'tratamento de erros adequado' em BatchExportDialog.__init__
04815. [x] app\ui\widgets\batch_export_dialog.py:26 — revisar facet 'sem comentários inline desnecessários' em BatchExportDialog.__init__
04816. [x] app\ui\widgets\batch_export_dialog.py:26 — revisar facet 'não imprime side-effects na UI/IO' em BatchExportDialog.__init__
04817. [x] app\ui\widgets\batch_export_dialog.py:26 — revisar facet 'thread-safety revisada' em BatchExportDialog.__init__
04818. [x] app\ui\widgets\batch_export_dialog.py:26 — revisar facet 'performance (sem loops O(n^2))' em BatchExportDialog.__init__
04819. [x] app\ui\widgets\batch_export_dialog.py:26 — revisar facet 'coberto por testes' em BatchExportDialog.__init__
04820. [x] app\ui\widgets\batch_export_dialog.py:35 — atribuição: BatchExportDialog.__init__ ← layout
04821. [x] app\ui\widgets\batch_export_dialog.py:37 — atribuição: BatchExportDialog.__init__ ← row1
04822. [x] app\ui\widgets\batch_export_dialog.py:39 — atribuição: BatchExportDialog.__init__ ← ?
04823. [x] app\ui\widgets\batch_export_dialog.py:44 — atribuição: BatchExportDialog.__init__ ← row2
04824. [x] app\ui\widgets\batch_export_dialog.py:46 — atribuição: BatchExportDialog.__init__ ← ?
04825. [x] app\ui\widgets\batch_export_dialog.py:47 — controle for em BatchExportDialog.__init__
04826. [x] app\ui\widgets\batch_export_dialog.py:52 — atribuição: BatchExportDialog.__init__ ← row3
04827. [x] app\ui\widgets\batch_export_dialog.py:54 — atribuição: BatchExportDialog.__init__ ← ?
04828. [x] app\ui\widgets\batch_export_dialog.py:55 — atribuição: BatchExportDialog.__init__ ← btn_browse
04829. [x] app\ui\widgets\batch_export_dialog.py:61 — atribuição: BatchExportDialog.__init__ ← btn_go
04830. [x] app\ui\widgets\batch_export_dialog.py:66 — definir/revisar FunctionDef: BatchExportDialog._browse
04831. [x] app\ui\widgets\batch_export_dialog.py:66 — revisar facet 'assinatura/args consistentes' em BatchExportDialog._browse
04832. [x] app\ui\widgets\batch_export_dialog.py:66 — revisar facet 'docstring em português' em BatchExportDialog._browse
04833. [x] app\ui\widgets\batch_export_dialog.py:66 — revisar facet 'nomenclatura clara (PEP8)' em BatchExportDialog._browse
04834. [x] app\ui\widgets\batch_export_dialog.py:66 — revisar facet 'type hints presentes' em BatchExportDialog._browse
04835. [x] app\ui\widgets\batch_export_dialog.py:66 — revisar facet 'tratamento de erros adequado' em BatchExportDialog._browse
04836. [x] app\ui\widgets\batch_export_dialog.py:66 — revisar facet 'sem comentários inline desnecessários' em BatchExportDialog._browse
04837. [x] app\ui\widgets\batch_export_dialog.py:66 — revisar facet 'não imprime side-effects na UI/IO' em BatchExportDialog._browse
04838. [x] app\ui\widgets\batch_export_dialog.py:66 — revisar facet 'thread-safety revisada' em BatchExportDialog._browse
04839. [x] app\ui\widgets\batch_export_dialog.py:66 — revisar facet 'performance (sem loops O(n^2))' em BatchExportDialog._browse
04840. [x] app\ui\widgets\batch_export_dialog.py:66 — revisar facet 'coberto por testes' em BatchExportDialog._browse
04841. [x] app\ui\widgets\batch_export_dialog.py:67 — atribuição: BatchExportDialog._browse ← directory
04842. [x] app\ui\widgets\batch_export_dialog.py:68 — controle if em BatchExportDialog._browse
04843. [x] app\ui\widgets\batch_export_dialog.py:71 — definir/revisar FunctionDef: BatchExportDialog._emit
04844. [x] app\ui\widgets\batch_export_dialog.py:71 — revisar facet 'assinatura/args consistentes' em BatchExportDialog._emit
04845. [x] app\ui\widgets\batch_export_dialog.py:71 — revisar facet 'docstring em português' em BatchExportDialog._emit
04846. [x] app\ui\widgets\batch_export_dialog.py:71 — revisar facet 'nomenclatura clara (PEP8)' em BatchExportDialog._emit
04847. [x] app\ui\widgets\batch_export_dialog.py:71 — revisar facet 'type hints presentes' em BatchExportDialog._emit
04848. [x] app\ui\widgets\batch_export_dialog.py:71 — revisar facet 'tratamento de erros adequado' em BatchExportDialog._emit
04849. [x] app\ui\widgets\batch_export_dialog.py:71 — revisar facet 'sem comentários inline desnecessários' em BatchExportDialog._emit
04850. [x] app\ui\widgets\batch_export_dialog.py:71 — revisar facet 'não imprime side-effects na UI/IO' em BatchExportDialog._emit
04851. [x] app\ui\widgets\batch_export_dialog.py:71 — revisar facet 'thread-safety revisada' em BatchExportDialog._emit
04852. [x] app\ui\widgets\batch_export_dialog.py:71 — revisar facet 'performance (sem loops O(n^2))' em BatchExportDialog._emit
04853. [x] app\ui\widgets\batch_export_dialog.py:71 — revisar facet 'coberto por testes' em BatchExportDialog._emit
04854. [x] app\ui\widgets\batch_export_dialog.py:72 — atribuição: BatchExportDialog._emit ← version_id
04855. [x] app\ui\widgets\batch_export_dialog.py:73 — controle if em BatchExportDialog._emit
04856. [x] app\ui\widgets\batch_export_dialog.py:74 — return em BatchExportDialog._emit
04857. [x] Existência e estrutura do módulo: app\ui\widgets\comparison_dialog.py
04858. [x] app\ui\widgets\comparison_dialog.py:3 — import: __future__
04859. [x] app\ui\widgets\comparison_dialog.py:5 — import: PySide6.QtWidgets
04860. [x] app\ui\widgets\comparison_dialog.py:13 — import: app.services.comparison_service
04861. [x] app\ui\widgets\comparison_dialog.py:16 — definir/revisar ClassDef: ComparisonDialog
04862. [x] app\ui\widgets\comparison_dialog.py:17 — definir/revisar FunctionDef: ComparisonDialog.__init__
04863. [x] app\ui\widgets\comparison_dialog.py:17 — revisar facet 'assinatura/args consistentes' em ComparisonDialog.__init__
04864. [x] app\ui\widgets\comparison_dialog.py:17 — revisar facet 'docstring em português' em ComparisonDialog.__init__
04865. [x] app\ui\widgets\comparison_dialog.py:17 — revisar facet 'nomenclatura clara (PEP8)' em ComparisonDialog.__init__
04866. [x] app\ui\widgets\comparison_dialog.py:17 — revisar facet 'type hints presentes' em ComparisonDialog.__init__
04867. [x] app\ui\widgets\comparison_dialog.py:17 — revisar facet 'tratamento de erros adequado' em ComparisonDialog.__init__
04868. [x] app\ui\widgets\comparison_dialog.py:17 — revisar facet 'sem comentários inline desnecessários' em ComparisonDialog.__init__
04869. [x] app\ui\widgets\comparison_dialog.py:17 — revisar facet 'não imprime side-effects na UI/IO' em ComparisonDialog.__init__
04870. [x] app\ui\widgets\comparison_dialog.py:17 — revisar facet 'thread-safety revisada' em ComparisonDialog.__init__
04871. [x] app\ui\widgets\comparison_dialog.py:17 — revisar facet 'performance (sem loops O(n^2))' em ComparisonDialog.__init__
04872. [x] app\ui\widgets\comparison_dialog.py:17 — revisar facet 'coberto por testes' em ComparisonDialog.__init__
04873. [x] app\ui\widgets\comparison_dialog.py:24 — atribuição: ComparisonDialog.__init__ ← layout
04874. [x] app\ui\widgets\comparison_dialog.py:26 — atribuição: ComparisonDialog.__init__ ← ?
04875. [x] app\ui\widgets\comparison_dialog.py:27 — atribuição: ComparisonDialog.__init__ ← header_labels
04876. [x] app\ui\widgets\comparison_dialog.py:31 — controle for em ComparisonDialog.__init__
04877. [x] app\ui\widgets\comparison_dialog.py:47 — atribuição: ComparisonDialog.__init__ ← ?
04878. [x] Existência e estrutura do módulo: app\ui\widgets\correlation_dialog.py
04879. [x] app\ui\widgets\correlation_dialog.py:3 — import: __future__
04880. [x] app\ui\widgets\correlation_dialog.py:5 — import: typing
04881. [x] app\ui\widgets\correlation_dialog.py:7 — import: numpy
04882. [x] app\ui\widgets\correlation_dialog.py:8 — import: PySide6.QtCore
04883. [x] app\ui\widgets\correlation_dialog.py:9 — import: PySide6.QtWidgets
04884. [x] app\ui\widgets\correlation_dialog.py:20 — import: app.services.correlation_service
04885. [x] app\ui\widgets\correlation_dialog.py:23 — definir/revisar FunctionDef: _color_from_value
04886. [x] app\ui\widgets\correlation_dialog.py:23 — revisar facet 'assinatura/args consistentes' em _color_from_value
04887. [x] app\ui\widgets\correlation_dialog.py:23 — revisar facet 'docstring em português' em _color_from_value
04888. [x] app\ui\widgets\correlation_dialog.py:23 — revisar facet 'nomenclatura clara (PEP8)' em _color_from_value
04889. [x] app\ui\widgets\correlation_dialog.py:23 — revisar facet 'type hints presentes' em _color_from_value
04890. [x] app\ui\widgets\correlation_dialog.py:23 — revisar facet 'tratamento de erros adequado' em _color_from_value
04891. [x] app\ui\widgets\correlation_dialog.py:23 — revisar facet 'sem comentários inline desnecessários' em _color_from_value
04892. [x] app\ui\widgets\correlation_dialog.py:23 — revisar facet 'não imprime side-effects na UI/IO' em _color_from_value
04893. [x] app\ui\widgets\correlation_dialog.py:23 — revisar facet 'thread-safety revisada' em _color_from_value
04894. [x] app\ui\widgets\correlation_dialog.py:23 — revisar facet 'performance (sem loops O(n^2))' em _color_from_value
04895. [x] app\ui\widgets\correlation_dialog.py:23 — revisar facet 'coberto por testes' em _color_from_value
04896. [x] app\ui\widgets\correlation_dialog.py:24 — import: PySide6.QtGui
04897. [x] app\ui\widgets\correlation_dialog.py:27 — controle if em _color_from_value
04898. [x] app\ui\widgets\correlation_dialog.py:28 — return em _color_from_value
04899. [x] app\ui\widgets\correlation_dialog.py:29 — return em _color_from_value
04900. [x] app\ui\widgets\correlation_dialog.py:32 — definir/revisar ClassDef: CorrelationDialog
04901. [x] app\ui\widgets\correlation_dialog.py:33 — atribuição: CorrelationDialog ← accepted_correlation
04902. [x] app\ui\widgets\correlation_dialog.py:35 — definir/revisar FunctionDef: CorrelationDialog.__init__
04903. [x] app\ui\widgets\correlation_dialog.py:35 — revisar facet 'assinatura/args consistentes' em CorrelationDialog.__init__
04904. [x] app\ui\widgets\correlation_dialog.py:35 — revisar facet 'docstring em português' em CorrelationDialog.__init__
04905. [x] app\ui\widgets\correlation_dialog.py:35 — revisar facet 'nomenclatura clara (PEP8)' em CorrelationDialog.__init__
04906. [x] app\ui\widgets\correlation_dialog.py:35 — revisar facet 'type hints presentes' em CorrelationDialog.__init__
04907. [x] app\ui\widgets\correlation_dialog.py:35 — revisar facet 'tratamento de erros adequado' em CorrelationDialog.__init__
04908. [x] app\ui\widgets\correlation_dialog.py:35 — revisar facet 'sem comentários inline desnecessários' em CorrelationDialog.__init__
04909. [x] app\ui\widgets\correlation_dialog.py:35 — revisar facet 'não imprime side-effects na UI/IO' em CorrelationDialog.__init__
04910. [x] app\ui\widgets\correlation_dialog.py:35 — revisar facet 'thread-safety revisada' em CorrelationDialog.__init__
04911. [x] app\ui\widgets\correlation_dialog.py:35 — revisar facet 'performance (sem loops O(n^2))' em CorrelationDialog.__init__
04912. [x] app\ui\widgets\correlation_dialog.py:35 — revisar facet 'coberto por testes' em CorrelationDialog.__init__
04913. [x] app\ui\widgets\correlation_dialog.py:38 — atribuição: CorrelationDialog.__init__ ← ?
04914. [x] app\ui\widgets\correlation_dialog.py:39 — atribuição: CorrelationDialog.__init__ ← ?
04915. [x] app\ui\widgets\correlation_dialog.py:40 — controle if em CorrelationDialog.__init__
04916. [x] app\ui\widgets\correlation_dialog.py:41 — atribuição: CorrelationDialog.__init__ ← corr
04917. [x] app\ui\widgets\correlation_dialog.py:42 — atribuição: CorrelationDialog.__init__ ← ?
04918. [x] app\ui\widgets\correlation_dialog.py:44 — atribuição: CorrelationDialog.__init__ ← ?
04919. [x] app\ui\widgets\correlation_dialog.py:47 — atribuição: CorrelationDialog.__init__ ← layout
04920. [x] app\ui\widgets\correlation_dialog.py:50 — atribuição: CorrelationDialog.__init__ ← top
04921. [x] app\ui\widgets\correlation_dialog.py:51 — atribuição: CorrelationDialog.__init__ ← ?
04922. [x] app\ui\widgets\correlation_dialog.py:54 — atribuição: CorrelationDialog.__init__ ← btn_resize
04923. [x] app\ui\widgets\correlation_dialog.py:62 — atribuição: CorrelationDialog.__init__ ← bottom
04924. [x] app\ui\widgets\correlation_dialog.py:63 — atribuição: CorrelationDialog.__init__ ← btn_validate
04925. [x] app\ui\widgets\correlation_dialog.py:64 — atribuição: CorrelationDialog.__init__ ← btn_repair
04926. [x] app\ui\widgets\correlation_dialog.py:65 — atribuição: CorrelationDialog.__init__ ← btn_ok
04927. [x] app\ui\widgets\correlation_dialog.py:77 — atribuição: CorrelationDialog.__init__ ← ?
04928. [x] app\ui\widgets\correlation_dialog.py:81 — definir/revisar FunctionDef: CorrelationDialog._fill
04929. [x] app\ui\widgets\correlation_dialog.py:81 — revisar facet 'assinatura/args consistentes' em CorrelationDialog._fill
04930. [x] app\ui\widgets\correlation_dialog.py:81 — revisar facet 'docstring em português' em CorrelationDialog._fill
04931. [x] app\ui\widgets\correlation_dialog.py:81 — revisar facet 'nomenclatura clara (PEP8)' em CorrelationDialog._fill
04932. [x] app\ui\widgets\correlation_dialog.py:81 — revisar facet 'type hints presentes' em CorrelationDialog._fill
04933. [x] app\ui\widgets\correlation_dialog.py:81 — revisar facet 'tratamento de erros adequado' em CorrelationDialog._fill
04934. [x] app\ui\widgets\correlation_dialog.py:81 — revisar facet 'sem comentários inline desnecessários' em CorrelationDialog._fill
04935. [x] app\ui\widgets\correlation_dialog.py:81 — revisar facet 'não imprime side-effects na UI/IO' em CorrelationDialog._fill
04936. [x] app\ui\widgets\correlation_dialog.py:81 — revisar facet 'thread-safety revisada' em CorrelationDialog._fill
04937. [x] app\ui\widgets\correlation_dialog.py:81 — revisar facet 'performance (sem loops O(n^2))' em CorrelationDialog._fill
04938. [x] app\ui\widgets\correlation_dialog.py:81 — revisar facet 'coberto por testes' em CorrelationDialog._fill
04939. [x] app\ui\widgets\correlation_dialog.py:83 — controle for em CorrelationDialog._fill
04940. [x] app\ui\widgets\correlation_dialog.py:85 — controle for em CorrelationDialog._fill
04941. [x] app\ui\widgets\correlation_dialog.py:86 — atribuição: CorrelationDialog._fill ← item
04942. [x] app\ui\widgets\correlation_dialog.py:90 — definir/revisar FunctionDef: CorrelationDialog._read_matrix
04943. [x] app\ui\widgets\correlation_dialog.py:90 — revisar facet 'assinatura/args consistentes' em CorrelationDialog._read_matrix
04944. [x] app\ui\widgets\correlation_dialog.py:90 — revisar facet 'docstring em português' em CorrelationDialog._read_matrix
04945. [x] app\ui\widgets\correlation_dialog.py:90 — revisar facet 'nomenclatura clara (PEP8)' em CorrelationDialog._read_matrix
04946. [x] app\ui\widgets\correlation_dialog.py:90 — revisar facet 'type hints presentes' em CorrelationDialog._read_matrix
04947. [x] app\ui\widgets\correlation_dialog.py:90 — revisar facet 'tratamento de erros adequado' em CorrelationDialog._read_matrix
04948. [x] app\ui\widgets\correlation_dialog.py:90 — revisar facet 'sem comentários inline desnecessários' em CorrelationDialog._read_matrix
04949. [x] app\ui\widgets\correlation_dialog.py:90 — revisar facet 'não imprime side-effects na UI/IO' em CorrelationDialog._read_matrix
04950. [x] app\ui\widgets\correlation_dialog.py:90 — revisar facet 'thread-safety revisada' em CorrelationDialog._read_matrix
04951. [x] app\ui\widgets\correlation_dialog.py:90 — revisar facet 'performance (sem loops O(n^2))' em CorrelationDialog._read_matrix
04952. [x] app\ui\widgets\correlation_dialog.py:90 — revisar facet 'coberto por testes' em CorrelationDialog._read_matrix
04953. [x] app\ui\widgets\correlation_dialog.py:91 — atribuição: CorrelationDialog._read_matrix ← n
04954. [x] app\ui\widgets\correlation_dialog.py:92 — atribuição: CorrelationDialog._read_matrix ← matrix
04955. [x] app\ui\widgets\correlation_dialog.py:93 — atribuição: CorrelationDialog._read_matrix ← current
04956. [x] app\ui\widgets\correlation_dialog.py:94 — controle for em CorrelationDialog._read_matrix
04957. [x] app\ui\widgets\correlation_dialog.py:95 — atribuição: CorrelationDialog._read_matrix ← row
04958. [x] app\ui\widgets\correlation_dialog.py:96 — controle for em CorrelationDialog._read_matrix
04959. [x] app\ui\widgets\correlation_dialog.py:97 — atribuição: CorrelationDialog._read_matrix ← text
04960. [x] app\ui\widgets\correlation_dialog.py:98 — try em CorrelationDialog._read_matrix
04961. [x] app\ui\widgets\correlation_dialog.py:103 — atribuição: CorrelationDialog._read_matrix ← ?
04962. [x] app\ui\widgets\correlation_dialog.py:104 — return em CorrelationDialog._read_matrix
04963. [x] app\ui\widgets\correlation_dialog.py:106 — definir/revisar FunctionDef: CorrelationDialog._validate
04964. [x] app\ui\widgets\correlation_dialog.py:106 — revisar facet 'assinatura/args consistentes' em CorrelationDialog._validate
04965. [x] app\ui\widgets\correlation_dialog.py:106 — revisar facet 'docstring em português' em CorrelationDialog._validate
04966. [x] app\ui\widgets\correlation_dialog.py:106 — revisar facet 'nomenclatura clara (PEP8)' em CorrelationDialog._validate
04967. [x] app\ui\widgets\correlation_dialog.py:106 — revisar facet 'type hints presentes' em CorrelationDialog._validate
04968. [x] app\ui\widgets\correlation_dialog.py:106 — revisar facet 'tratamento de erros adequado' em CorrelationDialog._validate
04969. [x] app\ui\widgets\correlation_dialog.py:106 — revisar facet 'sem comentários inline desnecessários' em CorrelationDialog._validate
04970. [x] app\ui\widgets\correlation_dialog.py:106 — revisar facet 'não imprime side-effects na UI/IO' em CorrelationDialog._validate
04971. [x] app\ui\widgets\correlation_dialog.py:106 — revisar facet 'thread-safety revisada' em CorrelationDialog._validate
04972. [x] app\ui\widgets\correlation_dialog.py:106 — revisar facet 'performance (sem loops O(n^2))' em CorrelationDialog._validate
04973. [x] app\ui\widgets\correlation_dialog.py:106 — revisar facet 'coberto por testes' em CorrelationDialog._validate
04974. [x] app\ui\widgets\correlation_dialog.py:107 — atribuição: CorrelationDialog._validate ← ?
04975. [x] app\ui\widgets\correlation_dialog.py:110 — definir/revisar FunctionDef: CorrelationDialog._repair
04976. [x] app\ui\widgets\correlation_dialog.py:110 — revisar facet 'assinatura/args consistentes' em CorrelationDialog._repair
04977. [x] app\ui\widgets\correlation_dialog.py:110 — revisar facet 'docstring em português' em CorrelationDialog._repair
04978. [x] app\ui\widgets\correlation_dialog.py:110 — revisar facet 'nomenclatura clara (PEP8)' em CorrelationDialog._repair
04979. [x] app\ui\widgets\correlation_dialog.py:110 — revisar facet 'type hints presentes' em CorrelationDialog._repair
04980. [x] app\ui\widgets\correlation_dialog.py:110 — revisar facet 'tratamento de erros adequado' em CorrelationDialog._repair
04981. [x] app\ui\widgets\correlation_dialog.py:110 — revisar facet 'sem comentários inline desnecessários' em CorrelationDialog._repair
04982. [x] app\ui\widgets\correlation_dialog.py:110 — revisar facet 'não imprime side-effects na UI/IO' em CorrelationDialog._repair
04983. [x] app\ui\widgets\correlation_dialog.py:110 — revisar facet 'thread-safety revisada' em CorrelationDialog._repair
04984. [x] app\ui\widgets\correlation_dialog.py:110 — revisar facet 'performance (sem loops O(n^2))' em CorrelationDialog._repair
04985. [x] app\ui\widgets\correlation_dialog.py:110 — revisar facet 'coberto por testes' em CorrelationDialog._repair
04986. [x] app\ui\widgets\correlation_dialog.py:111 — atribuição: CorrelationDialog._repair ← repaired
04987. [x] app\ui\widgets\correlation_dialog.py:112 — atribuição: CorrelationDialog._repair ← ?
04988. [x] app\ui\widgets\correlation_dialog.py:116 — definir/revisar FunctionDef: CorrelationDialog._resize
04989. [x] app\ui\widgets\correlation_dialog.py:116 — revisar facet 'assinatura/args consistentes' em CorrelationDialog._resize
04990. [x] app\ui\widgets\correlation_dialog.py:116 — revisar facet 'docstring em português' em CorrelationDialog._resize
04991. [x] app\ui\widgets\correlation_dialog.py:116 — revisar facet 'nomenclatura clara (PEP8)' em CorrelationDialog._resize
04992. [x] app\ui\widgets\correlation_dialog.py:116 — revisar facet 'type hints presentes' em CorrelationDialog._resize
04993. [x] app\ui\widgets\correlation_dialog.py:116 — revisar facet 'tratamento de erros adequado' em CorrelationDialog._resize
04994. [x] app\ui\widgets\correlation_dialog.py:116 — revisar facet 'sem comentários inline desnecessários' em CorrelationDialog._resize
04995. [x] app\ui\widgets\correlation_dialog.py:116 — revisar facet 'não imprime side-effects na UI/IO' em CorrelationDialog._resize
04996. [x] app\ui\widgets\correlation_dialog.py:116 — revisar facet 'thread-safety revisada' em CorrelationDialog._resize
04997. [x] app\ui\widgets\correlation_dialog.py:116 — revisar facet 'performance (sem loops O(n^2))' em CorrelationDialog._resize
04998. [x] app\ui\widgets\correlation_dialog.py:116 — revisar facet 'coberto por testes' em CorrelationDialog._resize
04999. [x] app\ui\widgets\correlation_dialog.py:117 — atribuição: CorrelationDialog._resize ← n
05000. [x] app\ui\widgets\correlation_dialog.py:118 — atribuição: CorrelationDialog._resize ← old
05001. [x] app\ui\widgets\correlation_dialog.py:119 — atribuição: CorrelationDialog._resize ← identity
05002. [x] app\ui\widgets\correlation_dialog.py:120 — controle for em CorrelationDialog._resize
05003. [x] app\ui\widgets\correlation_dialog.py:121 — controle for em CorrelationDialog._resize
05004. [x] app\ui\widgets\correlation_dialog.py:122 — atribuição: CorrelationDialog._resize ← ?
05005. [x] app\ui\widgets\correlation_dialog.py:124 — atribuição: CorrelationDialog._resize ← ?
05006. [x] app\ui\widgets\correlation_dialog.py:125 — atribuição: CorrelationDialog._resize ← ?
05007. [x] app\ui\widgets\correlation_dialog.py:132 — definir/revisar FunctionDef: CorrelationDialog._apply
05008. [x] app\ui\widgets\correlation_dialog.py:132 — revisar facet 'assinatura/args consistentes' em CorrelationDialog._apply
05009. [x] app\ui\widgets\correlation_dialog.py:132 — revisar facet 'docstring em português' em CorrelationDialog._apply
05010. [x] app\ui\widgets\correlation_dialog.py:132 — revisar facet 'nomenclatura clara (PEP8)' em CorrelationDialog._apply
05011. [x] app\ui\widgets\correlation_dialog.py:132 — revisar facet 'type hints presentes' em CorrelationDialog._apply
05012. [x] app\ui\widgets\correlation_dialog.py:132 — revisar facet 'tratamento de erros adequado' em CorrelationDialog._apply
05013. [x] app\ui\widgets\correlation_dialog.py:132 — revisar facet 'sem comentários inline desnecessários' em CorrelationDialog._apply
05014. [x] app\ui\widgets\correlation_dialog.py:132 — revisar facet 'não imprime side-effects na UI/IO' em CorrelationDialog._apply
05015. [x] app\ui\widgets\correlation_dialog.py:132 — revisar facet 'thread-safety revisada' em CorrelationDialog._apply
05016. [x] app\ui\widgets\correlation_dialog.py:132 — revisar facet 'performance (sem loops O(n^2))' em CorrelationDialog._apply
05017. [x] app\ui\widgets\correlation_dialog.py:132 — revisar facet 'coberto por testes' em CorrelationDialog._apply
05018. [x] app\ui\widgets\correlation_dialog.py:133 — atribuição: CorrelationDialog._apply ← matrix
05019. [x] app\ui\widgets\correlation_dialog.py:134 — atribuição: CorrelationDialog._apply ← ?
05020. [x] app\ui\widgets\correlation_dialog.py:135 — controle if em CorrelationDialog._apply
05021. [x] app\ui\widgets\correlation_dialog.py:137 — return em CorrelationDialog._apply
05022. [x] Existência e estrutura do módulo: app\ui\widgets\dashboard_panel.py
05023. [x] app\ui\widgets\dashboard_panel.py:3 — import: __future__
05024. [x] app\ui\widgets\dashboard_panel.py:5 — import: PySide6.QtWidgets
05025. [x] app\ui\widgets\dashboard_panel.py:15 — import: app.services.metrics_service
05026. [x] app\ui\widgets\dashboard_panel.py:18 — definir/revisar ClassDef: KpiTile
05027. [x] app\ui\widgets\dashboard_panel.py:19 — definir/revisar FunctionDef: KpiTile.__init__
05028. [x] app\ui\widgets\dashboard_panel.py:19 — revisar facet 'assinatura/args consistentes' em KpiTile.__init__
05029. [x] app\ui\widgets\dashboard_panel.py:19 — revisar facet 'docstring em português' em KpiTile.__init__
05030. [x] app\ui\widgets\dashboard_panel.py:19 — revisar facet 'nomenclatura clara (PEP8)' em KpiTile.__init__
05031. [x] app\ui\widgets\dashboard_panel.py:19 — revisar facet 'type hints presentes' em KpiTile.__init__
05032. [x] app\ui\widgets\dashboard_panel.py:19 — revisar facet 'tratamento de erros adequado' em KpiTile.__init__
05033. [x] app\ui\widgets\dashboard_panel.py:19 — revisar facet 'sem comentários inline desnecessários' em KpiTile.__init__
05034. [x] app\ui\widgets\dashboard_panel.py:19 — revisar facet 'não imprime side-effects na UI/IO' em KpiTile.__init__
05035. [x] app\ui\widgets\dashboard_panel.py:19 — revisar facet 'thread-safety revisada' em KpiTile.__init__
05036. [x] app\ui\widgets\dashboard_panel.py:19 — revisar facet 'performance (sem loops O(n^2))' em KpiTile.__init__
05037. [x] app\ui\widgets\dashboard_panel.py:19 — revisar facet 'coberto por testes' em KpiTile.__init__
05038. [x] app\ui\widgets\dashboard_panel.py:25 — definir/revisar ClassDef: DashboardPanel
05039. [x] app\ui\widgets\dashboard_panel.py:26 — definir/revisar FunctionDef: DashboardPanel.__init__
05040. [x] app\ui\widgets\dashboard_panel.py:26 — revisar facet 'assinatura/args consistentes' em DashboardPanel.__init__
05041. [x] app\ui\widgets\dashboard_panel.py:26 — revisar facet 'docstring em português' em DashboardPanel.__init__
05042. [x] app\ui\widgets\dashboard_panel.py:26 — revisar facet 'nomenclatura clara (PEP8)' em DashboardPanel.__init__
05043. [x] app\ui\widgets\dashboard_panel.py:26 — revisar facet 'type hints presentes' em DashboardPanel.__init__
05044. [x] app\ui\widgets\dashboard_panel.py:26 — revisar facet 'tratamento de erros adequado' em DashboardPanel.__init__
05045. [x] app\ui\widgets\dashboard_panel.py:26 — revisar facet 'sem comentários inline desnecessários' em DashboardPanel.__init__
05046. [x] app\ui\widgets\dashboard_panel.py:26 — revisar facet 'não imprime side-effects na UI/IO' em DashboardPanel.__init__
05047. [x] app\ui\widgets\dashboard_panel.py:26 — revisar facet 'thread-safety revisada' em DashboardPanel.__init__
05048. [x] app\ui\widgets\dashboard_panel.py:26 — revisar facet 'performance (sem loops O(n^2))' em DashboardPanel.__init__
05049. [x] app\ui\widgets\dashboard_panel.py:26 — revisar facet 'coberto por testes' em DashboardPanel.__init__
05050. [x] app\ui\widgets\dashboard_panel.py:28 — atribuição: DashboardPanel.__init__ ← ?
05051. [x] app\ui\widgets\dashboard_panel.py:30 — atribuição: DashboardPanel.__init__ ← layout
05052. [x] app\ui\widgets\dashboard_panel.py:31 — atribuição: DashboardPanel.__init__ ← header
05053. [x] app\ui\widgets\dashboard_panel.py:32 — atribuição: DashboardPanel.__init__ ← ?
05054. [x] app\ui\widgets\dashboard_panel.py:33 — atribuição: DashboardPanel.__init__ ← ?
05055. [x] app\ui\widgets\dashboard_panel.py:34 — atribuição: DashboardPanel.__init__ ← ?
05056. [x] app\ui\widgets\dashboard_panel.py:35 — atribuição: DashboardPanel.__init__ ← ?
05057. [x] app\ui\widgets\dashboard_panel.py:36 — controle for em DashboardPanel.__init__
05058. [x] app\ui\widgets\dashboard_panel.py:40 — atribuição: DashboardPanel.__init__ ← ?
05059. [x] app\ui\widgets\dashboard_panel.py:41 — atribuição: DashboardPanel.__init__ ← ?
05060. [x] app\ui\widgets\dashboard_panel.py:42 — atribuição: DashboardPanel.__init__ ← ?
05061. [x] app\ui\widgets\dashboard_panel.py:43 — atribuição: DashboardPanel.__init__ ← ?
05062. [x] app\ui\widgets\dashboard_panel.py:49 — atribuição: DashboardPanel.__init__ ← ?
05063. [x] app\ui\widgets\dashboard_panel.py:53 — definir/revisar FunctionDef: DashboardPanel._table_tab
05064. [x] app\ui\widgets\dashboard_panel.py:53 — revisar facet 'assinatura/args consistentes' em DashboardPanel._table_tab
05065. [x] app\ui\widgets\dashboard_panel.py:53 — revisar facet 'docstring em português' em DashboardPanel._table_tab
05066. [x] app\ui\widgets\dashboard_panel.py:53 — revisar facet 'nomenclatura clara (PEP8)' em DashboardPanel._table_tab
05067. [x] app\ui\widgets\dashboard_panel.py:53 — revisar facet 'type hints presentes' em DashboardPanel._table_tab
05068. [x] app\ui\widgets\dashboard_panel.py:53 — revisar facet 'tratamento de erros adequado' em DashboardPanel._table_tab
05069. [x] app\ui\widgets\dashboard_panel.py:53 — revisar facet 'sem comentários inline desnecessários' em DashboardPanel._table_tab
05070. [x] app\ui\widgets\dashboard_panel.py:53 — revisar facet 'não imprime side-effects na UI/IO' em DashboardPanel._table_tab
05071. [x] app\ui\widgets\dashboard_panel.py:53 — revisar facet 'thread-safety revisada' em DashboardPanel._table_tab
05072. [x] app\ui\widgets\dashboard_panel.py:53 — revisar facet 'performance (sem loops O(n^2))' em DashboardPanel._table_tab
05073. [x] app\ui\widgets\dashboard_panel.py:53 — revisar facet 'coberto por testes' em DashboardPanel._table_tab
05074. [x] app\ui\widgets\dashboard_panel.py:54 — atribuição: DashboardPanel._table_tab ← table
05075. [x] app\ui\widgets\dashboard_panel.py:57 — return em DashboardPanel._table_tab
05076. [x] app\ui\widgets\dashboard_panel.py:59 — definir/revisar FunctionDef: DashboardPanel.refresh
05077. [x] app\ui\widgets\dashboard_panel.py:59 — revisar facet 'assinatura/args consistentes' em DashboardPanel.refresh
05078. [x] app\ui\widgets\dashboard_panel.py:59 — revisar facet 'docstring em português' em DashboardPanel.refresh
05079. [x] app\ui\widgets\dashboard_panel.py:59 — revisar facet 'nomenclatura clara (PEP8)' em DashboardPanel.refresh
05080. [x] app\ui\widgets\dashboard_panel.py:59 — revisar facet 'type hints presentes' em DashboardPanel.refresh
05081. [x] app\ui\widgets\dashboard_panel.py:59 — revisar facet 'tratamento de erros adequado' em DashboardPanel.refresh
05082. [x] app\ui\widgets\dashboard_panel.py:59 — revisar facet 'sem comentários inline desnecessários' em DashboardPanel.refresh
05083. [x] app\ui\widgets\dashboard_panel.py:59 — revisar facet 'não imprime side-effects na UI/IO' em DashboardPanel.refresh
05084. [x] app\ui\widgets\dashboard_panel.py:59 — revisar facet 'thread-safety revisada' em DashboardPanel.refresh
05085. [x] app\ui\widgets\dashboard_panel.py:59 — revisar facet 'performance (sem loops O(n^2))' em DashboardPanel.refresh
05086. [x] app\ui\widgets\dashboard_panel.py:59 — revisar facet 'coberto por testes' em DashboardPanel.refresh
05087. [x] app\ui\widgets\dashboard_panel.py:60 — controle if em DashboardPanel.refresh
05088. [x] app\ui\widgets\dashboard_panel.py:61 — return em DashboardPanel.refresh
05089. [x] app\ui\widgets\dashboard_panel.py:62 — atribuição: DashboardPanel.refresh ← s
05090. [x] app\ui\widgets\dashboard_panel.py:73 — definir/revisar FunctionDef: DashboardPanel._fill
05091. [x] app\ui\widgets\dashboard_panel.py:73 — revisar facet 'assinatura/args consistentes' em DashboardPanel._fill
05092. [x] app\ui\widgets\dashboard_panel.py:73 — revisar facet 'docstring em português' em DashboardPanel._fill
05093. [x] app\ui\widgets\dashboard_panel.py:73 — revisar facet 'nomenclatura clara (PEP8)' em DashboardPanel._fill
05094. [x] app\ui\widgets\dashboard_panel.py:73 — revisar facet 'type hints presentes' em DashboardPanel._fill
05095. [x] app\ui\widgets\dashboard_panel.py:73 — revisar facet 'tratamento de erros adequado' em DashboardPanel._fill
05096. [x] app\ui\widgets\dashboard_panel.py:73 — revisar facet 'sem comentários inline desnecessários' em DashboardPanel._fill
05097. [x] app\ui\widgets\dashboard_panel.py:73 — revisar facet 'não imprime side-effects na UI/IO' em DashboardPanel._fill
05098. [x] app\ui\widgets\dashboard_panel.py:73 — revisar facet 'thread-safety revisada' em DashboardPanel._fill
05099. [x] app\ui\widgets\dashboard_panel.py:73 — revisar facet 'performance (sem loops O(n^2))' em DashboardPanel._fill
05100. [x] app\ui\widgets\dashboard_panel.py:73 — revisar facet 'coberto por testes' em DashboardPanel._fill
05101. [x] app\ui\widgets\dashboard_panel.py:75 — controle for em DashboardPanel._fill
05102. [x] Existência e estrutura do módulo: app\ui\widgets\distribution_dialog.py
05103. [x] app\ui\widgets\distribution_dialog.py:3 — import: __future__
05104. [x] app\ui\widgets\distribution_dialog.py:5 — import: typing
05105. [x] app\ui\widgets\distribution_dialog.py:7 — import: PySide6.QtCore
05106. [x] app\ui\widgets\distribution_dialog.py:8 — import: PySide6.QtWidgets
05107. [x] app\ui\widgets\distribution_dialog.py:20 — import: app.core.parsing
05108. [x] app\ui\widgets\distribution_dialog.py:21 — import: app.domain.entities
05109. [x] app\ui\widgets\distribution_dialog.py:22 — import: app.infrastructure.distribution_registry
05110. [x] app\ui\widgets\distribution_dialog.py:25 — definir/revisar ClassDef: DistributionDialog
05111. [x] app\ui\widgets\distribution_dialog.py:28 — definir/revisar FunctionDef: DistributionDialog.__init__
05112. [x] app\ui\widgets\distribution_dialog.py:28 — revisar facet 'assinatura/args consistentes' em DistributionDialog.__init__
05113. [x] app\ui\widgets\distribution_dialog.py:28 — revisar facet 'docstring em português' em DistributionDialog.__init__
05114. [x] app\ui\widgets\distribution_dialog.py:28 — revisar facet 'nomenclatura clara (PEP8)' em DistributionDialog.__init__
05115. [x] app\ui\widgets\distribution_dialog.py:28 — revisar facet 'type hints presentes' em DistributionDialog.__init__
05116. [x] app\ui\widgets\distribution_dialog.py:28 — revisar facet 'tratamento de erros adequado' em DistributionDialog.__init__
05117. [x] app\ui\widgets\distribution_dialog.py:28 — revisar facet 'sem comentários inline desnecessários' em DistributionDialog.__init__
05118. [x] app\ui\widgets\distribution_dialog.py:28 — revisar facet 'não imprime side-effects na UI/IO' em DistributionDialog.__init__
05119. [x] app\ui\widgets\distribution_dialog.py:28 — revisar facet 'thread-safety revisada' em DistributionDialog.__init__
05120. [x] app\ui\widgets\distribution_dialog.py:28 — revisar facet 'performance (sem loops O(n^2))' em DistributionDialog.__init__
05121. [x] app\ui\widgets\distribution_dialog.py:28 — revisar facet 'coberto por testes' em DistributionDialog.__init__
05122. [x] app\ui\widgets\distribution_dialog.py:37 — atribuição: DistributionDialog.__init__ ← ?
05123. [x] app\ui\widgets\distribution_dialog.py:38 — atribuição: DistributionDialog.__init__ ← ?
05124. [x] app\ui\widgets\distribution_dialog.py:39 — atribuição: DistributionDialog.__init__ ← ?
05125. [x] app\ui\widgets\distribution_dialog.py:40 — atribuição: DistributionDialog.__init__ ← ?
05126. [x] app\ui\widgets\distribution_dialog.py:42 — atribuição: DistributionDialog.__init__ ← layout
05127. [x] app\ui\widgets\distribution_dialog.py:43 — atribuição: DistributionDialog.__init__ ← ?
05128. [x] app\ui\widgets\distribution_dialog.py:46 — atribuição: DistributionDialog.__init__ ← ?
05129. [x] app\ui\widgets\distribution_dialog.py:51 — atribuição: DistributionDialog.__init__ ← ?
05130. [x] app\ui\widgets\distribution_dialog.py:54 — atribuição: DistributionDialog.__init__ ← ?
05131. [x] app\ui\widgets\distribution_dialog.py:56 — atribuição: DistributionDialog.__init__ ← ?
05132. [x] app\ui\widgets\distribution_dialog.py:59 — atribuição: DistributionDialog.__init__ ← ?
05133. [x] app\ui\widgets\distribution_dialog.py:60 — atribuição: DistributionDialog.__init__ ← ?
05134. [x] app\ui\widgets\distribution_dialog.py:63 — atribuição: DistributionDialog.__init__ ← buttons
05135. [x] app\ui\widgets\distribution_dialog.py:70 — controle if em DistributionDialog.__init__
05136. [x] app\ui\widgets\distribution_dialog.py:72 — atribuição: DistributionDialog.__init__ ← ?
05137. [x] app\ui\widgets\distribution_dialog.py:73 — atribuição: DistributionDialog.__init__ ← ?
05138. [x] app\ui\widgets\distribution_dialog.py:77 — definir/revisar FunctionDef: DistributionDialog._rebuild_dists
05139. [x] app\ui\widgets\distribution_dialog.py:77 — revisar facet 'assinatura/args consistentes' em DistributionDialog._rebuild_dists
05140. [x] app\ui\widgets\distribution_dialog.py:77 — revisar facet 'docstring em português' em DistributionDialog._rebuild_dists
05141. [x] app\ui\widgets\distribution_dialog.py:77 — revisar facet 'nomenclatura clara (PEP8)' em DistributionDialog._rebuild_dists
05142. [x] app\ui\widgets\distribution_dialog.py:77 — revisar facet 'type hints presentes' em DistributionDialog._rebuild_dists
05143. [x] app\ui\widgets\distribution_dialog.py:77 — revisar facet 'tratamento de erros adequado' em DistributionDialog._rebuild_dists
05144. [x] app\ui\widgets\distribution_dialog.py:77 — revisar facet 'sem comentários inline desnecessários' em DistributionDialog._rebuild_dists
05145. [x] app\ui\widgets\distribution_dialog.py:77 — revisar facet 'não imprime side-effects na UI/IO' em DistributionDialog._rebuild_dists
05146. [x] app\ui\widgets\distribution_dialog.py:77 — revisar facet 'thread-safety revisada' em DistributionDialog._rebuild_dists
05147. [x] app\ui\widgets\distribution_dialog.py:77 — revisar facet 'performance (sem loops O(n^2))' em DistributionDialog._rebuild_dists
05148. [x] app\ui\widgets\distribution_dialog.py:77 — revisar facet 'coberto por testes' em DistributionDialog._rebuild_dists
05149. [x] app\ui\widgets\distribution_dialog.py:78 — atribuição: DistributionDialog._rebuild_dists ← provider
05150. [x] app\ui\widgets\distribution_dialog.py:79 — controle if em DistributionDialog._rebuild_dists
05151. [x] app\ui\widgets\distribution_dialog.py:81 — return em DistributionDialog._rebuild_dists
05152. [x] app\ui\widgets\distribution_dialog.py:85 — controle if em DistributionDialog._rebuild_dists
05153. [x] app\ui\widgets\distribution_dialog.py:86 — atribuição: DistributionDialog._rebuild_dists ← index
05154. [x] app\ui\widgets\distribution_dialog.py:87 — controle if em DistributionDialog._rebuild_dists
05155. [x] app\ui\widgets\distribution_dialog.py:92 — definir/revisar FunctionDef: DistributionDialog._rebuild_fields
05156. [x] app\ui\widgets\distribution_dialog.py:92 — revisar facet 'assinatura/args consistentes' em DistributionDialog._rebuild_fields
05157. [x] app\ui\widgets\distribution_dialog.py:92 — revisar facet 'docstring em português' em DistributionDialog._rebuild_fields
05158. [x] app\ui\widgets\distribution_dialog.py:92 — revisar facet 'nomenclatura clara (PEP8)' em DistributionDialog._rebuild_fields
05159. [x] app\ui\widgets\distribution_dialog.py:92 — revisar facet 'type hints presentes' em DistributionDialog._rebuild_fields
05160. [x] app\ui\widgets\distribution_dialog.py:92 — revisar facet 'tratamento de erros adequado' em DistributionDialog._rebuild_fields
05161. [x] app\ui\widgets\distribution_dialog.py:92 — revisar facet 'sem comentários inline desnecessários' em DistributionDialog._rebuild_fields
05162. [x] app\ui\widgets\distribution_dialog.py:92 — revisar facet 'não imprime side-effects na UI/IO' em DistributionDialog._rebuild_fields
05163. [x] app\ui\widgets\distribution_dialog.py:92 — revisar facet 'thread-safety revisada' em DistributionDialog._rebuild_fields
05164. [x] app\ui\widgets\distribution_dialog.py:92 — revisar facet 'performance (sem loops O(n^2))' em DistributionDialog._rebuild_fields
05165. [x] app\ui\widgets\distribution_dialog.py:92 — revisar facet 'coberto por testes' em DistributionDialog._rebuild_fields
05166. [x] app\ui\widgets\distribution_dialog.py:93 — controle while em DistributionDialog._rebuild_fields
05167. [x] app\ui\widgets\distribution_dialog.py:94 — atribuição: DistributionDialog._rebuild_fields ← item
05168. [x] app\ui\widgets\distribution_dialog.py:95 — controle if em DistributionDialog._rebuild_fields
05169. [x] app\ui\widgets\distribution_dialog.py:97 — atribuição: DistributionDialog._rebuild_fields ← ?
05170. [x] app\ui\widgets\distribution_dialog.py:99 — atribuição: DistributionDialog._rebuild_fields ← provider
05171. [x] app\ui\widgets\distribution_dialog.py:100 — controle if em DistributionDialog._rebuild_fields
05172. [x] app\ui\widgets\distribution_dialog.py:101 — return em DistributionDialog._rebuild_fields
05173. [x] app\ui\widgets\distribution_dialog.py:105 — controle for em DistributionDialog._rebuild_fields
05174. [x] app\ui\widgets\distribution_dialog.py:106 — atribuição: DistributionDialog._rebuild_fields ← name
05175. [x] app\ui\widgets\distribution_dialog.py:107 — atribuição: DistributionDialog._rebuild_fields ← default
05176. [x] app\ui\widgets\distribution_dialog.py:108 — atribuição: DistributionDialog._rebuild_fields ← widget
05177. [x] app\ui\widgets\distribution_dialog.py:115 — atribuição: DistributionDialog._rebuild_fields ← ?
05178. [x] app\ui\widgets\distribution_dialog.py:118 — definir/revisar FunctionDef: DistributionDialog.collect
05179. [x] app\ui\widgets\distribution_dialog.py:118 — revisar facet 'assinatura/args consistentes' em DistributionDialog.collect
05180. [x] app\ui\widgets\distribution_dialog.py:118 — revisar facet 'docstring em português' em DistributionDialog.collect
05181. [x] app\ui\widgets\distribution_dialog.py:118 — revisar facet 'nomenclatura clara (PEP8)' em DistributionDialog.collect
05182. [x] app\ui\widgets\distribution_dialog.py:118 — revisar facet 'type hints presentes' em DistributionDialog.collect
05183. [x] app\ui\widgets\distribution_dialog.py:118 — revisar facet 'tratamento de erros adequado' em DistributionDialog.collect
05184. [x] app\ui\widgets\distribution_dialog.py:118 — revisar facet 'sem comentários inline desnecessários' em DistributionDialog.collect
05185. [x] app\ui\widgets\distribution_dialog.py:118 — revisar facet 'não imprime side-effects na UI/IO' em DistributionDialog.collect
05186. [x] app\ui\widgets\distribution_dialog.py:118 — revisar facet 'thread-safety revisada' em DistributionDialog.collect
05187. [x] app\ui\widgets\distribution_dialog.py:118 — revisar facet 'performance (sem loops O(n^2))' em DistributionDialog.collect
05188. [x] app\ui\widgets\distribution_dialog.py:118 — revisar facet 'coberto por testes' em DistributionDialog.collect
05189. [x] app\ui\widgets\distribution_dialog.py:119 — atribuição: DistributionDialog.collect ← params
05190. [x] app\ui\widgets\distribution_dialog.py:120 — return em DistributionDialog.collect
05191. [x] Existência e estrutura do módulo: app\ui\widgets\experiments_panel.py
05192. [x] app\ui\widgets\experiments_panel.py:3 — import: __future__
05193. [x] app\ui\widgets\experiments_panel.py:5 — import: PySide6.QtCore
05194. [x] app\ui\widgets\experiments_panel.py:6 — import: PySide6.QtWidgets
05195. [x] app\ui\widgets\experiments_panel.py:16 — import: app.ui.models.repository_paged_model
05196. [x] app\ui\widgets\experiments_panel.py:19 — definir/revisar ClassDef: ExperimentsPanel
05197. [x] app\ui\widgets\experiments_panel.py:20 — atribuição: ExperimentsPanel ← compareRequested
05198. [x] app\ui\widgets\experiments_panel.py:22 — definir/revisar FunctionDef: ExperimentsPanel.__init__
05199. [x] app\ui\widgets\experiments_panel.py:22 — revisar facet 'assinatura/args consistentes' em ExperimentsPanel.__init__
05200. [x] app\ui\widgets\experiments_panel.py:22 — revisar facet 'docstring em português' em ExperimentsPanel.__init__
05201. [x] app\ui\widgets\experiments_panel.py:22 — revisar facet 'nomenclatura clara (PEP8)' em ExperimentsPanel.__init__
05202. [x] app\ui\widgets\experiments_panel.py:22 — revisar facet 'type hints presentes' em ExperimentsPanel.__init__
05203. [x] app\ui\widgets\experiments_panel.py:22 — revisar facet 'tratamento de erros adequado' em ExperimentsPanel.__init__
05204. [x] app\ui\widgets\experiments_panel.py:22 — revisar facet 'sem comentários inline desnecessários' em ExperimentsPanel.__init__
05205. [x] app\ui\widgets\experiments_panel.py:22 — revisar facet 'não imprime side-effects na UI/IO' em ExperimentsPanel.__init__
05206. [x] app\ui\widgets\experiments_panel.py:22 — revisar facet 'thread-safety revisada' em ExperimentsPanel.__init__
05207. [x] app\ui\widgets\experiments_panel.py:22 — revisar facet 'performance (sem loops O(n^2))' em ExperimentsPanel.__init__
05208. [x] app\ui\widgets\experiments_panel.py:22 — revisar facet 'coberto por testes' em ExperimentsPanel.__init__
05209. [x] app\ui\widgets\experiments_panel.py:24 — atribuição: ExperimentsPanel.__init__ ← ?
05210. [x] app\ui\widgets\experiments_panel.py:26 — atribuição: ExperimentsPanel.__init__ ← layout
05211. [x] app\ui\widgets\experiments_panel.py:28 — atribuição: ExperimentsPanel.__init__ ← header
05212. [x] app\ui\widgets\experiments_panel.py:29 — atribuição: ExperimentsPanel.__init__ ← ?
05213. [x] app\ui\widgets\experiments_panel.py:30 — atribuição: ExperimentsPanel.__init__ ← btn_prev
05214. [x] app\ui\widgets\experiments_panel.py:31 — atribuição: ExperimentsPanel.__init__ ← btn_next
05215. [x] app\ui\widgets\experiments_panel.py:40 — atribuição: ExperimentsPanel.__init__ ← ?
05216. [x] app\ui\widgets\experiments_panel.py:47 — atribuição: ExperimentsPanel.__init__ ← ?
05217. [x] app\ui\widgets\experiments_panel.py:55 — definir/revisar FunctionDef: ExperimentsPanel._refresh_label
05218. [x] app\ui\widgets\experiments_panel.py:55 — revisar facet 'assinatura/args consistentes' em ExperimentsPanel._refresh_label
05219. [x] app\ui\widgets\experiments_panel.py:55 — revisar facet 'docstring em português' em ExperimentsPanel._refresh_label
05220. [x] app\ui\widgets\experiments_panel.py:55 — revisar facet 'nomenclatura clara (PEP8)' em ExperimentsPanel._refresh_label
05221. [x] app\ui\widgets\experiments_panel.py:55 — revisar facet 'type hints presentes' em ExperimentsPanel._refresh_label
05222. [x] app\ui\widgets\experiments_panel.py:55 — revisar facet 'tratamento de erros adequado' em ExperimentsPanel._refresh_label
05223. [x] app\ui\widgets\experiments_panel.py:55 — revisar facet 'sem comentários inline desnecessários' em ExperimentsPanel._refresh_label
05224. [x] app\ui\widgets\experiments_panel.py:55 — revisar facet 'não imprime side-effects na UI/IO' em ExperimentsPanel._refresh_label
05225. [x] app\ui\widgets\experiments_panel.py:55 — revisar facet 'thread-safety revisada' em ExperimentsPanel._refresh_label
05226. [x] app\ui\widgets\experiments_panel.py:55 — revisar facet 'performance (sem loops O(n^2))' em ExperimentsPanel._refresh_label
05227. [x] app\ui\widgets\experiments_panel.py:55 — revisar facet 'coberto por testes' em ExperimentsPanel._refresh_label
05228. [x] app\ui\widgets\experiments_panel.py:56 — atribuição: ExperimentsPanel._refresh_label ← m
05229. [x] app\ui\widgets\experiments_panel.py:61 — definir/revisar FunctionDef: ExperimentsPanel._prev
05230. [x] app\ui\widgets\experiments_panel.py:61 — revisar facet 'assinatura/args consistentes' em ExperimentsPanel._prev
05231. [x] app\ui\widgets\experiments_panel.py:61 — revisar facet 'docstring em português' em ExperimentsPanel._prev
05232. [x] app\ui\widgets\experiments_panel.py:61 — revisar facet 'nomenclatura clara (PEP8)' em ExperimentsPanel._prev
05233. [x] app\ui\widgets\experiments_panel.py:61 — revisar facet 'type hints presentes' em ExperimentsPanel._prev
05234. [x] app\ui\widgets\experiments_panel.py:61 — revisar facet 'tratamento de erros adequado' em ExperimentsPanel._prev
05235. [x] app\ui\widgets\experiments_panel.py:61 — revisar facet 'sem comentários inline desnecessários' em ExperimentsPanel._prev
05236. [x] app\ui\widgets\experiments_panel.py:61 — revisar facet 'não imprime side-effects na UI/IO' em ExperimentsPanel._prev
05237. [x] app\ui\widgets\experiments_panel.py:61 — revisar facet 'thread-safety revisada' em ExperimentsPanel._prev
05238. [x] app\ui\widgets\experiments_panel.py:61 — revisar facet 'performance (sem loops O(n^2))' em ExperimentsPanel._prev
05239. [x] app\ui\widgets\experiments_panel.py:61 — revisar facet 'coberto por testes' em ExperimentsPanel._prev
05240. [x] app\ui\widgets\experiments_panel.py:65 — definir/revisar FunctionDef: ExperimentsPanel._next
05241. [x] app\ui\widgets\experiments_panel.py:65 — revisar facet 'assinatura/args consistentes' em ExperimentsPanel._next
05242. [x] app\ui\widgets\experiments_panel.py:65 — revisar facet 'docstring em português' em ExperimentsPanel._next
05243. [x] app\ui\widgets\experiments_panel.py:65 — revisar facet 'nomenclatura clara (PEP8)' em ExperimentsPanel._next
05244. [x] app\ui\widgets\experiments_panel.py:65 — revisar facet 'type hints presentes' em ExperimentsPanel._next
05245. [x] app\ui\widgets\experiments_panel.py:65 — revisar facet 'tratamento de erros adequado' em ExperimentsPanel._next
05246. [x] app\ui\widgets\experiments_panel.py:65 — revisar facet 'sem comentários inline desnecessários' em ExperimentsPanel._next
05247. [x] app\ui\widgets\experiments_panel.py:65 — revisar facet 'não imprime side-effects na UI/IO' em ExperimentsPanel._next
05248. [x] app\ui\widgets\experiments_panel.py:65 — revisar facet 'thread-safety revisada' em ExperimentsPanel._next
05249. [x] app\ui\widgets\experiments_panel.py:65 — revisar facet 'performance (sem loops O(n^2))' em ExperimentsPanel._next
05250. [x] app\ui\widgets\experiments_panel.py:65 — revisar facet 'coberto por testes' em ExperimentsPanel._next
05251. [x] app\ui\widgets\experiments_panel.py:69 — definir/revisar FunctionDef: ExperimentsPanel.selected_rows
05252. [x] app\ui\widgets\experiments_panel.py:69 — revisar facet 'assinatura/args consistentes' em ExperimentsPanel.selected_rows
05253. [x] app\ui\widgets\experiments_panel.py:69 — revisar facet 'docstring em português' em ExperimentsPanel.selected_rows
05254. [x] app\ui\widgets\experiments_panel.py:69 — revisar facet 'nomenclatura clara (PEP8)' em ExperimentsPanel.selected_rows
05255. [x] app\ui\widgets\experiments_panel.py:69 — revisar facet 'type hints presentes' em ExperimentsPanel.selected_rows
05256. [x] app\ui\widgets\experiments_panel.py:69 — revisar facet 'tratamento de erros adequado' em ExperimentsPanel.selected_rows
05257. [x] app\ui\widgets\experiments_panel.py:69 — revisar facet 'sem comentários inline desnecessários' em ExperimentsPanel.selected_rows
05258. [x] app\ui\widgets\experiments_panel.py:69 — revisar facet 'não imprime side-effects na UI/IO' em ExperimentsPanel.selected_rows
05259. [x] app\ui\widgets\experiments_panel.py:69 — revisar facet 'thread-safety revisada' em ExperimentsPanel.selected_rows
05260. [x] app\ui\widgets\experiments_panel.py:69 — revisar facet 'performance (sem loops O(n^2))' em ExperimentsPanel.selected_rows
05261. [x] app\ui\widgets\experiments_panel.py:69 — revisar facet 'coberto por testes' em ExperimentsPanel.selected_rows
05262. [x] app\ui\widgets\experiments_panel.py:70 — atribuição: ExperimentsPanel.selected_rows ← selection
05263. [x] app\ui\widgets\experiments_panel.py:71 — atribuição: ExperimentsPanel.selected_rows ← rows
05264. [x] app\ui\widgets\experiments_panel.py:77 — return em ExperimentsPanel.selected_rows
05265. [x] app\ui\widgets\experiments_panel.py:79 — definir/revisar FunctionDef: ExperimentsPanel._emit_compare
05266. [x] app\ui\widgets\experiments_panel.py:79 — revisar facet 'assinatura/args consistentes' em ExperimentsPanel._emit_compare
05267. [x] app\ui\widgets\experiments_panel.py:79 — revisar facet 'docstring em português' em ExperimentsPanel._emit_compare
05268. [x] app\ui\widgets\experiments_panel.py:79 — revisar facet 'nomenclatura clara (PEP8)' em ExperimentsPanel._emit_compare
05269. [x] app\ui\widgets\experiments_panel.py:79 — revisar facet 'type hints presentes' em ExperimentsPanel._emit_compare
05270. [x] app\ui\widgets\experiments_panel.py:79 — revisar facet 'tratamento de erros adequado' em ExperimentsPanel._emit_compare
05271. [x] app\ui\widgets\experiments_panel.py:79 — revisar facet 'sem comentários inline desnecessários' em ExperimentsPanel._emit_compare
05272. [x] app\ui\widgets\experiments_panel.py:79 — revisar facet 'não imprime side-effects na UI/IO' em ExperimentsPanel._emit_compare
05273. [x] app\ui\widgets\experiments_panel.py:79 — revisar facet 'thread-safety revisada' em ExperimentsPanel._emit_compare
05274. [x] app\ui\widgets\experiments_panel.py:79 — revisar facet 'performance (sem loops O(n^2))' em ExperimentsPanel._emit_compare
05275. [x] app\ui\widgets\experiments_panel.py:79 — revisar facet 'coberto por testes' em ExperimentsPanel._emit_compare
05276. [x] app\ui\widgets\experiments_panel.py:80 — atribuição: ExperimentsPanel._emit_compare ← rows
05277. [x] app\ui\widgets\experiments_panel.py:81 — controle if em ExperimentsPanel._emit_compare
05278. [x] app\ui\widgets\experiments_panel.py:82 — return em ExperimentsPanel._emit_compare
05279. [x] Existência e estrutura do módulo: app\ui\widgets\export_done_dialog.py
05280. [x] app\ui\widgets\export_done_dialog.py:3 — import: __future__
05281. [x] app\ui\widgets\export_done_dialog.py:5 — import: pathlib
05282. [x] app\ui\widgets\export_done_dialog.py:7 — import: PySide6.QtCore
05283. [x] app\ui\widgets\export_done_dialog.py:8 — import: PySide6.QtGui
05284. [x] app\ui\widgets\export_done_dialog.py:9 — import: PySide6.QtWidgets
05285. [x] app\ui\widgets\export_done_dialog.py:18 — definir/revisar ClassDef: ExportDoneDialog
05286. [x] app\ui\widgets\export_done_dialog.py:21 — definir/revisar FunctionDef: ExportDoneDialog.__init__
05287. [x] app\ui\widgets\export_done_dialog.py:21 — revisar facet 'assinatura/args consistentes' em ExportDoneDialog.__init__
05288. [x] app\ui\widgets\export_done_dialog.py:21 — revisar facet 'docstring em português' em ExportDoneDialog.__init__
05289. [x] app\ui\widgets\export_done_dialog.py:21 — revisar facet 'nomenclatura clara (PEP8)' em ExportDoneDialog.__init__
05290. [x] app\ui\widgets\export_done_dialog.py:21 — revisar facet 'type hints presentes' em ExportDoneDialog.__init__
05291. [x] app\ui\widgets\export_done_dialog.py:21 — revisar facet 'tratamento de erros adequado' em ExportDoneDialog.__init__
05292. [x] app\ui\widgets\export_done_dialog.py:21 — revisar facet 'sem comentários inline desnecessários' em ExportDoneDialog.__init__
05293. [x] app\ui\widgets\export_done_dialog.py:21 — revisar facet 'não imprime side-effects na UI/IO' em ExportDoneDialog.__init__
05294. [x] app\ui\widgets\export_done_dialog.py:21 — revisar facet 'thread-safety revisada' em ExportDoneDialog.__init__
05295. [x] app\ui\widgets\export_done_dialog.py:21 — revisar facet 'performance (sem loops O(n^2))' em ExportDoneDialog.__init__
05296. [x] app\ui\widgets\export_done_dialog.py:21 — revisar facet 'coberto por testes' em ExportDoneDialog.__init__
05297. [x] app\ui\widgets\export_done_dialog.py:26 — atribuição: ExportDoneDialog.__init__ ← ?
05298. [x] app\ui\widgets\export_done_dialog.py:27 — atribuição: ExportDoneDialog.__init__ ← ?
05299. [x] app\ui\widgets\export_done_dialog.py:32 — atribuição: ExportDoneDialog.__init__ ← layout
05300. [x] app\ui\widgets\export_done_dialog.py:34 — atribuição: ExportDoneDialog.__init__ ← header
05301. [x] app\ui\widgets\export_done_dialog.py:37 — atribuição: ExportDoneDialog.__init__ ← n_label
05302. [x] app\ui\widgets\export_done_dialog.py:40 — atribuição: ExportDoneDialog.__init__ ← destino
05303. [x] app\ui\widgets\export_done_dialog.py:49 — atribuição: ExportDoneDialog.__init__ ← buttons
05304. [x] app\ui\widgets\export_done_dialog.py:50 — atribuição: ExportDoneDialog.__init__ ← btn_open
05305. [x] app\ui\widgets\export_done_dialog.py:52 — atribuição: ExportDoneDialog.__init__ ← btn_manifest
05306. [x] app\ui\widgets\export_done_dialog.py:53 — atribuição: ExportDoneDialog.__init__ ← btn_close
05307. [x] app\ui\widgets\export_done_dialog.py:64 — definir/revisar FunctionDef: ExportDoneDialog._open_folder
05308. [x] app\ui\widgets\export_done_dialog.py:64 — revisar facet 'assinatura/args consistentes' em ExportDoneDialog._open_folder
05309. [x] app\ui\widgets\export_done_dialog.py:64 — revisar facet 'docstring em português' em ExportDoneDialog._open_folder
05310. [x] app\ui\widgets\export_done_dialog.py:64 — revisar facet 'nomenclatura clara (PEP8)' em ExportDoneDialog._open_folder
05311. [x] app\ui\widgets\export_done_dialog.py:64 — revisar facet 'type hints presentes' em ExportDoneDialog._open_folder
05312. [x] app\ui\widgets\export_done_dialog.py:64 — revisar facet 'tratamento de erros adequado' em ExportDoneDialog._open_folder
05313. [x] app\ui\widgets\export_done_dialog.py:64 — revisar facet 'sem comentários inline desnecessários' em ExportDoneDialog._open_folder
05314. [x] app\ui\widgets\export_done_dialog.py:64 — revisar facet 'não imprime side-effects na UI/IO' em ExportDoneDialog._open_folder
05315. [x] app\ui\widgets\export_done_dialog.py:64 — revisar facet 'thread-safety revisada' em ExportDoneDialog._open_folder
05316. [x] app\ui\widgets\export_done_dialog.py:64 — revisar facet 'performance (sem loops O(n^2))' em ExportDoneDialog._open_folder
05317. [x] app\ui\widgets\export_done_dialog.py:64 — revisar facet 'coberto por testes' em ExportDoneDialog._open_folder
05318. [x] app\ui\widgets\export_done_dialog.py:68 — definir/revisar FunctionDef: ExportDoneDialog._open_manifest
05319. [x] app\ui\widgets\export_done_dialog.py:68 — revisar facet 'assinatura/args consistentes' em ExportDoneDialog._open_manifest
05320. [x] app\ui\widgets\export_done_dialog.py:68 — revisar facet 'docstring em português' em ExportDoneDialog._open_manifest
05321. [x] app\ui\widgets\export_done_dialog.py:68 — revisar facet 'nomenclatura clara (PEP8)' em ExportDoneDialog._open_manifest
05322. [x] app\ui\widgets\export_done_dialog.py:68 — revisar facet 'type hints presentes' em ExportDoneDialog._open_manifest
05323. [x] app\ui\widgets\export_done_dialog.py:68 — revisar facet 'tratamento de erros adequado' em ExportDoneDialog._open_manifest
05324. [x] app\ui\widgets\export_done_dialog.py:68 — revisar facet 'sem comentários inline desnecessários' em ExportDoneDialog._open_manifest
05325. [x] app\ui\widgets\export_done_dialog.py:68 — revisar facet 'não imprime side-effects na UI/IO' em ExportDoneDialog._open_manifest
05326. [x] app\ui\widgets\export_done_dialog.py:68 — revisar facet 'thread-safety revisada' em ExportDoneDialog._open_manifest
05327. [x] app\ui\widgets\export_done_dialog.py:68 — revisar facet 'performance (sem loops O(n^2))' em ExportDoneDialog._open_manifest
05328. [x] app\ui\widgets\export_done_dialog.py:68 — revisar facet 'coberto por testes' em ExportDoneDialog._open_manifest
05329. [x] app\ui\widgets\export_done_dialog.py:69 — controle if em ExportDoneDialog._open_manifest
05330. [x] Existência e estrutura do módulo: app\ui\widgets\logs_panel.py
05331. [x] app\ui\widgets\logs_panel.py:3 — import: __future__
05332. [x] app\ui\widgets\logs_panel.py:5 — import: csv
05333. [x] app\ui\widgets\logs_panel.py:7 — import: PySide6.QtCore
05334. [x] app\ui\widgets\logs_panel.py:8 — import: PySide6.QtGui
05335. [x] app\ui\widgets\logs_panel.py:9 — import: PySide6.QtWidgets
05336. [x] app\ui\widgets\logs_panel.py:23 — definir/revisar ClassDef: LogsPanel
05337. [x] app\ui\widgets\logs_panel.py:24 — atribuição: LogsPanel ← refreshRequested
05338. [x] app\ui\widgets\logs_panel.py:26 — atribuição: LogsPanel ← COLUMNS
05339. [x] app\ui\widgets\logs_panel.py:28 — atribuição: LogsPanel ← LEVEL_COLORS
05340. [x] app\ui\widgets\logs_panel.py:35 — definir/revisar FunctionDef: LogsPanel.__init__
05341. [x] app\ui\widgets\logs_panel.py:35 — revisar facet 'assinatura/args consistentes' em LogsPanel.__init__
05342. [x] app\ui\widgets\logs_panel.py:35 — revisar facet 'docstring em português' em LogsPanel.__init__
05343. [x] app\ui\widgets\logs_panel.py:35 — revisar facet 'nomenclatura clara (PEP8)' em LogsPanel.__init__
05344. [x] app\ui\widgets\logs_panel.py:35 — revisar facet 'type hints presentes' em LogsPanel.__init__
05345. [x] app\ui\widgets\logs_panel.py:35 — revisar facet 'tratamento de erros adequado' em LogsPanel.__init__
05346. [x] app\ui\widgets\logs_panel.py:35 — revisar facet 'sem comentários inline desnecessários' em LogsPanel.__init__
05347. [x] app\ui\widgets\logs_panel.py:35 — revisar facet 'não imprime side-effects na UI/IO' em LogsPanel.__init__
05348. [x] app\ui\widgets\logs_panel.py:35 — revisar facet 'thread-safety revisada' em LogsPanel.__init__
05349. [x] app\ui\widgets\logs_panel.py:35 — revisar facet 'performance (sem loops O(n^2))' em LogsPanel.__init__
05350. [x] app\ui\widgets\logs_panel.py:35 — revisar facet 'coberto por testes' em LogsPanel.__init__
05351. [x] app\ui\widgets\logs_panel.py:37 — atribuição: LogsPanel.__init__ ← ?
05352. [x] app\ui\widgets\logs_panel.py:38 — atribuição: LogsPanel.__init__ ← ?
05353. [x] app\ui\widgets\logs_panel.py:40 — atribuição: LogsPanel.__init__ ← layout
05354. [x] app\ui\widgets\logs_panel.py:42 — atribuição: LogsPanel.__init__ ← bar
05355. [x] app\ui\widgets\logs_panel.py:43 — atribuição: LogsPanel.__init__ ← ?
05356. [x] app\ui\widgets\logs_panel.py:45 — atribuição: LogsPanel.__init__ ← ?
05357. [x] app\ui\widgets\logs_panel.py:47 — atribuição: LogsPanel.__init__ ← ?
05358. [x] app\ui\widgets\logs_panel.py:49 — atribuição: LogsPanel.__init__ ← ?
05359. [x] app\ui\widgets\logs_panel.py:50 — atribuição: LogsPanel.__init__ ← btn_refresh
05360. [x] app\ui\widgets\logs_panel.py:51 — atribuição: LogsPanel.__init__ ← btn_export
05361. [x] app\ui\widgets\logs_panel.py:52 — controle for em LogsPanel.__init__
05362. [x] app\ui\widgets\logs_panel.py:56 — atribuição: LogsPanel.__init__ ← ?
05363. [x] app\ui\widgets\logs_panel.py:67 — atribuição: LogsPanel.__init__ ← ?
05364. [x] app\ui\widgets\logs_panel.py:72 — definir/revisar FunctionDef: LogsPanel._toggle_auto
05365. [x] app\ui\widgets\logs_panel.py:72 — revisar facet 'assinatura/args consistentes' em LogsPanel._toggle_auto
05366. [x] app\ui\widgets\logs_panel.py:72 — revisar facet 'docstring em português' em LogsPanel._toggle_auto
05367. [x] app\ui\widgets\logs_panel.py:72 — revisar facet 'nomenclatura clara (PEP8)' em LogsPanel._toggle_auto
05368. [x] app\ui\widgets\logs_panel.py:72 — revisar facet 'type hints presentes' em LogsPanel._toggle_auto
05369. [x] app\ui\widgets\logs_panel.py:72 — revisar facet 'tratamento de erros adequado' em LogsPanel._toggle_auto
05370. [x] app\ui\widgets\logs_panel.py:72 — revisar facet 'sem comentários inline desnecessários' em LogsPanel._toggle_auto
05371. [x] app\ui\widgets\logs_panel.py:72 — revisar facet 'não imprime side-effects na UI/IO' em LogsPanel._toggle_auto
05372. [x] app\ui\widgets\logs_panel.py:72 — revisar facet 'thread-safety revisada' em LogsPanel._toggle_auto
05373. [x] app\ui\widgets\logs_panel.py:72 — revisar facet 'performance (sem loops O(n^2))' em LogsPanel._toggle_auto
05374. [x] app\ui\widgets\logs_panel.py:72 — revisar facet 'coberto por testes' em LogsPanel._toggle_auto
05375. [x] app\ui\widgets\logs_panel.py:73 — controle if em LogsPanel._toggle_auto
05376. [x] app\ui\widgets\logs_panel.py:78 — definir/revisar FunctionDef: LogsPanel.refresh
05377. [x] app\ui\widgets\logs_panel.py:78 — revisar facet 'assinatura/args consistentes' em LogsPanel.refresh
05378. [x] app\ui\widgets\logs_panel.py:78 — revisar facet 'docstring em português' em LogsPanel.refresh
05379. [x] app\ui\widgets\logs_panel.py:78 — revisar facet 'nomenclatura clara (PEP8)' em LogsPanel.refresh
05380. [x] app\ui\widgets\logs_panel.py:78 — revisar facet 'type hints presentes' em LogsPanel.refresh
05381. [x] app\ui\widgets\logs_panel.py:78 — revisar facet 'tratamento de erros adequado' em LogsPanel.refresh
05382. [x] app\ui\widgets\logs_panel.py:78 — revisar facet 'sem comentários inline desnecessários' em LogsPanel.refresh
05383. [x] app\ui\widgets\logs_panel.py:78 — revisar facet 'não imprime side-effects na UI/IO' em LogsPanel.refresh
05384. [x] app\ui\widgets\logs_panel.py:78 — revisar facet 'thread-safety revisada' em LogsPanel.refresh
05385. [x] app\ui\widgets\logs_panel.py:78 — revisar facet 'performance (sem loops O(n^2))' em LogsPanel.refresh
05386. [x] app\ui\widgets\logs_panel.py:78 — revisar facet 'coberto por testes' em LogsPanel.refresh
05387. [x] app\ui\widgets\logs_panel.py:79 — controle if em LogsPanel.refresh
05388. [x] app\ui\widgets\logs_panel.py:80 — return em LogsPanel.refresh
05389. [x] app\ui\widgets\logs_panel.py:81 — atribuição: LogsPanel.refresh ← ?
05390. [x] app\ui\widgets\logs_panel.py:88 — controle for em LogsPanel.refresh
05391. [x] app\ui\widgets\logs_panel.py:89 — controle for em LogsPanel.refresh
05392. [x] app\ui\widgets\logs_panel.py:90 — atribuição: LogsPanel.refresh ← value
05393. [x] app\ui\widgets\logs_panel.py:91 — atribuição: LogsPanel.refresh ← item
05394. [x] app\ui\widgets\logs_panel.py:92 — controle if em LogsPanel.refresh
05395. [x] app\ui\widgets\logs_panel.py:96 — definir/revisar FunctionDef: LogsPanel.export_csv
05396. [x] app\ui\widgets\logs_panel.py:96 — revisar facet 'assinatura/args consistentes' em LogsPanel.export_csv
05397. [x] app\ui\widgets\logs_panel.py:96 — revisar facet 'docstring em português' em LogsPanel.export_csv
05398. [x] app\ui\widgets\logs_panel.py:96 — revisar facet 'nomenclatura clara (PEP8)' em LogsPanel.export_csv
05399. [x] app\ui\widgets\logs_panel.py:96 — revisar facet 'type hints presentes' em LogsPanel.export_csv
05400. [x] app\ui\widgets\logs_panel.py:96 — revisar facet 'tratamento de erros adequado' em LogsPanel.export_csv
05401. [x] app\ui\widgets\logs_panel.py:96 — revisar facet 'sem comentários inline desnecessários' em LogsPanel.export_csv
05402. [x] app\ui\widgets\logs_panel.py:96 — revisar facet 'não imprime side-effects na UI/IO' em LogsPanel.export_csv
05403. [x] app\ui\widgets\logs_panel.py:96 — revisar facet 'thread-safety revisada' em LogsPanel.export_csv
05404. [x] app\ui\widgets\logs_panel.py:96 — revisar facet 'performance (sem loops O(n^2))' em LogsPanel.export_csv
05405. [x] app\ui\widgets\logs_panel.py:96 — revisar facet 'coberto por testes' em LogsPanel.export_csv
05406. [x] app\ui\widgets\logs_panel.py:97 — atribuição: LogsPanel.export_csv ← ?
05407. [x] app\ui\widgets\logs_panel.py:98 — controle if em LogsPanel.export_csv
05408. [x] app\ui\widgets\logs_panel.py:99 — return em LogsPanel.export_csv
05409. [x] app\ui\widgets\logs_panel.py:100 — controle with em LogsPanel.export_csv
05410. [x] app\ui\widgets\logs_panel.py:101 — atribuição: LogsPanel.export_csv ← writer
05411. [x] app\ui\widgets\logs_panel.py:103 — controle for em LogsPanel.export_csv
05412. [x] Existência e estrutura do módulo: app\ui\widgets\plugins_dialog.py
05413. [x] app\ui\widgets\plugins_dialog.py:3 — import: __future__
05414. [x] app\ui\widgets\plugins_dialog.py:5 — import: PySide6.QtWidgets
05415. [x] app\ui\widgets\plugins_dialog.py:14 — definir/revisar ClassDef: PluginsDialog
05416. [x] app\ui\widgets\plugins_dialog.py:15 — definir/revisar FunctionDef: PluginsDialog.__init__
05417. [x] app\ui\widgets\plugins_dialog.py:15 — revisar facet 'assinatura/args consistentes' em PluginsDialog.__init__
05418. [x] app\ui\widgets\plugins_dialog.py:15 — revisar facet 'docstring em português' em PluginsDialog.__init__
05419. [x] app\ui\widgets\plugins_dialog.py:15 — revisar facet 'nomenclatura clara (PEP8)' em PluginsDialog.__init__
05420. [x] app\ui\widgets\plugins_dialog.py:15 — revisar facet 'type hints presentes' em PluginsDialog.__init__
05421. [x] app\ui\widgets\plugins_dialog.py:15 — revisar facet 'tratamento de erros adequado' em PluginsDialog.__init__
05422. [x] app\ui\widgets\plugins_dialog.py:15 — revisar facet 'sem comentários inline desnecessários' em PluginsDialog.__init__
05423. [x] app\ui\widgets\plugins_dialog.py:15 — revisar facet 'não imprime side-effects na UI/IO' em PluginsDialog.__init__
05424. [x] app\ui\widgets\plugins_dialog.py:15 — revisar facet 'thread-safety revisada' em PluginsDialog.__init__
05425. [x] app\ui\widgets\plugins_dialog.py:15 — revisar facet 'performance (sem loops O(n^2))' em PluginsDialog.__init__
05426. [x] app\ui\widgets\plugins_dialog.py:15 — revisar facet 'coberto por testes' em PluginsDialog.__init__
05427. [x] app\ui\widgets\plugins_dialog.py:20 — atribuição: PluginsDialog.__init__ ← layout
05428. [x] app\ui\widgets\plugins_dialog.py:21 — atribuição: PluginsDialog.__init__ ← ?
05429. [x] app\ui\widgets\plugins_dialog.py:24 — controle for em PluginsDialog.__init__
05430. [x] app\ui\widgets\plugins_dialog.py:25 — atribuição: PluginsDialog.__init__ ← provider
05431. [x] app\ui\widgets\plugins_dialog.py:26 — atribuição: PluginsDialog.__init__ ← item
05432. [x] app\ui\widgets\plugins_dialog.py:29 — atribuição: PluginsDialog.__init__ ← ?
05433. [x] app\ui\widgets\plugins_dialog.py:32 — controle if em PluginsDialog.__init__
05434. [x] app\ui\widgets\plugins_dialog.py:33 — controle for em PluginsDialog.__init__
05435. [x] app\ui\widgets\plugins_dialog.py:35 — controle for em PluginsDialog.__init__
05436. [x] Existência e estrutura do módulo: app\ui\widgets\preview_panel.py
05437. [x] app\ui\widgets\preview_panel.py:3 — import: __future__
05438. [x] app\ui\widgets\preview_panel.py:5 — import: PySide6.QtCore
05439. [x] app\ui\widgets\preview_panel.py:6 — import: PySide6.QtWidgets
05440. [x] app\ui\widgets\preview_panel.py:16 — definir/revisar ClassDef: PreviewPanel
05441. [x] app\ui\widgets\preview_panel.py:17 — atribuição: PreviewPanel ← previewRequested
05442. [x] app\ui\widgets\preview_panel.py:19 — definir/revisar FunctionDef: PreviewPanel.__init__
05443. [x] app\ui\widgets\preview_panel.py:19 — revisar facet 'assinatura/args consistentes' em PreviewPanel.__init__
05444. [x] app\ui\widgets\preview_panel.py:19 — revisar facet 'docstring em português' em PreviewPanel.__init__
05445. [x] app\ui\widgets\preview_panel.py:19 — revisar facet 'nomenclatura clara (PEP8)' em PreviewPanel.__init__
05446. [x] app\ui\widgets\preview_panel.py:19 — revisar facet 'type hints presentes' em PreviewPanel.__init__
05447. [x] app\ui\widgets\preview_panel.py:19 — revisar facet 'tratamento de erros adequado' em PreviewPanel.__init__
05448. [x] app\ui\widgets\preview_panel.py:19 — revisar facet 'sem comentários inline desnecessários' em PreviewPanel.__init__
05449. [x] app\ui\widgets\preview_panel.py:19 — revisar facet 'não imprime side-effects na UI/IO' em PreviewPanel.__init__
05450. [x] app\ui\widgets\preview_panel.py:19 — revisar facet 'thread-safety revisada' em PreviewPanel.__init__
05451. [x] app\ui\widgets\preview_panel.py:19 — revisar facet 'performance (sem loops O(n^2))' em PreviewPanel.__init__
05452. [x] app\ui\widgets\preview_panel.py:19 — revisar facet 'coberto por testes' em PreviewPanel.__init__
05453. [x] app\ui\widgets\preview_panel.py:21 — atribuição: PreviewPanel.__init__ ← layout
05454. [x] app\ui\widgets\preview_panel.py:23 — atribuição: PreviewPanel.__init__ ← bar
05455. [x] app\ui\widgets\preview_panel.py:24 — atribuição: PreviewPanel.__init__ ← ?
05456. [x] app\ui\widgets\preview_panel.py:27 — atribuição: PreviewPanel.__init__ ← ?
05457. [x] app\ui\widgets\preview_panel.py:33 — atribuição: PreviewPanel.__init__ ← ?
05458. [x] app\ui\widgets\preview_panel.py:42 — definir/revisar FunctionDef: PreviewPanel.show_text
05459. [x] app\ui\widgets\preview_panel.py:42 — revisar facet 'assinatura/args consistentes' em PreviewPanel.show_text
05460. [x] app\ui\widgets\preview_panel.py:42 — revisar facet 'docstring em português' em PreviewPanel.show_text
05461. [x] app\ui\widgets\preview_panel.py:42 — revisar facet 'nomenclatura clara (PEP8)' em PreviewPanel.show_text
05462. [x] app\ui\widgets\preview_panel.py:42 — revisar facet 'type hints presentes' em PreviewPanel.show_text
05463. [x] app\ui\widgets\preview_panel.py:42 — revisar facet 'tratamento de erros adequado' em PreviewPanel.show_text
05464. [x] app\ui\widgets\preview_panel.py:42 — revisar facet 'sem comentários inline desnecessários' em PreviewPanel.show_text
05465. [x] app\ui\widgets\preview_panel.py:42 — revisar facet 'não imprime side-effects na UI/IO' em PreviewPanel.show_text
05466. [x] app\ui\widgets\preview_panel.py:42 — revisar facet 'thread-safety revisada' em PreviewPanel.show_text
05467. [x] app\ui\widgets\preview_panel.py:42 — revisar facet 'performance (sem loops O(n^2))' em PreviewPanel.show_text
05468. [x] app\ui\widgets\preview_panel.py:42 — revisar facet 'coberto por testes' em PreviewPanel.show_text
05469. [x] Existência e estrutura do módulo: app\ui\widgets\statistics_dialog.py
05470. [x] app\ui\widgets\statistics_dialog.py:3 — import: __future__
05471. [x] app\ui\widgets\statistics_dialog.py:5 — import: PySide6.QtWidgets
05472. [x] app\ui\widgets\statistics_dialog.py:14 — import: app.services.statistics_service
05473. [x] app\ui\widgets\statistics_dialog.py:17 — definir/revisar ClassDef: StatisticsDialog
05474. [x] app\ui\widgets\statistics_dialog.py:18 — atribuição: StatisticsDialog ← STATS_COLUMNS
05475. [x] app\ui\widgets\statistics_dialog.py:20 — definir/revisar FunctionDef: StatisticsDialog.__init__
05476. [x] app\ui\widgets\statistics_dialog.py:20 — revisar facet 'assinatura/args consistentes' em StatisticsDialog.__init__
05477. [x] app\ui\widgets\statistics_dialog.py:20 — revisar facet 'docstring em português' em StatisticsDialog.__init__
05478. [x] app\ui\widgets\statistics_dialog.py:20 — revisar facet 'nomenclatura clara (PEP8)' em StatisticsDialog.__init__
05479. [x] app\ui\widgets\statistics_dialog.py:20 — revisar facet 'type hints presentes' em StatisticsDialog.__init__
05480. [x] app\ui\widgets\statistics_dialog.py:20 — revisar facet 'tratamento de erros adequado' em StatisticsDialog.__init__
05481. [x] app\ui\widgets\statistics_dialog.py:20 — revisar facet 'sem comentários inline desnecessários' em StatisticsDialog.__init__
05482. [x] app\ui\widgets\statistics_dialog.py:20 — revisar facet 'não imprime side-effects na UI/IO' em StatisticsDialog.__init__
05483. [x] app\ui\widgets\statistics_dialog.py:20 — revisar facet 'thread-safety revisada' em StatisticsDialog.__init__
05484. [x] app\ui\widgets\statistics_dialog.py:20 — revisar facet 'performance (sem loops O(n^2))' em StatisticsDialog.__init__
05485. [x] app\ui\widgets\statistics_dialog.py:20 — revisar facet 'coberto por testes' em StatisticsDialog.__init__
05486. [x] app\ui\widgets\statistics_dialog.py:23 — atribuição: StatisticsDialog.__init__ ← ?
05487. [x] app\ui\widgets\statistics_dialog.py:24 — atribuição: StatisticsDialog.__init__ ← ?
05488. [x] app\ui\widgets\statistics_dialog.py:26 — atribuição: StatisticsDialog.__init__ ← layout
05489. [x] app\ui\widgets\statistics_dialog.py:27 — atribuição: StatisticsDialog.__init__ ← ?
05490. [x] app\ui\widgets\statistics_dialog.py:32 — atribuição: StatisticsDialog.__init__ ← btn
05491. [x] app\ui\widgets\statistics_dialog.py:36 — atribuição: StatisticsDialog.__init__ ← ?
05492. [x] app\ui\widgets\statistics_dialog.py:41 — definir/revisar FunctionDef: StatisticsDialog.refresh
05493. [x] app\ui\widgets\statistics_dialog.py:41 — revisar facet 'assinatura/args consistentes' em StatisticsDialog.refresh
05494. [x] app\ui\widgets\statistics_dialog.py:41 — revisar facet 'docstring em português' em StatisticsDialog.refresh
05495. [x] app\ui\widgets\statistics_dialog.py:41 — revisar facet 'nomenclatura clara (PEP8)' em StatisticsDialog.refresh
05496. [x] app\ui\widgets\statistics_dialog.py:41 — revisar facet 'type hints presentes' em StatisticsDialog.refresh
05497. [x] app\ui\widgets\statistics_dialog.py:41 — revisar facet 'tratamento de erros adequado' em StatisticsDialog.refresh
05498. [x] app\ui\widgets\statistics_dialog.py:41 — revisar facet 'sem comentários inline desnecessários' em StatisticsDialog.refresh
05499. [x] app\ui\widgets\statistics_dialog.py:41 — revisar facet 'não imprime side-effects na UI/IO' em StatisticsDialog.refresh
05500. [x] app\ui\widgets\statistics_dialog.py:41 — revisar facet 'thread-safety revisada' em StatisticsDialog.refresh
05501. [x] app\ui\widgets\statistics_dialog.py:41 — revisar facet 'performance (sem loops O(n^2))' em StatisticsDialog.refresh
05502. [x] app\ui\widgets\statistics_dialog.py:41 — revisar facet 'coberto por testes' em StatisticsDialog.refresh
05503. [x] app\ui\widgets\statistics_dialog.py:42 — atribuição: StatisticsDialog.refresh ← var_id
05504. [x] app\ui\widgets\statistics_dialog.py:43 — try em StatisticsDialog.refresh
05505. [x] app\ui\widgets\statistics_dialog.py:44 — atribuição: StatisticsDialog.refresh ← values
05506. [x] app\ui\widgets\statistics_dialog.py:46 — atribuição: StatisticsDialog.refresh ← values
05507. [x] app\ui\widgets\statistics_dialog.py:47 — atribuição: StatisticsDialog.refresh ← stats
05508. [x] app\ui\widgets\statistics_dialog.py:49 — atribuição: StatisticsDialog.refresh ← rows
05509. [x] app\ui\widgets\statistics_dialog.py:61 — controle for em StatisticsDialog.refresh
05510. [x] Existência e estrutura do módulo: app\ui\widgets\tasks_panel.py
05511. [x] app\ui\widgets\tasks_panel.py:3 — import: __future__
05512. [x] app\ui\widgets\tasks_panel.py:5 — import: PySide6.QtCore
05513. [x] app\ui\widgets\tasks_panel.py:6 — import: PySide6.QtWidgets
05514. [x] app\ui\widgets\tasks_panel.py:16 — import: app.domain.tasks
05515. [x] app\ui\widgets\tasks_panel.py:19 — definir/revisar ClassDef: TasksPanel
05516. [x] app\ui\widgets\tasks_panel.py:20 — atribuição: TasksPanel ← pauseRequested
05517. [x] app\ui\widgets\tasks_panel.py:21 — atribuição: TasksPanel ← resumeRequested
05518. [x] app\ui\widgets\tasks_panel.py:22 — atribuição: TasksPanel ← cancelRequested
05519. [x] app\ui\widgets\tasks_panel.py:24 — definir/revisar FunctionDef: TasksPanel.__init__
05520. [x] app\ui\widgets\tasks_panel.py:24 — revisar facet 'assinatura/args consistentes' em TasksPanel.__init__
05521. [x] app\ui\widgets\tasks_panel.py:24 — revisar facet 'docstring em português' em TasksPanel.__init__
05522. [x] app\ui\widgets\tasks_panel.py:24 — revisar facet 'nomenclatura clara (PEP8)' em TasksPanel.__init__
05523. [x] app\ui\widgets\tasks_panel.py:24 — revisar facet 'type hints presentes' em TasksPanel.__init__
05524. [x] app\ui\widgets\tasks_panel.py:24 — revisar facet 'tratamento de erros adequado' em TasksPanel.__init__
05525. [x] app\ui\widgets\tasks_panel.py:24 — revisar facet 'sem comentários inline desnecessários' em TasksPanel.__init__
05526. [x] app\ui\widgets\tasks_panel.py:24 — revisar facet 'não imprime side-effects na UI/IO' em TasksPanel.__init__
05527. [x] app\ui\widgets\tasks_panel.py:24 — revisar facet 'thread-safety revisada' em TasksPanel.__init__
05528. [x] app\ui\widgets\tasks_panel.py:24 — revisar facet 'performance (sem loops O(n^2))' em TasksPanel.__init__
05529. [x] app\ui\widgets\tasks_panel.py:24 — revisar facet 'coberto por testes' em TasksPanel.__init__
05530. [x] app\ui\widgets\tasks_panel.py:26 — atribuição: TasksPanel.__init__ ← ?
05531. [x] app\ui\widgets\tasks_panel.py:28 — atribuição: TasksPanel.__init__ ← layout
05532. [x] app\ui\widgets\tasks_panel.py:30 — atribuição: TasksPanel.__init__ ← ?
05533. [x] app\ui\widgets\tasks_panel.py:36 — atribuição: TasksPanel.__init__ ← bar
05534. [x] app\ui\widgets\tasks_panel.py:37 — atribuição: TasksPanel.__init__ ← ?
05535. [x] app\ui\widgets\tasks_panel.py:38 — atribuição: TasksPanel.__init__ ← ?
05536. [x] app\ui\widgets\tasks_panel.py:39 — atribuição: TasksPanel.__init__ ← ?
05537. [x] app\ui\widgets\tasks_panel.py:51 — definir/revisar FunctionDef: TasksPanel._emit
05538. [x] app\ui\widgets\tasks_panel.py:51 — revisar facet 'assinatura/args consistentes' em TasksPanel._emit
05539. [x] app\ui\widgets\tasks_panel.py:51 — revisar facet 'docstring em português' em TasksPanel._emit
05540. [x] app\ui\widgets\tasks_panel.py:51 — revisar facet 'nomenclatura clara (PEP8)' em TasksPanel._emit
05541. [x] app\ui\widgets\tasks_panel.py:51 — revisar facet 'type hints presentes' em TasksPanel._emit
05542. [x] app\ui\widgets\tasks_panel.py:51 — revisar facet 'tratamento de erros adequado' em TasksPanel._emit
05543. [x] app\ui\widgets\tasks_panel.py:51 — revisar facet 'sem comentários inline desnecessários' em TasksPanel._emit
05544. [x] app\ui\widgets\tasks_panel.py:51 — revisar facet 'não imprime side-effects na UI/IO' em TasksPanel._emit
05545. [x] app\ui\widgets\tasks_panel.py:51 — revisar facet 'thread-safety revisada' em TasksPanel._emit
05546. [x] app\ui\widgets\tasks_panel.py:51 — revisar facet 'performance (sem loops O(n^2))' em TasksPanel._emit
05547. [x] app\ui\widgets\tasks_panel.py:51 — revisar facet 'coberto por testes' em TasksPanel._emit
05548. [x] app\ui\widgets\tasks_panel.py:52 — definir/revisar FunctionDef: TasksPanel._emit.inner
05549. [x] app\ui\widgets\tasks_panel.py:52 — revisar facet 'assinatura/args consistentes' em TasksPanel._emit.inner
05550. [x] app\ui\widgets\tasks_panel.py:52 — revisar facet 'docstring em português' em TasksPanel._emit.inner
05551. [x] app\ui\widgets\tasks_panel.py:52 — revisar facet 'nomenclatura clara (PEP8)' em TasksPanel._emit.inner
05552. [x] app\ui\widgets\tasks_panel.py:52 — revisar facet 'type hints presentes' em TasksPanel._emit.inner
05553. [x] app\ui\widgets\tasks_panel.py:52 — revisar facet 'tratamento de erros adequado' em TasksPanel._emit.inner
05554. [x] app\ui\widgets\tasks_panel.py:52 — revisar facet 'sem comentários inline desnecessários' em TasksPanel._emit.inner
05555. [x] app\ui\widgets\tasks_panel.py:52 — revisar facet 'não imprime side-effects na UI/IO' em TasksPanel._emit.inner
05556. [x] app\ui\widgets\tasks_panel.py:52 — revisar facet 'thread-safety revisada' em TasksPanel._emit.inner
05557. [x] app\ui\widgets\tasks_panel.py:52 — revisar facet 'performance (sem loops O(n^2))' em TasksPanel._emit.inner
05558. [x] app\ui\widgets\tasks_panel.py:52 — revisar facet 'coberto por testes' em TasksPanel._emit.inner
05559. [x] app\ui\widgets\tasks_panel.py:53 — atribuição: TasksPanel._emit.inner ← row
05560. [x] app\ui\widgets\tasks_panel.py:54 — controle if em TasksPanel._emit.inner
05561. [x] app\ui\widgets\tasks_panel.py:55 — return em TasksPanel._emit.inner
05562. [x] app\ui\widgets\tasks_panel.py:56 — atribuição: TasksPanel._emit.inner ← task_id
05563. [x] app\ui\widgets\tasks_panel.py:58 — return em TasksPanel._emit
05564. [x] app\ui\widgets\tasks_panel.py:60 — definir/revisar FunctionDef: TasksPanel.add_task_row
05565. [x] app\ui\widgets\tasks_panel.py:60 — revisar facet 'assinatura/args consistentes' em TasksPanel.add_task_row
05566. [x] app\ui\widgets\tasks_panel.py:60 — revisar facet 'docstring em português' em TasksPanel.add_task_row
05567. [x] app\ui\widgets\tasks_panel.py:60 — revisar facet 'nomenclatura clara (PEP8)' em TasksPanel.add_task_row
05568. [x] app\ui\widgets\tasks_panel.py:60 — revisar facet 'type hints presentes' em TasksPanel.add_task_row
05569. [x] app\ui\widgets\tasks_panel.py:60 — revisar facet 'tratamento de erros adequado' em TasksPanel.add_task_row
05570. [x] app\ui\widgets\tasks_panel.py:60 — revisar facet 'sem comentários inline desnecessários' em TasksPanel.add_task_row
05571. [x] app\ui\widgets\tasks_panel.py:60 — revisar facet 'não imprime side-effects na UI/IO' em TasksPanel.add_task_row
05572. [x] app\ui\widgets\tasks_panel.py:60 — revisar facet 'thread-safety revisada' em TasksPanel.add_task_row
05573. [x] app\ui\widgets\tasks_panel.py:60 — revisar facet 'performance (sem loops O(n^2))' em TasksPanel.add_task_row
05574. [x] app\ui\widgets\tasks_panel.py:60 — revisar facet 'coberto por testes' em TasksPanel.add_task_row
05575. [x] app\ui\widgets\tasks_panel.py:63 — definir/revisar FunctionDef: TasksPanel.update_task_progress
05576. [x] app\ui\widgets\tasks_panel.py:63 — revisar facet 'assinatura/args consistentes' em TasksPanel.update_task_progress
05577. [x] app\ui\widgets\tasks_panel.py:63 — revisar facet 'docstring em português' em TasksPanel.update_task_progress
05578. [x] app\ui\widgets\tasks_panel.py:63 — revisar facet 'nomenclatura clara (PEP8)' em TasksPanel.update_task_progress
05579. [x] app\ui\widgets\tasks_panel.py:63 — revisar facet 'type hints presentes' em TasksPanel.update_task_progress
05580. [x] app\ui\widgets\tasks_panel.py:63 — revisar facet 'tratamento de erros adequado' em TasksPanel.update_task_progress
05581. [x] app\ui\widgets\tasks_panel.py:63 — revisar facet 'sem comentários inline desnecessários' em TasksPanel.update_task_progress
05582. [x] app\ui\widgets\tasks_panel.py:63 — revisar facet 'não imprime side-effects na UI/IO' em TasksPanel.update_task_progress
05583. [x] app\ui\widgets\tasks_panel.py:63 — revisar facet 'thread-safety revisada' em TasksPanel.update_task_progress
05584. [x] app\ui\widgets\tasks_panel.py:63 — revisar facet 'performance (sem loops O(n^2))' em TasksPanel.update_task_progress
05585. [x] app\ui\widgets\tasks_panel.py:63 — revisar facet 'coberto por testes' em TasksPanel.update_task_progress
05586. [x] app\ui\widgets\tasks_panel.py:66 — definir/revisar FunctionDef: TasksPanel.refresh
05587. [x] app\ui\widgets\tasks_panel.py:66 — revisar facet 'assinatura/args consistentes' em TasksPanel.refresh
05588. [x] app\ui\widgets\tasks_panel.py:66 — revisar facet 'docstring em português' em TasksPanel.refresh
05589. [x] app\ui\widgets\tasks_panel.py:66 — revisar facet 'nomenclatura clara (PEP8)' em TasksPanel.refresh
05590. [x] app\ui\widgets\tasks_panel.py:66 — revisar facet 'type hints presentes' em TasksPanel.refresh
05591. [x] app\ui\widgets\tasks_panel.py:66 — revisar facet 'tratamento de erros adequado' em TasksPanel.refresh
05592. [x] app\ui\widgets\tasks_panel.py:66 — revisar facet 'sem comentários inline desnecessários' em TasksPanel.refresh
05593. [x] app\ui\widgets\tasks_panel.py:66 — revisar facet 'não imprime side-effects na UI/IO' em TasksPanel.refresh
05594. [x] app\ui\widgets\tasks_panel.py:66 — revisar facet 'thread-safety revisada' em TasksPanel.refresh
05595. [x] app\ui\widgets\tasks_panel.py:66 — revisar facet 'performance (sem loops O(n^2))' em TasksPanel.refresh
05596. [x] app\ui\widgets\tasks_panel.py:66 — revisar facet 'coberto por testes' em TasksPanel.refresh
05597. [x] app\ui\widgets\tasks_panel.py:67 — controle if em TasksPanel.refresh
05598. [x] app\ui\widgets\tasks_panel.py:68 — return em TasksPanel.refresh
05599. [x] app\ui\widgets\tasks_panel.py:69 — atribuição: TasksPanel.refresh ← tasks
05600. [x] app\ui\widgets\tasks_panel.py:71 — controle for em TasksPanel.refresh
05601. [x] app\ui\widgets\tasks_panel.py:72 — atribuição: TasksPanel.refresh ← values
05602. [x] app\ui\widgets\tasks_panel.py:79 — controle for em TasksPanel.refresh
05603. [x] app\ui\widgets\tasks_panel.py:80 — atribuição: TasksPanel.refresh ← item
05604. [x] app\ui\widgets\tasks_panel.py:81 — controle if em TasksPanel.refresh
05605. [x] Existência e estrutura do módulo: app\ui\widgets\template_version_dialog.py
05606. [x] app\ui\widgets\template_version_dialog.py:3 — import: __future__
05607. [x] app\ui\widgets\template_version_dialog.py:5 — import: PySide6.QtCore
05608. [x] app\ui\widgets\template_version_dialog.py:6 — import: PySide6.QtWidgets
05609. [x] app\ui\widgets\template_version_dialog.py:16 — import: app.services.template_service
05610. [x] app\ui\widgets\template_version_dialog.py:19 — definir/revisar ClassDef: TemplateVersionDialog
05611. [x] app\ui\widgets\template_version_dialog.py:20 — atribuição: TemplateVersionDialog ← restoreRequested
05612. [x] app\ui\widgets\template_version_dialog.py:22 — definir/revisar FunctionDef: TemplateVersionDialog.__init__
05613. [x] app\ui\widgets\template_version_dialog.py:22 — revisar facet 'assinatura/args consistentes' em TemplateVersionDialog.__init__
05614. [x] app\ui\widgets\template_version_dialog.py:22 — revisar facet 'docstring em português' em TemplateVersionDialog.__init__
05615. [x] app\ui\widgets\template_version_dialog.py:22 — revisar facet 'nomenclatura clara (PEP8)' em TemplateVersionDialog.__init__
05616. [x] app\ui\widgets\template_version_dialog.py:22 — revisar facet 'type hints presentes' em TemplateVersionDialog.__init__
05617. [x] app\ui\widgets\template_version_dialog.py:22 — revisar facet 'tratamento de erros adequado' em TemplateVersionDialog.__init__
05618. [x] app\ui\widgets\template_version_dialog.py:22 — revisar facet 'sem comentários inline desnecessários' em TemplateVersionDialog.__init__
05619. [x] app\ui\widgets\template_version_dialog.py:22 — revisar facet 'não imprime side-effects na UI/IO' em TemplateVersionDialog.__init__
05620. [x] app\ui\widgets\template_version_dialog.py:22 — revisar facet 'thread-safety revisada' em TemplateVersionDialog.__init__
05621. [x] app\ui\widgets\template_version_dialog.py:22 — revisar facet 'performance (sem loops O(n^2))' em TemplateVersionDialog.__init__
05622. [x] app\ui\widgets\template_version_dialog.py:22 — revisar facet 'coberto por testes' em TemplateVersionDialog.__init__
05623. [x] app\ui\widgets\template_version_dialog.py:25 — atribuição: TemplateVersionDialog.__init__ ← ?
05624. [x] app\ui\widgets\template_version_dialog.py:26 — atribuição: TemplateVersionDialog.__init__ ← ?
05625. [x] app\ui\widgets\template_version_dialog.py:28 — atribuição: TemplateVersionDialog.__init__ ← layout
05626. [x] app\ui\widgets\template_version_dialog.py:29 — atribuição: TemplateVersionDialog.__init__ ← ?
05627. [x] app\ui\widgets\template_version_dialog.py:33 — atribuição: TemplateVersionDialog.__init__ ← ?
05628. [x] app\ui\widgets\template_version_dialog.py:37 — atribuição: TemplateVersionDialog.__init__ ← bar
05629. [x] app\ui\widgets\template_version_dialog.py:38 — atribuição: TemplateVersionDialog.__init__ ← btn_diff
05630. [x] app\ui\widgets\template_version_dialog.py:39 — atribuição: TemplateVersionDialog.__init__ ← btn_restore
05631. [x] app\ui\widgets\template_version_dialog.py:49 — definir/revisar FunctionDef: TemplateVersionDialog.refresh_list
05632. [x] app\ui\widgets\template_version_dialog.py:49 — revisar facet 'assinatura/args consistentes' em TemplateVersionDialog.refresh_list
05633. [x] app\ui\widgets\template_version_dialog.py:49 — revisar facet 'docstring em português' em TemplateVersionDialog.refresh_list
05634. [x] app\ui\widgets\template_version_dialog.py:49 — revisar facet 'nomenclatura clara (PEP8)' em TemplateVersionDialog.refresh_list
05635. [x] app\ui\widgets\template_version_dialog.py:49 — revisar facet 'type hints presentes' em TemplateVersionDialog.refresh_list
05636. [x] app\ui\widgets\template_version_dialog.py:49 — revisar facet 'tratamento de erros adequado' em TemplateVersionDialog.refresh_list
05637. [x] app\ui\widgets\template_version_dialog.py:49 — revisar facet 'sem comentários inline desnecessários' em TemplateVersionDialog.refresh_list
05638. [x] app\ui\widgets\template_version_dialog.py:49 — revisar facet 'não imprime side-effects na UI/IO' em TemplateVersionDialog.refresh_list
05639. [x] app\ui\widgets\template_version_dialog.py:49 — revisar facet 'thread-safety revisada' em TemplateVersionDialog.refresh_list
05640. [x] app\ui\widgets\template_version_dialog.py:49 — revisar facet 'performance (sem loops O(n^2))' em TemplateVersionDialog.refresh_list
05641. [x] app\ui\widgets\template_version_dialog.py:49 — revisar facet 'coberto por testes' em TemplateVersionDialog.refresh_list
05642. [x] app\ui\widgets\template_version_dialog.py:51 — atribuição: TemplateVersionDialog.refresh_list ← versions
05643. [x] app\ui\widgets\template_version_dialog.py:52 — controle for em TemplateVersionDialog.refresh_list
05644. [x] app\ui\widgets\template_version_dialog.py:53 — atribuição: TemplateVersionDialog.refresh_list ← label
05645. [x] app\ui\widgets\template_version_dialog.py:57 — atribuição: TemplateVersionDialog.refresh_list ← item
05646. [x] app\ui\widgets\template_version_dialog.py:62 — definir/revisar FunctionDef: TemplateVersionDialog._selected_versions
05647. [x] app\ui\widgets\template_version_dialog.py:62 — revisar facet 'assinatura/args consistentes' em TemplateVersionDialog._selected_versions
05648. [x] app\ui\widgets\template_version_dialog.py:62 — revisar facet 'docstring em português' em TemplateVersionDialog._selected_versions
05649. [x] app\ui\widgets\template_version_dialog.py:62 — revisar facet 'nomenclatura clara (PEP8)' em TemplateVersionDialog._selected_versions
05650. [x] app\ui\widgets\template_version_dialog.py:62 — revisar facet 'type hints presentes' em TemplateVersionDialog._selected_versions
05651. [x] app\ui\widgets\template_version_dialog.py:62 — revisar facet 'tratamento de erros adequado' em TemplateVersionDialog._selected_versions
05652. [x] app\ui\widgets\template_version_dialog.py:62 — revisar facet 'sem comentários inline desnecessários' em TemplateVersionDialog._selected_versions
05653. [x] app\ui\widgets\template_version_dialog.py:62 — revisar facet 'não imprime side-effects na UI/IO' em TemplateVersionDialog._selected_versions
05654. [x] app\ui\widgets\template_version_dialog.py:62 — revisar facet 'thread-safety revisada' em TemplateVersionDialog._selected_versions
05655. [x] app\ui\widgets\template_version_dialog.py:62 — revisar facet 'performance (sem loops O(n^2))' em TemplateVersionDialog._selected_versions
05656. [x] app\ui\widgets\template_version_dialog.py:62 — revisar facet 'coberto por testes' em TemplateVersionDialog._selected_versions
05657. [x] app\ui\widgets\template_version_dialog.py:63 — return em TemplateVersionDialog._selected_versions
05658. [x] app\ui\widgets\template_version_dialog.py:68 — definir/revisar FunctionDef: TemplateVersionDialog._show_diff
05659. [x] app\ui\widgets\template_version_dialog.py:68 — revisar facet 'assinatura/args consistentes' em TemplateVersionDialog._show_diff
05660. [x] app\ui\widgets\template_version_dialog.py:68 — revisar facet 'docstring em português' em TemplateVersionDialog._show_diff
05661. [x] app\ui\widgets\template_version_dialog.py:68 — revisar facet 'nomenclatura clara (PEP8)' em TemplateVersionDialog._show_diff
05662. [x] app\ui\widgets\template_version_dialog.py:68 — revisar facet 'type hints presentes' em TemplateVersionDialog._show_diff
05663. [x] app\ui\widgets\template_version_dialog.py:68 — revisar facet 'tratamento de erros adequado' em TemplateVersionDialog._show_diff
05664. [x] app\ui\widgets\template_version_dialog.py:68 — revisar facet 'sem comentários inline desnecessários' em TemplateVersionDialog._show_diff
05665. [x] app\ui\widgets\template_version_dialog.py:68 — revisar facet 'não imprime side-effects na UI/IO' em TemplateVersionDialog._show_diff
05666. [x] app\ui\widgets\template_version_dialog.py:68 — revisar facet 'thread-safety revisada' em TemplateVersionDialog._show_diff
05667. [x] app\ui\widgets\template_version_dialog.py:68 — revisar facet 'performance (sem loops O(n^2))' em TemplateVersionDialog._show_diff
05668. [x] app\ui\widgets\template_version_dialog.py:68 — revisar facet 'coberto por testes' em TemplateVersionDialog._show_diff
05669. [x] app\ui\widgets\template_version_dialog.py:69 — atribuição: TemplateVersionDialog._show_diff ← selected
05670. [x] app\ui\widgets\template_version_dialog.py:70 — controle if em TemplateVersionDialog._show_diff
05671. [x] app\ui\widgets\template_version_dialog.py:72 — return em TemplateVersionDialog._show_diff
05672. [x] app\ui\widgets\template_version_dialog.py:73 — atribuição: TemplateVersionDialog._show_diff ← v1
05673. [x] app\ui\widgets\template_version_dialog.py:74 — atribuição: TemplateVersionDialog._show_diff ← v2
05674. [x] app\ui\widgets\template_version_dialog.py:77 — definir/revisar FunctionDef: TemplateVersionDialog._restore
05675. [x] app\ui\widgets\template_version_dialog.py:77 — revisar facet 'assinatura/args consistentes' em TemplateVersionDialog._restore
05676. [x] app\ui\widgets\template_version_dialog.py:77 — revisar facet 'docstring em português' em TemplateVersionDialog._restore
05677. [x] app\ui\widgets\template_version_dialog.py:77 — revisar facet 'nomenclatura clara (PEP8)' em TemplateVersionDialog._restore
05678. [x] app\ui\widgets\template_version_dialog.py:77 — revisar facet 'type hints presentes' em TemplateVersionDialog._restore
05679. [x] app\ui\widgets\template_version_dialog.py:77 — revisar facet 'tratamento de erros adequado' em TemplateVersionDialog._restore
05680. [x] app\ui\widgets\template_version_dialog.py:77 — revisar facet 'sem comentários inline desnecessários' em TemplateVersionDialog._restore
05681. [x] app\ui\widgets\template_version_dialog.py:77 — revisar facet 'não imprime side-effects na UI/IO' em TemplateVersionDialog._restore
05682. [x] app\ui\widgets\template_version_dialog.py:77 — revisar facet 'thread-safety revisada' em TemplateVersionDialog._restore
05683. [x] app\ui\widgets\template_version_dialog.py:77 — revisar facet 'performance (sem loops O(n^2))' em TemplateVersionDialog._restore
05684. [x] app\ui\widgets\template_version_dialog.py:77 — revisar facet 'coberto por testes' em TemplateVersionDialog._restore
05685. [x] app\ui\widgets\template_version_dialog.py:78 — atribuição: TemplateVersionDialog._restore ← selected
05686. [x] app\ui\widgets\template_version_dialog.py:79 — controle if em TemplateVersionDialog._restore
05687. [x] app\ui\widgets\template_version_dialog.py:80 — return em TemplateVersionDialog._restore
05688. [x] app\ui\widgets\template_version_dialog.py:81 — atribuição: TemplateVersionDialog._restore ← item
05689. [x] app\ui\widgets\template_version_dialog.py:82 — atribuição: TemplateVersionDialog._restore ← version_id
05690. [x] Existência e estrutura do módulo: app\ui\widgets\variables_panel.py
05691. [x] app\ui\widgets\variables_panel.py:3 — import: __future__
05692. [x] app\ui\widgets\variables_panel.py:5 — import: typing
05693. [x] app\ui\widgets\variables_panel.py:7 — import: PySide6.QtCore
05694. [x] app\ui\widgets\variables_panel.py:8 — import: PySide6.QtGui
05695. [x] app\ui\widgets\variables_panel.py:9 — import: PySide6.QtWidgets
05696. [x] app\ui\widgets\variables_panel.py:19 — import: app.core.parsing
05697. [x] app\ui\widgets\variables_panel.py:20 — import: app.infrastructure.distribution_registry
05698. [x] app\ui\widgets\variables_panel.py:21 — import: app.ui.widgets.distribution_dialog
05699. [x] app\ui\widgets\variables_panel.py:24 — definir/revisar ClassDef: VariablesPanel
05700. [x] app\ui\widgets\variables_panel.py:27 — atribuição: VariablesPanel ← variables_changed
05701. [x] app\ui\widgets\variables_panel.py:28 — atribuição: VariablesPanel ← sampleRequested
05702. [x] app\ui\widgets\variables_panel.py:30 — definir/revisar FunctionDef: VariablesPanel.__init__
05703. [x] app\ui\widgets\variables_panel.py:30 — revisar facet 'assinatura/args consistentes' em VariablesPanel.__init__
05704. [x] app\ui\widgets\variables_panel.py:30 — revisar facet 'docstring em português' em VariablesPanel.__init__
05705. [x] app\ui\widgets\variables_panel.py:30 — revisar facet 'nomenclatura clara (PEP8)' em VariablesPanel.__init__
05706. [x] app\ui\widgets\variables_panel.py:30 — revisar facet 'type hints presentes' em VariablesPanel.__init__
05707. [x] app\ui\widgets\variables_panel.py:30 — revisar facet 'tratamento de erros adequado' em VariablesPanel.__init__
05708. [x] app\ui\widgets\variables_panel.py:30 — revisar facet 'sem comentários inline desnecessários' em VariablesPanel.__init__
05709. [x] app\ui\widgets\variables_panel.py:30 — revisar facet 'não imprime side-effects na UI/IO' em VariablesPanel.__init__
05710. [x] app\ui\widgets\variables_panel.py:30 — revisar facet 'thread-safety revisada' em VariablesPanel.__init__
05711. [x] app\ui\widgets\variables_panel.py:30 — revisar facet 'performance (sem loops O(n^2))' em VariablesPanel.__init__
05712. [x] app\ui\widgets\variables_panel.py:30 — revisar facet 'coberto por testes' em VariablesPanel.__init__
05713. [x] app\ui\widgets\variables_panel.py:32 — atribuição: VariablesPanel.__init__ ← ?
05714. [x] app\ui\widgets\variables_panel.py:35 — atribuição: VariablesPanel.__init__ ← ?
05715. [x] app\ui\widgets\variables_panel.py:37 — atribuição: VariablesPanel.__init__ ← layout
05716. [x] app\ui\widgets\variables_panel.py:38 — atribuição: VariablesPanel.__init__ ← ?
05717. [x] app\ui\widgets\variables_panel.py:46 — atribuição: VariablesPanel.__init__ ← bar
05718. [x] app\ui\widgets\variables_panel.py:47 — atribuição: VariablesPanel.__init__ ← ?
05719. [x] app\ui\widgets\variables_panel.py:48 — atribuição: VariablesPanel.__init__ ← ?
05720. [x] app\ui\widgets\variables_panel.py:58 — definir/revisar FunctionDef: VariablesPanel.update_tokens
05721. [x] app\ui\widgets\variables_panel.py:58 — revisar facet 'assinatura/args consistentes' em VariablesPanel.update_tokens
05722. [x] app\ui\widgets\variables_panel.py:58 — revisar facet 'docstring em português' em VariablesPanel.update_tokens
05723. [x] app\ui\widgets\variables_panel.py:58 — revisar facet 'nomenclatura clara (PEP8)' em VariablesPanel.update_tokens
05724. [x] app\ui\widgets\variables_panel.py:58 — revisar facet 'type hints presentes' em VariablesPanel.update_tokens
05725. [x] app\ui\widgets\variables_panel.py:58 — revisar facet 'tratamento de erros adequado' em VariablesPanel.update_tokens
05726. [x] app\ui\widgets\variables_panel.py:58 — revisar facet 'sem comentários inline desnecessários' em VariablesPanel.update_tokens
05727. [x] app\ui\widgets\variables_panel.py:58 — revisar facet 'não imprime side-effects na UI/IO' em VariablesPanel.update_tokens
05728. [x] app\ui\widgets\variables_panel.py:58 — revisar facet 'thread-safety revisada' em VariablesPanel.update_tokens
05729. [x] app\ui\widgets\variables_panel.py:58 — revisar facet 'performance (sem loops O(n^2))' em VariablesPanel.update_tokens
05730. [x] app\ui\widgets\variables_panel.py:58 — revisar facet 'coberto por testes' em VariablesPanel.update_tokens
05731. [x] app\ui\widgets\variables_panel.py:59 — atribuição: VariablesPanel.update_tokens ← ?
05732. [x] app\ui\widgets\variables_panel.py:62 — controle for em VariablesPanel.update_tokens
05733. [x] app\ui\widgets\variables_panel.py:63 — atribuição: VariablesPanel.update_tokens ← spec
05734. [x] app\ui\widgets\variables_panel.py:64 — controle if em VariablesPanel.update_tokens
05735. [x] app\ui\widgets\variables_panel.py:65 — atribuição: VariablesPanel.update_tokens ← label
05736. [x] app\ui\widgets\variables_panel.py:66 — atribuição: VariablesPanel.update_tokens ← color
05737. [x] app\ui\widgets\variables_panel.py:68 — atribuição: VariablesPanel.update_tokens ← label
05738. [x] app\ui\widgets\variables_panel.py:69 — atribuição: VariablesPanel.update_tokens ← color
05739. [x] app\ui\widgets\variables_panel.py:70 — atribuição: VariablesPanel.update_tokens ← item
05740. [x] app\ui\widgets\variables_panel.py:75 — return em VariablesPanel.update_tokens
05741. [x] app\ui\widgets\variables_panel.py:77 — definir/revisar FunctionDef: VariablesPanel._edit_current
05742. [x] app\ui\widgets\variables_panel.py:77 — revisar facet 'assinatura/args consistentes' em VariablesPanel._edit_current
05743. [x] app\ui\widgets\variables_panel.py:77 — revisar facet 'docstring em português' em VariablesPanel._edit_current
05744. [x] app\ui\widgets\variables_panel.py:77 — revisar facet 'nomenclatura clara (PEP8)' em VariablesPanel._edit_current
05745. [x] app\ui\widgets\variables_panel.py:77 — revisar facet 'type hints presentes' em VariablesPanel._edit_current
05746. [x] app\ui\widgets\variables_panel.py:77 — revisar facet 'tratamento de erros adequado' em VariablesPanel._edit_current
05747. [x] app\ui\widgets\variables_panel.py:77 — revisar facet 'sem comentários inline desnecessários' em VariablesPanel._edit_current
05748. [x] app\ui\widgets\variables_panel.py:77 — revisar facet 'não imprime side-effects na UI/IO' em VariablesPanel._edit_current
05749. [x] app\ui\widgets\variables_panel.py:77 — revisar facet 'thread-safety revisada' em VariablesPanel._edit_current
05750. [x] app\ui\widgets\variables_panel.py:77 — revisar facet 'performance (sem loops O(n^2))' em VariablesPanel._edit_current
05751. [x] app\ui\widgets\variables_panel.py:77 — revisar facet 'coberto por testes' em VariablesPanel._edit_current
05752. [x] app\ui\widgets\variables_panel.py:78 — import: PySide6.QtCore
05753. [x] app\ui\widgets\variables_panel.py:80 — atribuição: VariablesPanel._edit_current ← item
05754. [x] app\ui\widgets\variables_panel.py:81 — controle if em VariablesPanel._edit_current
05755. [x] app\ui\widgets\variables_panel.py:82 — return em VariablesPanel._edit_current
05756. [x] app\ui\widgets\variables_panel.py:83 — atribuição: VariablesPanel._edit_current ← text
05757. [x] app\ui\widgets\variables_panel.py:84 — controle if em VariablesPanel._edit_current
05758. [x] app\ui\widgets\variables_panel.py:85 — atribuição: VariablesPanel._edit_current ← var_id
05759. [x] app\ui\widgets\variables_panel.py:87 — atribuição: VariablesPanel._edit_current ← var_id
05760. [x] app\ui\widgets\variables_panel.py:90 — definir/revisar FunctionDef: VariablesPanel.edit_variable
05761. [x] app\ui\widgets\variables_panel.py:90 — revisar facet 'assinatura/args consistentes' em VariablesPanel.edit_variable
05762. [x] app\ui\widgets\variables_panel.py:90 — revisar facet 'docstring em português' em VariablesPanel.edit_variable
05763. [x] app\ui\widgets\variables_panel.py:90 — revisar facet 'nomenclatura clara (PEP8)' em VariablesPanel.edit_variable
05764. [x] app\ui\widgets\variables_panel.py:90 — revisar facet 'type hints presentes' em VariablesPanel.edit_variable
05765. [x] app\ui\widgets\variables_panel.py:90 — revisar facet 'tratamento de erros adequado' em VariablesPanel.edit_variable
05766. [x] app\ui\widgets\variables_panel.py:90 — revisar facet 'sem comentários inline desnecessários' em VariablesPanel.edit_variable
05767. [x] app\ui\widgets\variables_panel.py:90 — revisar facet 'não imprime side-effects na UI/IO' em VariablesPanel.edit_variable
05768. [x] app\ui\widgets\variables_panel.py:90 — revisar facet 'thread-safety revisada' em VariablesPanel.edit_variable
05769. [x] app\ui\widgets\variables_panel.py:90 — revisar facet 'performance (sem loops O(n^2))' em VariablesPanel.edit_variable
05770. [x] app\ui\widgets\variables_panel.py:90 — revisar facet 'coberto por testes' em VariablesPanel.edit_variable
05771. [x] app\ui\widgets\variables_panel.py:91 — atribuição: VariablesPanel.edit_variable ← dialog
05772. [x] app\ui\widgets\variables_panel.py:92 — controle if em VariablesPanel.edit_variable
05773. [x] app\ui\widgets\variables_panel.py:93 — atribuição: VariablesPanel.edit_variable ← ?
05774. [x] app\ui\widgets\variables_panel.py:96 — definir/revisar FunctionDef: VariablesPanel._show_menu
05775. [x] app\ui\widgets\variables_panel.py:96 — revisar facet 'assinatura/args consistentes' em VariablesPanel._show_menu
05776. [x] app\ui\widgets\variables_panel.py:96 — revisar facet 'docstring em português' em VariablesPanel._show_menu
05777. [x] app\ui\widgets\variables_panel.py:96 — revisar facet 'nomenclatura clara (PEP8)' em VariablesPanel._show_menu
05778. [x] app\ui\widgets\variables_panel.py:96 — revisar facet 'type hints presentes' em VariablesPanel._show_menu
05779. [x] app\ui\widgets\variables_panel.py:96 — revisar facet 'tratamento de erros adequado' em VariablesPanel._show_menu
05780. [x] app\ui\widgets\variables_panel.py:96 — revisar facet 'sem comentários inline desnecessários' em VariablesPanel._show_menu
05781. [x] app\ui\widgets\variables_panel.py:96 — revisar facet 'não imprime side-effects na UI/IO' em VariablesPanel._show_menu
05782. [x] app\ui\widgets\variables_panel.py:96 — revisar facet 'thread-safety revisada' em VariablesPanel._show_menu
05783. [x] app\ui\widgets\variables_panel.py:96 — revisar facet 'performance (sem loops O(n^2))' em VariablesPanel._show_menu
05784. [x] app\ui\widgets\variables_panel.py:96 — revisar facet 'coberto por testes' em VariablesPanel._show_menu
05785. [x] app\ui\widgets\variables_panel.py:97 — import: PySide6.QtGui
05786. [x] app\ui\widgets\variables_panel.py:98 — import: PySide6.QtCore
05787. [x] app\ui\widgets\variables_panel.py:100 — atribuição: VariablesPanel._show_menu ← menu
05788. [x] app\ui\widgets\variables_panel.py:101 — atribuição: VariablesPanel._show_menu ← act_min
05789. [x] app\ui\widgets\variables_panel.py:102 — atribuição: VariablesPanel._show_menu ← act_helper
05790. [x] app\ui\widgets\variables_panel.py:106 — definir/revisar FunctionDef: VariablesPanel.specs_snapshot
05791. [x] app\ui\widgets\variables_panel.py:106 — revisar facet 'assinatura/args consistentes' em VariablesPanel.specs_snapshot
05792. [x] app\ui\widgets\variables_panel.py:106 — revisar facet 'docstring em português' em VariablesPanel.specs_snapshot
05793. [x] app\ui\widgets\variables_panel.py:106 — revisar facet 'nomenclatura clara (PEP8)' em VariablesPanel.specs_snapshot
05794. [x] app\ui\widgets\variables_panel.py:106 — revisar facet 'type hints presentes' em VariablesPanel.specs_snapshot
05795. [x] app\ui\widgets\variables_panel.py:106 — revisar facet 'tratamento de erros adequado' em VariablesPanel.specs_snapshot
05796. [x] app\ui\widgets\variables_panel.py:106 — revisar facet 'sem comentários inline desnecessários' em VariablesPanel.specs_snapshot
05797. [x] app\ui\widgets\variables_panel.py:106 — revisar facet 'não imprime side-effects na UI/IO' em VariablesPanel.specs_snapshot
05798. [x] app\ui\widgets\variables_panel.py:106 — revisar facet 'thread-safety revisada' em VariablesPanel.specs_snapshot
05799. [x] app\ui\widgets\variables_panel.py:106 — revisar facet 'performance (sem loops O(n^2))' em VariablesPanel.specs_snapshot
05800. [x] app\ui\widgets\variables_panel.py:106 — revisar facet 'coberto por testes' em VariablesPanel.specs_snapshot
05801. [x] app\ui\widgets\variables_panel.py:107 — return em VariablesPanel.specs_snapshot
05802. [x] Existência e estrutura do módulo: app\workers\__init__.py
05803. [x] app\workers\__init__.py:3 — import: app.workers.sampling_worker
05804. [x] app\workers\__init__.py:5 — atribuição:  ← __all__
05805. [x] Existência e estrutura do módulo: app\workers\base_worker.py
05806. [x] app\workers\base_worker.py:3 — import: __future__
05807. [x] app\workers\base_worker.py:5 — import: PySide6.QtCore
05808. [x] app\workers\base_worker.py:8 — definir/revisar ClassDef: BaseWorker
05809. [x] app\workers\base_worker.py:11 — definir/revisar FunctionDef: BaseWorker.run
05810. [x] app\workers\base_worker.py:11 — revisar facet 'assinatura/args consistentes' em BaseWorker.run
05811. [x] app\workers\base_worker.py:11 — revisar facet 'docstring em português' em BaseWorker.run
05812. [x] app\workers\base_worker.py:11 — revisar facet 'nomenclatura clara (PEP8)' em BaseWorker.run
05813. [x] app\workers\base_worker.py:11 — revisar facet 'type hints presentes' em BaseWorker.run
05814. [x] app\workers\base_worker.py:11 — revisar facet 'tratamento de erros adequado' em BaseWorker.run
05815. [x] app\workers\base_worker.py:11 — revisar facet 'sem comentários inline desnecessários' em BaseWorker.run
05816. [x] app\workers\base_worker.py:11 — revisar facet 'não imprime side-effects na UI/IO' em BaseWorker.run
05817. [x] app\workers\base_worker.py:11 — revisar facet 'thread-safety revisada' em BaseWorker.run
05818. [x] app\workers\base_worker.py:11 — revisar facet 'performance (sem loops O(n^2))' em BaseWorker.run
05819. [x] app\workers\base_worker.py:11 — revisar facet 'coberto por testes' em BaseWorker.run
05820. [x] app\workers\base_worker.py:12 — raise em BaseWorker.run
05821. [x] Existência e estrutura do módulo: app\workers\batch_export_worker.py
05822. [x] app\workers\batch_export_worker.py:3 — import: __future__
05823. [x] app\workers\batch_export_worker.py:5 — import: typing
05824. [x] app\workers\batch_export_worker.py:7 — import: PySide6.QtCore
05825. [x] app\workers\batch_export_worker.py:9 — import: app.services.batch_export_service
05826. [x] app\workers\batch_export_worker.py:10 — import: app.workers.base_worker
05827. [x] app\workers\batch_export_worker.py:13 — definir/revisar ClassDef: BatchExportWorker
05828. [x] app\workers\batch_export_worker.py:14 — atribuição: BatchExportWorker ← progress
05829. [x] app\workers\batch_export_worker.py:15 — atribuição: BatchExportWorker ← completed
05830. [x] app\workers\batch_export_worker.py:16 — atribuição: BatchExportWorker ← failed
05831. [x] app\workers\batch_export_worker.py:18 — definir/revisar FunctionDef: BatchExportWorker.__init__
05832. [x] app\workers\batch_export_worker.py:18 — revisar facet 'assinatura/args consistentes' em BatchExportWorker.__init__
05833. [x] app\workers\batch_export_worker.py:18 — revisar facet 'docstring em português' em BatchExportWorker.__init__
05834. [x] app\workers\batch_export_worker.py:18 — revisar facet 'nomenclatura clara (PEP8)' em BatchExportWorker.__init__
05835. [x] app\workers\batch_export_worker.py:18 — revisar facet 'type hints presentes' em BatchExportWorker.__init__
05836. [x] app\workers\batch_export_worker.py:18 — revisar facet 'tratamento de erros adequado' em BatchExportWorker.__init__
05837. [x] app\workers\batch_export_worker.py:18 — revisar facet 'sem comentários inline desnecessários' em BatchExportWorker.__init__
05838. [x] app\workers\batch_export_worker.py:18 — revisar facet 'não imprime side-effects na UI/IO' em BatchExportWorker.__init__
05839. [x] app\workers\batch_export_worker.py:18 — revisar facet 'thread-safety revisada' em BatchExportWorker.__init__
05840. [x] app\workers\batch_export_worker.py:18 — revisar facet 'performance (sem loops O(n^2))' em BatchExportWorker.__init__
05841. [x] app\workers\batch_export_worker.py:18 — revisar facet 'coberto por testes' em BatchExportWorker.__init__
05842. [x] app\workers\batch_export_worker.py:29 — atribuição: BatchExportWorker.__init__ ← ?
05843. [x] app\workers\batch_export_worker.py:30 — atribuição: BatchExportWorker.__init__ ← ?
05844. [x] app\workers\batch_export_worker.py:31 — atribuição: BatchExportWorker.__init__ ← ?
05845. [x] app\workers\batch_export_worker.py:32 — atribuição: BatchExportWorker.__init__ ← ?
05846. [x] app\workers\batch_export_worker.py:33 — atribuição: BatchExportWorker.__init__ ← ?
05847. [x] app\workers\batch_export_worker.py:34 — atribuição: BatchExportWorker.__init__ ← ?
05848. [x] app\workers\batch_export_worker.py:36 — definir/revisar FunctionDef: BatchExportWorker.run
05849. [x] app\workers\batch_export_worker.py:36 — revisar facet 'assinatura/args consistentes' em BatchExportWorker.run
05850. [x] app\workers\batch_export_worker.py:36 — revisar facet 'docstring em português' em BatchExportWorker.run
05851. [x] app\workers\batch_export_worker.py:36 — revisar facet 'nomenclatura clara (PEP8)' em BatchExportWorker.run
05852. [x] app\workers\batch_export_worker.py:36 — revisar facet 'type hints presentes' em BatchExportWorker.run
05853. [x] app\workers\batch_export_worker.py:36 — revisar facet 'tratamento de erros adequado' em BatchExportWorker.run
05854. [x] app\workers\batch_export_worker.py:36 — revisar facet 'sem comentários inline desnecessários' em BatchExportWorker.run
05855. [x] app\workers\batch_export_worker.py:36 — revisar facet 'não imprime side-effects na UI/IO' em BatchExportWorker.run
05856. [x] app\workers\batch_export_worker.py:36 — revisar facet 'thread-safety revisada' em BatchExportWorker.run
05857. [x] app\workers\batch_export_worker.py:36 — revisar facet 'performance (sem loops O(n^2))' em BatchExportWorker.run
05858. [x] app\workers\batch_export_worker.py:36 — revisar facet 'coberto por testes' em BatchExportWorker.run
05859. [x] app\workers\batch_export_worker.py:37 — try em BatchExportWorker.run
05860. [x] app\workers\batch_export_worker.py:38 — atribuição: BatchExportWorker.run ← manifest
05861. [x] app\workers\batch_export_worker.py:48 — import: traceback
05862. [x] Existência e estrutura do módulo: app\workers\export_worker.py
05863. [x] app\workers\export_worker.py:3 — import: __future__
05864. [x] app\workers\export_worker.py:5 — import: pathlib
05865. [x] app\workers\export_worker.py:6 — import: typing
05866. [x] app\workers\export_worker.py:8 — import: PySide6.QtCore
05867. [x] app\workers\export_worker.py:10 — import: app.workers.base_worker
05868. [x] app\workers\export_worker.py:13 — definir/revisar ClassDef: ExportWorker
05869. [x] app\workers\export_worker.py:14 — atribuição: ExportWorker ← progress
05870. [x] app\workers\export_worker.py:15 — atribuição: ExportWorker ← completed
05871. [x] app\workers\export_worker.py:16 — atribuição: ExportWorker ← failed
05872. [x] app\workers\export_worker.py:18 — definir/revisar FunctionDef: ExportWorker.__init__
05873. [x] app\workers\export_worker.py:18 — revisar facet 'assinatura/args consistentes' em ExportWorker.__init__
05874. [x] app\workers\export_worker.py:18 — revisar facet 'docstring em português' em ExportWorker.__init__
05875. [x] app\workers\export_worker.py:18 — revisar facet 'nomenclatura clara (PEP8)' em ExportWorker.__init__
05876. [x] app\workers\export_worker.py:18 — revisar facet 'type hints presentes' em ExportWorker.__init__
05877. [x] app\workers\export_worker.py:18 — revisar facet 'tratamento de erros adequado' em ExportWorker.__init__
05878. [x] app\workers\export_worker.py:18 — revisar facet 'sem comentários inline desnecessários' em ExportWorker.__init__
05879. [x] app\workers\export_worker.py:18 — revisar facet 'não imprime side-effects na UI/IO' em ExportWorker.__init__
05880. [x] app\workers\export_worker.py:18 — revisar facet 'thread-safety revisada' em ExportWorker.__init__
05881. [x] app\workers\export_worker.py:18 — revisar facet 'performance (sem loops O(n^2))' em ExportWorker.__init__
05882. [x] app\workers\export_worker.py:18 — revisar facet 'coberto por testes' em ExportWorker.__init__
05883. [x] app\workers\export_worker.py:29 — atribuição: ExportWorker.__init__ ← ?
05884. [x] app\workers\export_worker.py:30 — atribuição: ExportWorker.__init__ ← ?
05885. [x] app\workers\export_worker.py:31 — atribuição: ExportWorker.__init__ ← ?
05886. [x] app\workers\export_worker.py:32 — atribuição: ExportWorker.__init__ ← ?
05887. [x] app\workers\export_worker.py:33 — atribuição: ExportWorker.__init__ ← ?
05888. [x] app\workers\export_worker.py:34 — atribuição: ExportWorker.__init__ ← ?
05889. [x] app\workers\export_worker.py:36 — definir/revisar FunctionDef: ExportWorker.run
05890. [x] app\workers\export_worker.py:36 — revisar facet 'assinatura/args consistentes' em ExportWorker.run
05891. [x] app\workers\export_worker.py:36 — revisar facet 'docstring em português' em ExportWorker.run
05892. [x] app\workers\export_worker.py:36 — revisar facet 'nomenclatura clara (PEP8)' em ExportWorker.run
05893. [x] app\workers\export_worker.py:36 — revisar facet 'type hints presentes' em ExportWorker.run
05894. [x] app\workers\export_worker.py:36 — revisar facet 'tratamento de erros adequado' em ExportWorker.run
05895. [x] app\workers\export_worker.py:36 — revisar facet 'sem comentários inline desnecessários' em ExportWorker.run
05896. [x] app\workers\export_worker.py:36 — revisar facet 'não imprime side-effects na UI/IO' em ExportWorker.run
05897. [x] app\workers\export_worker.py:36 — revisar facet 'thread-safety revisada' em ExportWorker.run
05898. [x] app\workers\export_worker.py:36 — revisar facet 'performance (sem loops O(n^2))' em ExportWorker.run
05899. [x] app\workers\export_worker.py:36 — revisar facet 'coberto por testes' em ExportWorker.run
05900. [x] app\workers\export_worker.py:37 — try em ExportWorker.run
05901. [x] app\workers\export_worker.py:38 — import: concurrent.futures
05902. [x] app\workers\export_worker.py:41 — atribuição: ExportWorker.run ← total
05903. [x] app\workers\export_worker.py:42 — atribuição: ExportWorker.run ← done
05904. [x] app\workers\export_worker.py:44 — controle with em ExportWorker.run
05905. [x] app\workers\export_worker.py:45 — atribuição: ExportWorker.run ← futures
05906. [x] app\workers\export_worker.py:49 — controle for em ExportWorker.run
05907. [x] app\workers\export_worker.py:52 — controle if em ExportWorker.run
05908. [x] app\workers\export_worker.py:57 — import: traceback
05909. [x] app\workers\export_worker.py:62 — definir/revisar FunctionDef: ExportWorker._write_one
05910. [x] app\workers\export_worker.py:62 — revisar facet 'assinatura/args consistentes' em ExportWorker._write_one
05911. [x] app\workers\export_worker.py:62 — revisar facet 'docstring em português' em ExportWorker._write_one
05912. [x] app\workers\export_worker.py:62 — revisar facet 'nomenclatura clara (PEP8)' em ExportWorker._write_one
05913. [x] app\workers\export_worker.py:62 — revisar facet 'type hints presentes' em ExportWorker._write_one
05914. [x] app\workers\export_worker.py:62 — revisar facet 'tratamento de erros adequado' em ExportWorker._write_one
05915. [x] app\workers\export_worker.py:62 — revisar facet 'sem comentários inline desnecessários' em ExportWorker._write_one
05916. [x] app\workers\export_worker.py:62 — revisar facet 'não imprime side-effects na UI/IO' em ExportWorker._write_one
05917. [x] app\workers\export_worker.py:62 — revisar facet 'thread-safety revisada' em ExportWorker._write_one
05918. [x] app\workers\export_worker.py:62 — revisar facet 'performance (sem loops O(n^2))' em ExportWorker._write_one
05919. [x] app\workers\export_worker.py:62 — revisar facet 'coberto por testes' em ExportWorker._write_one
05920. [x] app\workers\export_worker.py:63 — import: app.core.parsing
05921. [x] app\workers\export_worker.py:65 — atribuição: ExportWorker._write_one ← values
05922. [x] app\workers\export_worker.py:66 — atribuição: ExportWorker._write_one ← text
05923. [x] Existência e estrutura do módulo: app\workers\sampling_worker.py
05924. [x] app\workers\sampling_worker.py:3 — import: __future__
05925. [x] app\workers\sampling_worker.py:5 — import: time
05926. [x] app\workers\sampling_worker.py:6 — import: concurrent.futures
05927. [x] app\workers\sampling_worker.py:7 — import: typing
05928. [x] app\workers\sampling_worker.py:9 — import: numpy
05929. [x] app\workers\sampling_worker.py:10 — import: PySide6.QtCore
05930. [x] app\workers\sampling_worker.py:12 — import: app.domain.entities
05931. [x] app\workers\sampling_worker.py:13 — import: app.services.sampling_service
05932. [x] app\workers\sampling_worker.py:14 — import: app.workers.base_worker
05933. [x] app\workers\sampling_worker.py:17 — definir/revisar FunctionDef: _chunk_worker
05934. [x] app\workers\sampling_worker.py:17 — revisar facet 'assinatura/args consistentes' em _chunk_worker
05935. [x] app\workers\sampling_worker.py:17 — revisar facet 'docstring em português' em _chunk_worker
05936. [x] app\workers\sampling_worker.py:17 — revisar facet 'nomenclatura clara (PEP8)' em _chunk_worker
05937. [x] app\workers\sampling_worker.py:17 — revisar facet 'type hints presentes' em _chunk_worker
05938. [x] app\workers\sampling_worker.py:17 — revisar facet 'tratamento de erros adequado' em _chunk_worker
05939. [x] app\workers\sampling_worker.py:17 — revisar facet 'sem comentários inline desnecessários' em _chunk_worker
05940. [x] app\workers\sampling_worker.py:17 — revisar facet 'não imprime side-effects na UI/IO' em _chunk_worker
05941. [x] app\workers\sampling_worker.py:17 — revisar facet 'thread-safety revisada' em _chunk_worker
05942. [x] app\workers\sampling_worker.py:17 — revisar facet 'performance (sem loops O(n^2))' em _chunk_worker
05943. [x] app\workers\sampling_worker.py:17 — revisar facet 'coberto por testes' em _chunk_worker
05944. [x] app\workers\sampling_worker.py:19 — atribuição: _chunk_worker ← ?
05945. [x] app\workers\sampling_worker.py:20 — atribuição: _chunk_worker ← partial
05946. [x] app\workers\sampling_worker.py:29 — import: app.infrastructure.distribution_registry
05947. [x] app\workers\sampling_worker.py:31 — atribuição: _chunk_worker ← service
05948. [x] app\workers\sampling_worker.py:32 — atribuição: _chunk_worker ← result
05949. [x] app\workers\sampling_worker.py:33 — return em _chunk_worker
05950. [x] app\workers\sampling_worker.py:36 — definir/revisar ClassDef: SamplingWorker
05951. [x] app\workers\sampling_worker.py:37 — atribuição: SamplingWorker ← progress
05952. [x] app\workers\sampling_worker.py:38 — atribuição: SamplingWorker ← completed
05953. [x] app\workers\sampling_worker.py:39 — atribuição: SamplingWorker ← failed
05954. [x] app\workers\sampling_worker.py:41 — definir/revisar FunctionDef: SamplingWorker.__init__
05955. [x] app\workers\sampling_worker.py:41 — revisar facet 'assinatura/args consistentes' em SamplingWorker.__init__
05956. [x] app\workers\sampling_worker.py:41 — revisar facet 'docstring em português' em SamplingWorker.__init__
05957. [x] app\workers\sampling_worker.py:41 — revisar facet 'nomenclatura clara (PEP8)' em SamplingWorker.__init__
05958. [x] app\workers\sampling_worker.py:41 — revisar facet 'type hints presentes' em SamplingWorker.__init__
05959. [x] app\workers\sampling_worker.py:41 — revisar facet 'tratamento de erros adequado' em SamplingWorker.__init__
05960. [x] app\workers\sampling_worker.py:41 — revisar facet 'sem comentários inline desnecessários' em SamplingWorker.__init__
05961. [x] app\workers\sampling_worker.py:41 — revisar facet 'não imprime side-effects na UI/IO' em SamplingWorker.__init__
05962. [x] app\workers\sampling_worker.py:41 — revisar facet 'thread-safety revisada' em SamplingWorker.__init__
05963. [x] app\workers\sampling_worker.py:41 — revisar facet 'performance (sem loops O(n^2))' em SamplingWorker.__init__
05964. [x] app\workers\sampling_worker.py:41 — revisar facet 'coberto por testes' em SamplingWorker.__init__
05965. [x] app\workers\sampling_worker.py:43 — atribuição: SamplingWorker.__init__ ← ?
05966. [x] app\workers\sampling_worker.py:44 — atribuição: SamplingWorker.__init__ ← ?
05967. [x] app\workers\sampling_worker.py:46 — definir/revisar FunctionDef: SamplingWorker.run
05968. [x] app\workers\sampling_worker.py:46 — revisar facet 'assinatura/args consistentes' em SamplingWorker.run
05969. [x] app\workers\sampling_worker.py:46 — revisar facet 'docstring em português' em SamplingWorker.run
05970. [x] app\workers\sampling_worker.py:46 — revisar facet 'nomenclatura clara (PEP8)' em SamplingWorker.run
05971. [x] app\workers\sampling_worker.py:46 — revisar facet 'type hints presentes' em SamplingWorker.run
05972. [x] app\workers\sampling_worker.py:46 — revisar facet 'tratamento de erros adequado' em SamplingWorker.run
05973. [x] app\workers\sampling_worker.py:46 — revisar facet 'sem comentários inline desnecessários' em SamplingWorker.run
05974. [x] app\workers\sampling_worker.py:46 — revisar facet 'não imprime side-effects na UI/IO' em SamplingWorker.run
05975. [x] app\workers\sampling_worker.py:46 — revisar facet 'thread-safety revisada' em SamplingWorker.run
05976. [x] app\workers\sampling_worker.py:46 — revisar facet 'performance (sem loops O(n^2))' em SamplingWorker.run
05977. [x] app\workers\sampling_worker.py:46 — revisar facet 'coberto por testes' em SamplingWorker.run
05978. [x] app\workers\sampling_worker.py:47 — try em SamplingWorker.run
05979. [x] app\workers\sampling_worker.py:48 — atribuição: SamplingWorker.run ← req
05980. [x] app\workers\sampling_worker.py:50 — controle if em SamplingWorker.run
05981. [x] app\workers\sampling_worker.py:51 — atribuição: SamplingWorker.run ← result
05982. [x] app\workers\sampling_worker.py:53 — return em SamplingWorker.run
05983. [x] app\workers\sampling_worker.py:55 — atribuição: SamplingWorker.run ← chunk_size
05984. [x] app\workers\sampling_worker.py:56 — atribuição: SamplingWorker.run ← starts
05985. [x] app\workers\sampling_worker.py:57 — atribuição: SamplingWorker.run ← tasks
05986. [x] app\workers\sampling_worker.py:59 — atribuição: SamplingWorker.run ← results
05987. [x] app\workers\sampling_worker.py:60 — atribuição: SamplingWorker.run ← started
05988. [x] app\workers\sampling_worker.py:62 — controle with em SamplingWorker.run
05989. [x] app\workers\sampling_worker.py:63 — atribuição: SamplingWorker.run ← futures
05990. [x] app\workers\sampling_worker.py:64 — atribuição: SamplingWorker.run ← done
05991. [x] app\workers\sampling_worker.py:65 — controle for em SamplingWorker.run
05992. [x] app\workers\sampling_worker.py:66 — atribuição: SamplingWorker.run ← i
05993. [x] app\workers\sampling_worker.py:67 — atribuição: SamplingWorker.run ← ?
05994. [x] app\workers\sampling_worker.py:68 — atribuição: SamplingWorker.run ← ?
05995. [x] app\workers\sampling_worker.py:74 — atribuição: SamplingWorker.run ← ordered
05996. [x] app\workers\sampling_worker.py:75 — atribuição: SamplingWorker.run ← full
05997. [x] app\workers\sampling_worker.py:87 — import: traceback
05998. [x] Existência e estrutura do módulo: app\workers\task_worker.py
05999. [x] app\workers\task_worker.py:3 — import: __future__
06000. [x] app\workers\task_worker.py:5 — import: PySide6.QtCore
06001. [x] app\workers\task_worker.py:7 — import: app.services.task_scheduler
06002. [x] app\workers\task_worker.py:8 — import: app.workers.base_worker
06003. [x] app\workers\task_worker.py:11 — definir/revisar ClassDef: TaskWorker
06004. [x] app\workers\task_worker.py:12 — atribuição: TaskWorker ← taskStarted
06005. [x] app\workers\task_worker.py:13 — atribuição: TaskWorker ← taskProgress
06006. [x] app\workers\task_worker.py:14 — atribuição: TaskWorker ← taskCompleted
06007. [x] app\workers\task_worker.py:15 — atribuição: TaskWorker ← taskFailed
06008. [x] app\workers\task_worker.py:16 — atribuição: TaskWorker ← idle
06009. [x] app\workers\task_worker.py:18 — definir/revisar FunctionDef: TaskWorker.__init__
06010. [x] app\workers\task_worker.py:18 — revisar facet 'assinatura/args consistentes' em TaskWorker.__init__
06011. [x] app\workers\task_worker.py:18 — revisar facet 'docstring em português' em TaskWorker.__init__
06012. [x] app\workers\task_worker.py:18 — revisar facet 'nomenclatura clara (PEP8)' em TaskWorker.__init__
06013. [x] app\workers\task_worker.py:18 — revisar facet 'type hints presentes' em TaskWorker.__init__
06014. [x] app\workers\task_worker.py:18 — revisar facet 'tratamento de erros adequado' em TaskWorker.__init__
06015. [x] app\workers\task_worker.py:18 — revisar facet 'sem comentários inline desnecessários' em TaskWorker.__init__
06016. [x] app\workers\task_worker.py:18 — revisar facet 'não imprime side-effects na UI/IO' em TaskWorker.__init__
06017. [x] app\workers\task_worker.py:18 — revisar facet 'thread-safety revisada' em TaskWorker.__init__
06018. [x] app\workers\task_worker.py:18 — revisar facet 'performance (sem loops O(n^2))' em TaskWorker.__init__
06019. [x] app\workers\task_worker.py:18 — revisar facet 'coberto por testes' em TaskWorker.__init__
06020. [x] app\workers\task_worker.py:20 — atribuição: TaskWorker.__init__ ← ?
06021. [x] app\workers\task_worker.py:21 — atribuição: TaskWorker.__init__ ← ?
06022. [x] app\workers\task_worker.py:22 — atribuição: TaskWorker.__init__ ← ?
06023. [x] app\workers\task_worker.py:24 — definir/revisar FunctionDef: TaskWorker.stop
06024. [x] app\workers\task_worker.py:24 — revisar facet 'assinatura/args consistentes' em TaskWorker.stop
06025. [x] app\workers\task_worker.py:24 — revisar facet 'docstring em português' em TaskWorker.stop
06026. [x] app\workers\task_worker.py:24 — revisar facet 'nomenclatura clara (PEP8)' em TaskWorker.stop
06027. [x] app\workers\task_worker.py:24 — revisar facet 'type hints presentes' em TaskWorker.stop
06028. [x] app\workers\task_worker.py:24 — revisar facet 'tratamento de erros adequado' em TaskWorker.stop
06029. [x] app\workers\task_worker.py:24 — revisar facet 'sem comentários inline desnecessários' em TaskWorker.stop
06030. [x] app\workers\task_worker.py:24 — revisar facet 'não imprime side-effects na UI/IO' em TaskWorker.stop
06031. [x] app\workers\task_worker.py:24 — revisar facet 'thread-safety revisada' em TaskWorker.stop
06032. [x] app\workers\task_worker.py:24 — revisar facet 'performance (sem loops O(n^2))' em TaskWorker.stop
06033. [x] app\workers\task_worker.py:24 — revisar facet 'coberto por testes' em TaskWorker.stop
06034. [x] app\workers\task_worker.py:25 — atribuição: TaskWorker.stop ← ?
06035. [x] app\workers\task_worker.py:27 — definir/revisar FunctionDef: TaskWorker.run
06036. [x] app\workers\task_worker.py:27 — revisar facet 'assinatura/args consistentes' em TaskWorker.run
06037. [x] app\workers\task_worker.py:27 — revisar facet 'docstring em português' em TaskWorker.run
06038. [x] app\workers\task_worker.py:27 — revisar facet 'nomenclatura clara (PEP8)' em TaskWorker.run
06039. [x] app\workers\task_worker.py:27 — revisar facet 'type hints presentes' em TaskWorker.run
06040. [x] app\workers\task_worker.py:27 — revisar facet 'tratamento de erros adequado' em TaskWorker.run
06041. [x] app\workers\task_worker.py:27 — revisar facet 'sem comentários inline desnecessários' em TaskWorker.run
06042. [x] app\workers\task_worker.py:27 — revisar facet 'não imprime side-effects na UI/IO' em TaskWorker.run
06043. [x] app\workers\task_worker.py:27 — revisar facet 'thread-safety revisada' em TaskWorker.run
06044. [x] app\workers\task_worker.py:27 — revisar facet 'performance (sem loops O(n^2))' em TaskWorker.run
06045. [x] app\workers\task_worker.py:27 — revisar facet 'coberto por testes' em TaskWorker.run
06046. [x] app\workers\task_worker.py:28 — controle while em TaskWorker.run
06047. [x] app\workers\task_worker.py:29 — atribuição: TaskWorker.run ← task
06048. [x] app\workers\task_worker.py:30 — controle if em TaskWorker.run
06049. [x] app\workers\task_worker.py:36 — try em TaskWorker.run
06050. [x] app\workers\task_worker.py:48 — import: traceback
06051. [x] Existência e estrutura do módulo: examples\run_example.py
06052. [x] examples\run_example.py:3 — import: __future__
06053. [x] examples\run_example.py:5 — import: json
06054. [x] examples\run_example.py:6 — import: sys
06055. [x] examples\run_example.py:7 — import: tempfile
06056. [x] examples\run_example.py:8 — import: pathlib
06057. [x] examples\run_example.py:10 — atribuição:  ← ROOT
06058. [x] examples\run_example.py:11 — controle if em 
06059. [x] examples\run_example.py:14 — import: app.container
06060. [x] examples\run_example.py:15 — import: app.core.parsing
06061. [x] examples\run_example.py:16 — import: app.domain.entities
06062. [x] examples\run_example.py:19 — definir/revisar FunctionDef: main
06063. [x] examples\run_example.py:19 — revisar facet 'assinatura/args consistentes' em main
06064. [x] examples\run_example.py:19 — revisar facet 'docstring em português' em main
06065. [x] examples\run_example.py:19 — revisar facet 'nomenclatura clara (PEP8)' em main
06066. [x] examples\run_example.py:19 — revisar facet 'type hints presentes' em main
06067. [x] examples\run_example.py:19 — revisar facet 'tratamento de erros adequado' em main
06068. [x] examples\run_example.py:19 — revisar facet 'sem comentários inline desnecessários' em main
06069. [x] examples\run_example.py:19 — revisar facet 'não imprime side-effects na UI/IO' em main
06070. [x] examples\run_example.py:19 — revisar facet 'thread-safety revisada' em main
06071. [x] examples\run_example.py:19 — revisar facet 'performance (sem loops O(n^2))' em main
06072. [x] examples\run_example.py:19 — revisar facet 'coberto por testes' em main
06073. [x] examples\run_example.py:20 — atribuição: main ← project_root
06074. [x] examples\run_example.py:21 — atribuição: main ← spec_file
06075. [x] examples\run_example.py:22 — atribuição: main ← template_file
06076. [x] examples\run_example.py:24 — controle with em main
06077. [x] examples\run_example.py:25 — atribuição: main ← template_text
06078. [x] examples\run_example.py:26 — controle with em main
06079. [x] examples\run_example.py:27 — atribuição: main ← config
06080. [x] examples\run_example.py:29 — atribuição: main ← container
06081. [x] examples\run_example.py:31 — atribuição: main ← var_ids
06082. [x] examples\run_example.py:34 — atribuição: main ← specs
06083. [x] examples\run_example.py:35 — controle for em main
06084. [x] examples\run_example.py:36 — atribuição: main ← ?
06085. [x] examples\run_example.py:41 — atribuição: main ← missing
06086. [x] examples\run_example.py:42 — controle if em main
06087. [x] examples\run_example.py:44 — controle for em main
06088. [x] examples\run_example.py:45 — atribuição: main ← ?
06089. [x] examples\run_example.py:47 — atribuição: main ← request
06090. [x] examples\run_example.py:55 — atribuição: main ← result
06091. [x] examples\run_example.py:58 — atribuição: main ← batch_id
06092. [x] examples\run_example.py:63 — atribuição: main ← version_id
06093. [x] examples\run_example.py:65 — atribuição: main ← output_root
06094. [x] examples\run_example.py:66 — atribuição: main ← manifest
06095. [x] examples\run_example.py:75 — return em main
06096. [x] examples\run_example.py:78 — controle if em 
06097. [x] Verificar arquivo de exemplo: examples\template.dat
06098. [x] Existência e estrutura do módulo: main.py
06099. [x] main.py:3 — import: __future__
06100. [x] main.py:5 — import: platform
06101. [x] main.py:6 — import: sys
06102. [x] main.py:9 — definir/revisar FunctionDef: main
06103. [x] main.py:9 — revisar facet 'assinatura/args consistentes' em main
06104. [x] main.py:9 — revisar facet 'docstring em português' em main
06105. [x] main.py:9 — revisar facet 'nomenclatura clara (PEP8)' em main
06106. [x] main.py:9 — revisar facet 'type hints presentes' em main
06107. [x] main.py:9 — revisar facet 'tratamento de erros adequado' em main
06108. [x] main.py:9 — revisar facet 'sem comentários inline desnecessários' em main
06109. [x] main.py:9 — revisar facet 'não imprime side-effects na UI/IO' em main
06110. [x] main.py:9 — revisar facet 'thread-safety revisada' em main
06111. [x] main.py:9 — revisar facet 'performance (sem loops O(n^2))' em main
06112. [x] main.py:9 — revisar facet 'coberto por testes' em main
06113. [x] main.py:11 — import: PySide6.QtWidgets
06114. [x] main.py:12 — import: sys
06115. [x] main.py:14 — import: app
06116. [x] main.py:15 — import: app.container
06117. [x] main.py:16 — import: app.ui.main_window
06118. [x] main.py:19 — atribuição: main ← app
06119. [x] main.py:22 — atribuição: main ← container
06120. [x] main.py:23 — atribuição: main ← window
06121. [x] main.py:26 — atribuição: main ← exit_code
06122. [x] main.py:28 — return em main
06123. [x] main.py:31 — controle if em 
06124. [x] Existência e estrutura do módulo: plugins\triangular_example.py
06125. [x] plugins\triangular_example.py:3 — import: __future__
06126. [x] plugins\triangular_example.py:5 — import: typing
06127. [x] plugins\triangular_example.py:7 — import: numpy
06128. [x] plugins\triangular_example.py:9 — import: app.domain.entities
06129. [x] plugins\triangular_example.py:10 — import: app.infrastructure.providers.base
06130. [x] plugins\triangular_example.py:13 — definir/revisar ClassDef: TriangularProvider
06131. [x] plugins\triangular_example.py:14 — atribuição: TriangularProvider ← provider_name
06132. [x] plugins\triangular_example.py:15 — atribuição: TriangularProvider ← description
06133. [x] plugins\triangular_example.py:17 — definir/revisar FunctionDef: TriangularProvider.list_distributions
06134. [x] plugins\triangular_example.py:17 — revisar facet 'assinatura/args consistentes' em TriangularProvider.list_distributions
06135. [x] plugins\triangular_example.py:17 — revisar facet 'docstring em português' em TriangularProvider.list_distributions
06136. [x] plugins\triangular_example.py:17 — revisar facet 'nomenclatura clara (PEP8)' em TriangularProvider.list_distributions
06137. [x] plugins\triangular_example.py:17 — revisar facet 'type hints presentes' em TriangularProvider.list_distributions
06138. [x] plugins\triangular_example.py:17 — revisar facet 'tratamento de erros adequado' em TriangularProvider.list_distributions
06139. [x] plugins\triangular_example.py:17 — revisar facet 'sem comentários inline desnecessários' em TriangularProvider.list_distributions
06140. [x] plugins\triangular_example.py:17 — revisar facet 'não imprime side-effects na UI/IO' em TriangularProvider.list_distributions
06141. [x] plugins\triangular_example.py:17 — revisar facet 'thread-safety revisada' em TriangularProvider.list_distributions
06142. [x] plugins\triangular_example.py:17 — revisar facet 'performance (sem loops O(n^2))' em TriangularProvider.list_distributions
06143. [x] plugins\triangular_example.py:17 — revisar facet 'coberto por testes' em TriangularProvider.list_distributions
06144. [x] plugins\triangular_example.py:18 — return em TriangularProvider.list_distributions
06145. [x] plugins\triangular_example.py:20 — definir/revisar FunctionDef: TriangularProvider.parameter_names
06146. [x] plugins\triangular_example.py:20 — revisar facet 'assinatura/args consistentes' em TriangularProvider.parameter_names
06147. [x] plugins\triangular_example.py:20 — revisar facet 'docstring em português' em TriangularProvider.parameter_names
06148. [x] plugins\triangular_example.py:20 — revisar facet 'nomenclatura clara (PEP8)' em TriangularProvider.parameter_names
06149. [x] plugins\triangular_example.py:20 — revisar facet 'type hints presentes' em TriangularProvider.parameter_names
06150. [x] plugins\triangular_example.py:20 — revisar facet 'tratamento de erros adequado' em TriangularProvider.parameter_names
06151. [x] plugins\triangular_example.py:20 — revisar facet 'sem comentários inline desnecessários' em TriangularProvider.parameter_names
06152. [x] plugins\triangular_example.py:20 — revisar facet 'não imprime side-effects na UI/IO' em TriangularProvider.parameter_names
06153. [x] plugins\triangular_example.py:20 — revisar facet 'thread-safety revisada' em TriangularProvider.parameter_names
06154. [x] plugins\triangular_example.py:20 — revisar facet 'performance (sem loops O(n^2))' em TriangularProvider.parameter_names
06155. [x] plugins\triangular_example.py:20 — revisar facet 'coberto por testes' em TriangularProvider.parameter_names
06156. [x] plugins\triangular_example.py:21 — return em TriangularProvider.parameter_names
06157. [x] plugins\triangular_example.py:23 — definir/revisar FunctionDef: TriangularProvider.sample
06158. [x] plugins\triangular_example.py:23 — revisar facet 'assinatura/args consistentes' em TriangularProvider.sample
06159. [x] plugins\triangular_example.py:23 — revisar facet 'docstring em português' em TriangularProvider.sample
06160. [x] plugins\triangular_example.py:23 — revisar facet 'nomenclatura clara (PEP8)' em TriangularProvider.sample
06161. [x] plugins\triangular_example.py:23 — revisar facet 'type hints presentes' em TriangularProvider.sample
06162. [x] plugins\triangular_example.py:23 — revisar facet 'tratamento de erros adequado' em TriangularProvider.sample
06163. [x] plugins\triangular_example.py:23 — revisar facet 'sem comentários inline desnecessários' em TriangularProvider.sample
06164. [x] plugins\triangular_example.py:23 — revisar facet 'não imprime side-effects na UI/IO' em TriangularProvider.sample
06165. [x] plugins\triangular_example.py:23 — revisar facet 'thread-safety revisada' em TriangularProvider.sample
06166. [x] plugins\triangular_example.py:23 — revisar facet 'performance (sem loops O(n^2))' em TriangularProvider.sample
06167. [x] plugins\triangular_example.py:23 — revisar facet 'coberto por testes' em TriangularProvider.sample
06168. [x] plugins\triangular_example.py:24 — atribuição: TriangularProvider.sample ← a
06169. [x] plugins\triangular_example.py:25 — atribuição: TriangularProvider.sample ← c
06170. [x] plugins\triangular_example.py:26 — atribuição: TriangularProvider.sample ← b
06171. [x] plugins\triangular_example.py:27 — return em TriangularProvider.sample
06172. [x] plugins\triangular_example.py:29 — definir/revisar FunctionDef: TriangularProvider.ppf
06173. [x] plugins\triangular_example.py:29 — revisar facet 'assinatura/args consistentes' em TriangularProvider.ppf
06174. [x] plugins\triangular_example.py:29 — revisar facet 'docstring em português' em TriangularProvider.ppf
06175. [x] plugins\triangular_example.py:29 — revisar facet 'nomenclatura clara (PEP8)' em TriangularProvider.ppf
06176. [x] plugins\triangular_example.py:29 — revisar facet 'type hints presentes' em TriangularProvider.ppf
06177. [x] plugins\triangular_example.py:29 — revisar facet 'tratamento de erros adequado' em TriangularProvider.ppf
06178. [x] plugins\triangular_example.py:29 — revisar facet 'sem comentários inline desnecessários' em TriangularProvider.ppf
06179. [x] plugins\triangular_example.py:29 — revisar facet 'não imprime side-effects na UI/IO' em TriangularProvider.ppf
06180. [x] plugins\triangular_example.py:29 — revisar facet 'thread-safety revisada' em TriangularProvider.ppf
06181. [x] plugins\triangular_example.py:29 — revisar facet 'performance (sem loops O(n^2))' em TriangularProvider.ppf
06182. [x] plugins\triangular_example.py:29 — revisar facet 'coberto por testes' em TriangularProvider.ppf
06183. [x] plugins\triangular_example.py:30 — atribuição: TriangularProvider.ppf ← u
06184. [x] plugins\triangular_example.py:31 — atribuição: TriangularProvider.ppf ← a
06185. [x] plugins\triangular_example.py:32 — atribuição: TriangularProvider.ppf ← c
06186. [x] plugins\triangular_example.py:33 — atribuição: TriangularProvider.ppf ← b
06187. [x] plugins\triangular_example.py:34 — import: scipy
06188. [x] plugins\triangular_example.py:36 — return em TriangularProvider.ppf
06189. [x] plugins\triangular_example.py:38 — definir/revisar FunctionDef: TriangularProvider.validate
06190. [x] plugins\triangular_example.py:38 — revisar facet 'assinatura/args consistentes' em TriangularProvider.validate
06191. [x] plugins\triangular_example.py:38 — revisar facet 'docstring em português' em TriangularProvider.validate
06192. [x] plugins\triangular_example.py:38 — revisar facet 'nomenclatura clara (PEP8)' em TriangularProvider.validate
06193. [x] plugins\triangular_example.py:38 — revisar facet 'type hints presentes' em TriangularProvider.validate
06194. [x] plugins\triangular_example.py:38 — revisar facet 'tratamento de erros adequado' em TriangularProvider.validate
06195. [x] plugins\triangular_example.py:38 — revisar facet 'sem comentários inline desnecessários' em TriangularProvider.validate
06196. [x] plugins\triangular_example.py:38 — revisar facet 'não imprime side-effects na UI/IO' em TriangularProvider.validate
06197. [x] plugins\triangular_example.py:38 — revisar facet 'thread-safety revisada' em TriangularProvider.validate
06198. [x] plugins\triangular_example.py:38 — revisar facet 'performance (sem loops O(n^2))' em TriangularProvider.validate
06199. [x] plugins\triangular_example.py:38 — revisar facet 'coberto por testes' em TriangularProvider.validate
06200. [x] plugins\triangular_example.py:39 — controle if em TriangularProvider.validate
06201. [x] plugins\triangular_example.py:40 — return em TriangularProvider.validate
06202. [x] plugins\triangular_example.py:41 — return em TriangularProvider.validate
06203. [x] Existência e estrutura do módulo: tests\conftest.py
06204. [x] tests\conftest.py:3 — import: sys
06205. [x] tests\conftest.py:4 — import: pathlib
06206. [x] tests\conftest.py:6 — import: pytest
06207. [x] tests\conftest.py:8 — atribuição:  ← PROJECT_ROOT
06208. [x] tests\conftest.py:9 — controle if em 
06209. [x] tests\conftest.py:14 — definir/revisar FunctionDef: registry
06210. [x] tests\conftest.py:14 — revisar facet 'assinatura/args consistentes' em registry
06211. [x] tests\conftest.py:14 — revisar facet 'docstring em português' em registry
06212. [x] tests\conftest.py:14 — revisar facet 'nomenclatura clara (PEP8)' em registry
06213. [x] tests\conftest.py:14 — revisar facet 'type hints presentes' em registry
06214. [x] tests\conftest.py:14 — revisar facet 'tratamento de erros adequado' em registry
06215. [x] tests\conftest.py:14 — revisar facet 'sem comentários inline desnecessários' em registry
06216. [x] tests\conftest.py:14 — revisar facet 'não imprime side-effects na UI/IO' em registry
06217. [x] tests\conftest.py:14 — revisar facet 'thread-safety revisada' em registry
06218. [x] tests\conftest.py:14 — revisar facet 'performance (sem loops O(n^2))' em registry
06219. [x] tests\conftest.py:14 — revisar facet 'coberto por testes' em registry
06220. [x] tests\conftest.py:15 — import: app.infrastructure.distribution_registry
06221. [x] tests\conftest.py:17 — return em registry
06222. [x] tests\conftest.py:21 — definir/revisar FunctionDef: sampling_service
06223. [x] tests\conftest.py:21 — revisar facet 'assinatura/args consistentes' em sampling_service
06224. [x] tests\conftest.py:21 — revisar facet 'docstring em português' em sampling_service
06225. [x] tests\conftest.py:21 — revisar facet 'nomenclatura clara (PEP8)' em sampling_service
06226. [x] tests\conftest.py:21 — revisar facet 'type hints presentes' em sampling_service
06227. [x] tests\conftest.py:21 — revisar facet 'tratamento de erros adequado' em sampling_service
06228. [x] tests\conftest.py:21 — revisar facet 'sem comentários inline desnecessários' em sampling_service
06229. [x] tests\conftest.py:21 — revisar facet 'não imprime side-effects na UI/IO' em sampling_service
06230. [x] tests\conftest.py:21 — revisar facet 'thread-safety revisada' em sampling_service
06231. [x] tests\conftest.py:21 — revisar facet 'performance (sem loops O(n^2))' em sampling_service
06232. [x] tests\conftest.py:21 — revisar facet 'coberto por testes' em sampling_service
06233. [x] tests\conftest.py:22 — import: app.services.sampling_service
06234. [x] tests\conftest.py:24 — return em sampling_service
06235. [x] tests\conftest.py:28 — definir/revisar FunctionDef: repos
06236. [x] tests\conftest.py:28 — revisar facet 'assinatura/args consistentes' em repos
06237. [x] tests\conftest.py:28 — revisar facet 'docstring em português' em repos
06238. [x] tests\conftest.py:28 — revisar facet 'nomenclatura clara (PEP8)' em repos
06239. [x] tests\conftest.py:28 — revisar facet 'type hints presentes' em repos
06240. [x] tests\conftest.py:28 — revisar facet 'tratamento de erros adequado' em repos
06241. [x] tests\conftest.py:28 — revisar facet 'sem comentários inline desnecessários' em repos
06242. [x] tests\conftest.py:28 — revisar facet 'não imprime side-effects na UI/IO' em repos
06243. [x] tests\conftest.py:28 — revisar facet 'thread-safety revisada' em repos
06244. [x] tests\conftest.py:28 — revisar facet 'performance (sem loops O(n^2))' em repos
06245. [x] tests\conftest.py:28 — revisar facet 'coberto por testes' em repos
06246. [x] tests\conftest.py:29 — import: app.infrastructure.experiment_repository
06247. [x] tests\conftest.py:30 — import: app.infrastructure.template_repository
06248. [x] tests\conftest.py:32 — atribuição: repos ← exp
06249. [x] tests\conftest.py:33 — atribuição: repos ← tpl
06250. [x] tests\conftest.py:34 — return em repos
06251. [x] tests\conftest.py:38 — definir/revisar FunctionDef: log_repo
06252. [x] tests\conftest.py:38 — revisar facet 'assinatura/args consistentes' em log_repo
06253. [x] tests\conftest.py:38 — revisar facet 'docstring em português' em log_repo
06254. [x] tests\conftest.py:38 — revisar facet 'nomenclatura clara (PEP8)' em log_repo
06255. [x] tests\conftest.py:38 — revisar facet 'type hints presentes' em log_repo
06256. [x] tests\conftest.py:38 — revisar facet 'tratamento de erros adequado' em log_repo
06257. [x] tests\conftest.py:38 — revisar facet 'sem comentários inline desnecessários' em log_repo
06258. [x] tests\conftest.py:38 — revisar facet 'não imprime side-effects na UI/IO' em log_repo
06259. [x] tests\conftest.py:38 — revisar facet 'thread-safety revisada' em log_repo
06260. [x] tests\conftest.py:38 — revisar facet 'performance (sem loops O(n^2))' em log_repo
06261. [x] tests\conftest.py:38 — revisar facet 'coberto por testes' em log_repo
06262. [x] tests\conftest.py:39 — import: app.infrastructure.async_log_repository
06263. [x] tests\conftest.py:41 — atribuição: log_repo ← repo
06264. [x] tests\conftest.py:47 — definir/revisar FunctionDef: log_service
06265. [x] tests\conftest.py:47 — revisar facet 'assinatura/args consistentes' em log_service
06266. [x] tests\conftest.py:47 — revisar facet 'docstring em português' em log_service
06267. [x] tests\conftest.py:47 — revisar facet 'nomenclatura clara (PEP8)' em log_service
06268. [x] tests\conftest.py:47 — revisar facet 'type hints presentes' em log_service
06269. [x] tests\conftest.py:47 — revisar facet 'tratamento de erros adequado' em log_service
06270. [x] tests\conftest.py:47 — revisar facet 'sem comentários inline desnecessários' em log_service
06271. [x] tests\conftest.py:47 — revisar facet 'não imprime side-effects na UI/IO' em log_service
06272. [x] tests\conftest.py:47 — revisar facet 'thread-safety revisada' em log_service
06273. [x] tests\conftest.py:47 — revisar facet 'performance (sem loops O(n^2))' em log_service
06274. [x] tests\conftest.py:47 — revisar facet 'coberto por testes' em log_service
06275. [x] tests\conftest.py:48 — atribuição: log_service ← module
06276. [x] tests\conftest.py:49 — return em log_service
06277. [x] tests\conftest.py:53 — definir/revisar FunctionDef: container
06278. [x] tests\conftest.py:53 — revisar facet 'assinatura/args consistentes' em container
06279. [x] tests\conftest.py:53 — revisar facet 'docstring em português' em container
06280. [x] tests\conftest.py:53 — revisar facet 'nomenclatura clara (PEP8)' em container
06281. [x] tests\conftest.py:53 — revisar facet 'type hints presentes' em container
06282. [x] tests\conftest.py:53 — revisar facet 'tratamento de erros adequado' em container
06283. [x] tests\conftest.py:53 — revisar facet 'sem comentários inline desnecessários' em container
06284. [x] tests\conftest.py:53 — revisar facet 'não imprime side-effects na UI/IO' em container
06285. [x] tests\conftest.py:53 — revisar facet 'thread-safety revisada' em container
06286. [x] tests\conftest.py:53 — revisar facet 'performance (sem loops O(n^2))' em container
06287. [x] tests\conftest.py:53 — revisar facet 'coberto por testes' em container
06288. [x] tests\conftest.py:54 — import: app.container
06289. [x] tests\conftest.py:56 — atribuição: container ← c
06290. [x] tests\conftest.py:63 — definir/revisar FunctionDef: populated_batch
06291. [x] tests\conftest.py:63 — revisar facet 'assinatura/args consistentes' em populated_batch
06292. [x] tests\conftest.py:63 — revisar facet 'docstring em português' em populated_batch
06293. [x] tests\conftest.py:63 — revisar facet 'nomenclatura clara (PEP8)' em populated_batch
06294. [x] tests\conftest.py:63 — revisar facet 'type hints presentes' em populated_batch
06295. [x] tests\conftest.py:63 — revisar facet 'tratamento de erros adequado' em populated_batch
06296. [x] tests\conftest.py:63 — revisar facet 'sem comentários inline desnecessários' em populated_batch
06297. [x] tests\conftest.py:63 — revisar facet 'não imprime side-effects na UI/IO' em populated_batch
06298. [x] tests\conftest.py:63 — revisar facet 'thread-safety revisada' em populated_batch
06299. [x] tests\conftest.py:63 — revisar facet 'performance (sem loops O(n^2))' em populated_batch
06300. [x] tests\conftest.py:63 — revisar facet 'coberto por testes' em populated_batch
06301. [x] tests\conftest.py:64 — import: app.domain.entities
06302. [x] tests\conftest.py:66 — atribuição: populated_batch ← request
06303. [x] tests\conftest.py:76 — atribuição: populated_batch ← result
06304. [x] tests\conftest.py:80 — atribuição: populated_batch ← version_id
06305. [x] tests\conftest.py:81 — return em populated_batch
06306. [x] tests\conftest.py:85 — definir/revisar FunctionDef: main_window_offscreen
06307. [x] tests\conftest.py:85 — revisar facet 'assinatura/args consistentes' em main_window_offscreen
06308. [x] tests\conftest.py:85 — revisar facet 'docstring em português' em main_window_offscreen
06309. [x] tests\conftest.py:85 — revisar facet 'nomenclatura clara (PEP8)' em main_window_offscreen
06310. [x] tests\conftest.py:85 — revisar facet 'type hints presentes' em main_window_offscreen
06311. [x] tests\conftest.py:85 — revisar facet 'tratamento de erros adequado' em main_window_offscreen
06312. [x] tests\conftest.py:85 — revisar facet 'sem comentários inline desnecessários' em main_window_offscreen
06313. [x] tests\conftest.py:85 — revisar facet 'não imprime side-effects na UI/IO' em main_window_offscreen
06314. [x] tests\conftest.py:85 — revisar facet 'thread-safety revisada' em main_window_offscreen
06315. [x] tests\conftest.py:85 — revisar facet 'performance (sem loops O(n^2))' em main_window_offscreen
06316. [x] tests\conftest.py:85 — revisar facet 'coberto por testes' em main_window_offscreen
06317. [x] tests\conftest.py:87 — import: PySide6.QtWidgets
06318. [x] tests\conftest.py:91 — import: app.container
06319. [x] tests\conftest.py:92 — import: app.ui.main_window
06320. [x] tests\conftest.py:94 — atribuição: main_window_offscreen ← container
06321. [x] tests\conftest.py:95 — atribuição: main_window_offscreen ← window
06322. [x] Existência e estrutura do módulo: tests\test_analysis_service.py
06323. [x] tests\test_analysis_service.py:3 — import: numpy
06324. [x] tests\test_analysis_service.py:4 — import: pytest
06325. [x] tests\test_analysis_service.py:7 — definir/revisar FunctionDef: test_comparison_service
06326. [x] tests\test_analysis_service.py:7 — revisar facet 'assinatura/args consistentes' em test_comparison_service
06327. [x] tests\test_analysis_service.py:7 — revisar facet 'docstring em português' em test_comparison_service
06328. [x] tests\test_analysis_service.py:7 — revisar facet 'nomenclatura clara (PEP8)' em test_comparison_service
06329. [x] tests\test_analysis_service.py:7 — revisar facet 'type hints presentes' em test_comparison_service
06330. [x] tests\test_analysis_service.py:7 — revisar facet 'tratamento de erros adequado' em test_comparison_service
06331. [x] tests\test_analysis_service.py:7 — revisar facet 'sem comentários inline desnecessários' em test_comparison_service
06332. [x] tests\test_analysis_service.py:7 — revisar facet 'não imprime side-effects na UI/IO' em test_comparison_service
06333. [x] tests\test_analysis_service.py:7 — revisar facet 'thread-safety revisada' em test_comparison_service
06334. [x] tests\test_analysis_service.py:7 — revisar facet 'performance (sem loops O(n^2))' em test_comparison_service
06335. [x] tests\test_analysis_service.py:7 — revisar facet 'coberto por testes' em test_comparison_service
06336. [x] tests\test_analysis_service.py:8 — atribuição: test_comparison_service ← svc
06337. [x] tests\test_analysis_service.py:9 — atribuição: test_comparison_service ← result
06338. [x] tests\test_analysis_service.py:11 — atribuição: test_comparison_service ← diffs
06339. [x] tests\test_analysis_service.py:16 — definir/revisar FunctionDef: test_batch_comparison_service
06340. [x] tests\test_analysis_service.py:16 — revisar facet 'assinatura/args consistentes' em test_batch_comparison_service
06341. [x] tests\test_analysis_service.py:16 — revisar facet 'docstring em português' em test_batch_comparison_service
06342. [x] tests\test_analysis_service.py:16 — revisar facet 'nomenclatura clara (PEP8)' em test_batch_comparison_service
06343. [x] tests\test_analysis_service.py:16 — revisar facet 'type hints presentes' em test_batch_comparison_service
06344. [x] tests\test_analysis_service.py:16 — revisar facet 'tratamento de erros adequado' em test_batch_comparison_service
06345. [x] tests\test_analysis_service.py:16 — revisar facet 'sem comentários inline desnecessários' em test_batch_comparison_service
06346. [x] tests\test_analysis_service.py:16 — revisar facet 'não imprime side-effects na UI/IO' em test_batch_comparison_service
06347. [x] tests\test_analysis_service.py:16 — revisar facet 'thread-safety revisada' em test_batch_comparison_service
06348. [x] tests\test_analysis_service.py:16 — revisar facet 'performance (sem loops O(n^2))' em test_batch_comparison_service
06349. [x] tests\test_analysis_service.py:16 — revisar facet 'coberto por testes' em test_batch_comparison_service
06350. [x] tests\test_analysis_service.py:18 — atribuição: test_batch_comparison_service ← values
06351. [x] tests\test_analysis_service.py:19 — atribuição: test_batch_comparison_service ← new_matrix
06352. [x] tests\test_analysis_service.py:22 — atribuição: test_batch_comparison_service ← cmp
06353. [x] tests\test_analysis_service.py:24 — atribuição: test_batch_comparison_service ← var1
06354. [x] tests\test_analysis_service.py:30 — definir/revisar FunctionDef: test_statistics_service
06355. [x] tests\test_analysis_service.py:30 — revisar facet 'assinatura/args consistentes' em test_statistics_service
06356. [x] tests\test_analysis_service.py:30 — revisar facet 'docstring em português' em test_statistics_service
06357. [x] tests\test_analysis_service.py:30 — revisar facet 'nomenclatura clara (PEP8)' em test_statistics_service
06358. [x] tests\test_analysis_service.py:30 — revisar facet 'type hints presentes' em test_statistics_service
06359. [x] tests\test_analysis_service.py:30 — revisar facet 'tratamento de erros adequado' em test_statistics_service
06360. [x] tests\test_analysis_service.py:30 — revisar facet 'sem comentários inline desnecessários' em test_statistics_service
06361. [x] tests\test_analysis_service.py:30 — revisar facet 'não imprime side-effects na UI/IO' em test_statistics_service
06362. [x] tests\test_analysis_service.py:30 — revisar facet 'thread-safety revisada' em test_statistics_service
06363. [x] tests\test_analysis_service.py:30 — revisar facet 'performance (sem loops O(n^2))' em test_statistics_service
06364. [x] tests\test_analysis_service.py:30 — revisar facet 'coberto por testes' em test_statistics_service
06365. [x] tests\test_analysis_service.py:31 — atribuição: test_statistics_service ← values
06366. [x] tests\test_analysis_service.py:32 — atribuição: test_statistics_service ← stats
06367. [x] tests\test_analysis_service.py:37 — atribuição: test_statistics_service ← stats_empty
06368. [x] tests\test_analysis_service.py:41 — definir/revisar FunctionDef: test_metrics_service
06369. [x] tests\test_analysis_service.py:41 — revisar facet 'assinatura/args consistentes' em test_metrics_service
06370. [x] tests\test_analysis_service.py:41 — revisar facet 'docstring em português' em test_metrics_service
06371. [x] tests\test_analysis_service.py:41 — revisar facet 'nomenclatura clara (PEP8)' em test_metrics_service
06372. [x] tests\test_analysis_service.py:41 — revisar facet 'type hints presentes' em test_metrics_service
06373. [x] tests\test_analysis_service.py:41 — revisar facet 'tratamento de erros adequado' em test_metrics_service
06374. [x] tests\test_analysis_service.py:41 — revisar facet 'sem comentários inline desnecessários' em test_metrics_service
06375. [x] tests\test_analysis_service.py:41 — revisar facet 'não imprime side-effects na UI/IO' em test_metrics_service
06376. [x] tests\test_analysis_service.py:41 — revisar facet 'thread-safety revisada' em test_metrics_service
06377. [x] tests\test_analysis_service.py:41 — revisar facet 'performance (sem loops O(n^2))' em test_metrics_service
06378. [x] tests\test_analysis_service.py:41 — revisar facet 'coberto por testes' em test_metrics_service
06379. [x] tests\test_analysis_service.py:43 — atribuição: test_metrics_service ← summary
06380. [x] tests\test_analysis_service.py:50 — atribuição: test_metrics_service ← per_batch
06381. [x] tests\test_analysis_service.py:54 — definir/revisar FunctionDef: test_preview_service_scales
06382. [x] tests\test_analysis_service.py:54 — revisar facet 'assinatura/args consistentes' em test_preview_service_scales
06383. [x] tests\test_analysis_service.py:54 — revisar facet 'docstring em português' em test_preview_service_scales
06384. [x] tests\test_analysis_service.py:54 — revisar facet 'nomenclatura clara (PEP8)' em test_preview_service_scales
06385. [x] tests\test_analysis_service.py:54 — revisar facet 'type hints presentes' em test_preview_service_scales
06386. [x] tests\test_analysis_service.py:54 — revisar facet 'tratamento de erros adequado' em test_preview_service_scales
06387. [x] tests\test_analysis_service.py:54 — revisar facet 'sem comentários inline desnecessários' em test_preview_service_scales
06388. [x] tests\test_analysis_service.py:54 — revisar facet 'não imprime side-effects na UI/IO' em test_preview_service_scales
06389. [x] tests\test_analysis_service.py:54 — revisar facet 'thread-safety revisada' em test_preview_service_scales
06390. [x] tests\test_analysis_service.py:54 — revisar facet 'performance (sem loops O(n^2))' em test_preview_service_scales
06391. [x] tests\test_analysis_service.py:54 — revisar facet 'coberto por testes' em test_preview_service_scales
06392. [x] tests\test_analysis_service.py:55 — import: app.services.preview_service
06393. [x] tests\test_analysis_service.py:57 — atribuição: test_preview_service_scales ← svc
06394. [x] tests\test_analysis_service.py:58 — atribuição: test_preview_service_scales ← specs
06395. [x] tests\test_analysis_service.py:63 — atribuição: test_preview_service_scales ← values
06396. [x] tests\test_analysis_service.py:65 — atribuição: test_preview_service_scales ← text
06397. [x] Existência e estrutura do módulo: tests\test_api_server.py
06398. [x] tests\test_api_server.py:3 — import: json
06399. [x] tests\test_api_server.py:4 — import: threading
06400. [x] tests\test_api_server.py:5 — import: urllib.error
06401. [x] tests\test_api_server.py:6 — import: urllib.request
06402. [x] tests\test_api_server.py:9 — definir/revisar FunctionDef: _get
06403. [x] tests\test_api_server.py:9 — revisar facet 'assinatura/args consistentes' em _get
06404. [x] tests\test_api_server.py:9 — revisar facet 'docstring em português' em _get
06405. [x] tests\test_api_server.py:9 — revisar facet 'nomenclatura clara (PEP8)' em _get
06406. [x] tests\test_api_server.py:9 — revisar facet 'type hints presentes' em _get
06407. [x] tests\test_api_server.py:9 — revisar facet 'tratamento de erros adequado' em _get
06408. [x] tests\test_api_server.py:9 — revisar facet 'sem comentários inline desnecessários' em _get
06409. [x] tests\test_api_server.py:9 — revisar facet 'não imprime side-effects na UI/IO' em _get
06410. [x] tests\test_api_server.py:9 — revisar facet 'thread-safety revisada' em _get
06411. [x] tests\test_api_server.py:9 — revisar facet 'performance (sem loops O(n^2))' em _get
06412. [x] tests\test_api_server.py:9 — revisar facet 'coberto por testes' em _get
06413. [x] tests\test_api_server.py:10 — try em _get
06414. [x] tests\test_api_server.py:11 — controle with em _get
06415. [x] tests\test_api_server.py:12 — return em _get
06416. [x] tests\test_api_server.py:14 — return em _get
06417. [x] tests\test_api_server.py:17 — definir/revisar FunctionDef: _start_api
06418. [x] tests\test_api_server.py:17 — revisar facet 'assinatura/args consistentes' em _start_api
06419. [x] tests\test_api_server.py:17 — revisar facet 'docstring em português' em _start_api
06420. [x] tests\test_api_server.py:17 — revisar facet 'nomenclatura clara (PEP8)' em _start_api
06421. [x] tests\test_api_server.py:17 — revisar facet 'type hints presentes' em _start_api
06422. [x] tests\test_api_server.py:17 — revisar facet 'tratamento de erros adequado' em _start_api
06423. [x] tests\test_api_server.py:17 — revisar facet 'sem comentários inline desnecessários' em _start_api
06424. [x] tests\test_api_server.py:17 — revisar facet 'não imprime side-effects na UI/IO' em _start_api
06425. [x] tests\test_api_server.py:17 — revisar facet 'thread-safety revisada' em _start_api
06426. [x] tests\test_api_server.py:17 — revisar facet 'performance (sem loops O(n^2))' em _start_api
06427. [x] tests\test_api_server.py:17 — revisar facet 'coberto por testes' em _start_api
06428. [x] tests\test_api_server.py:18 — import: app.infrastructure.api.routes
06429. [x] tests\test_api_server.py:19 — import: app.infrastructure.api.server
06430. [x] tests\test_api_server.py:21 — atribuição: _start_api ← server
06431. [x] tests\test_api_server.py:24 — return em _start_api
06432. [x] tests\test_api_server.py:27 — definir/revisar FunctionDef: test_api_health_and_batches
06433. [x] tests\test_api_server.py:27 — revisar facet 'assinatura/args consistentes' em test_api_health_and_batches
06434. [x] tests\test_api_server.py:27 — revisar facet 'docstring em português' em test_api_health_and_batches
06435. [x] tests\test_api_server.py:27 — revisar facet 'nomenclatura clara (PEP8)' em test_api_health_and_batches
06436. [x] tests\test_api_server.py:27 — revisar facet 'type hints presentes' em test_api_health_and_batches
06437. [x] tests\test_api_server.py:27 — revisar facet 'tratamento de erros adequado' em test_api_health_and_batches
06438. [x] tests\test_api_server.py:27 — revisar facet 'sem comentários inline desnecessários' em test_api_health_and_batches
06439. [x] tests\test_api_server.py:27 — revisar facet 'não imprime side-effects na UI/IO' em test_api_health_and_batches
06440. [x] tests\test_api_server.py:27 — revisar facet 'thread-safety revisada' em test_api_health_and_batches
06441. [x] tests\test_api_server.py:27 — revisar facet 'performance (sem loops O(n^2))' em test_api_health_and_batches
06442. [x] tests\test_api_server.py:27 — revisar facet 'coberto por testes' em test_api_health_and_batches
06443. [x] tests\test_api_server.py:28 — atribuição: test_api_health_and_batches ← server
06444. [x] tests\test_api_server.py:29 — try em test_api_health_and_batches
06445. [x] tests\test_api_server.py:30 — atribuição: test_api_health_and_batches ← base
06446. [x] tests\test_api_server.py:32 — atribuição: test_api_health_and_batches ← ?
06447. [x] tests\test_api_server.py:37 — atribuição: test_api_health_and_batches ← ?
06448. [x] tests\test_api_server.py:39 — atribuição: test_api_health_and_batches ← ids
06449. [x] tests\test_api_server.py:42 — atribuição: test_api_health_and_batches ← ?
06450. [x] tests\test_api_server.py:49 — definir/revisar FunctionDef: test_api_experiments_pagination
06451. [x] tests\test_api_server.py:49 — revisar facet 'assinatura/args consistentes' em test_api_experiments_pagination
06452. [x] tests\test_api_server.py:49 — revisar facet 'docstring em português' em test_api_experiments_pagination
06453. [x] tests\test_api_server.py:49 — revisar facet 'nomenclatura clara (PEP8)' em test_api_experiments_pagination
06454. [x] tests\test_api_server.py:49 — revisar facet 'type hints presentes' em test_api_experiments_pagination
06455. [x] tests\test_api_server.py:49 — revisar facet 'tratamento de erros adequado' em test_api_experiments_pagination
06456. [x] tests\test_api_server.py:49 — revisar facet 'sem comentários inline desnecessários' em test_api_experiments_pagination
06457. [x] tests\test_api_server.py:49 — revisar facet 'não imprime side-effects na UI/IO' em test_api_experiments_pagination
06458. [x] tests\test_api_server.py:49 — revisar facet 'thread-safety revisada' em test_api_experiments_pagination
06459. [x] tests\test_api_server.py:49 — revisar facet 'performance (sem loops O(n^2))' em test_api_experiments_pagination
06460. [x] tests\test_api_server.py:49 — revisar facet 'coberto por testes' em test_api_experiments_pagination
06461. [x] tests\test_api_server.py:50 — atribuição: test_api_experiments_pagination ← server
06462. [x] tests\test_api_server.py:51 — try em test_api_experiments_pagination
06463. [x] tests\test_api_server.py:52 — atribuição: test_api_experiments_pagination ← base
06464. [x] tests\test_api_server.py:54 — atribuição: test_api_experiments_pagination ← ?
06465. [x] tests\test_api_server.py:57 — atribuição: test_api_experiments_pagination ← first
06466. [x] tests\test_api_server.py:61 — atribuição: test_api_experiments_pagination ← ?
06467. [x] tests\test_api_server.py:68 — definir/revisar FunctionDef: test_api_stats_and_templates
06468. [x] tests\test_api_server.py:68 — revisar facet 'assinatura/args consistentes' em test_api_stats_and_templates
06469. [x] tests\test_api_server.py:68 — revisar facet 'docstring em português' em test_api_stats_and_templates
06470. [x] tests\test_api_server.py:68 — revisar facet 'nomenclatura clara (PEP8)' em test_api_stats_and_templates
06471. [x] tests\test_api_server.py:68 — revisar facet 'type hints presentes' em test_api_stats_and_templates
06472. [x] tests\test_api_server.py:68 — revisar facet 'tratamento de erros adequado' em test_api_stats_and_templates
06473. [x] tests\test_api_server.py:68 — revisar facet 'sem comentários inline desnecessários' em test_api_stats_and_templates
06474. [x] tests\test_api_server.py:68 — revisar facet 'não imprime side-effects na UI/IO' em test_api_stats_and_templates
06475. [x] tests\test_api_server.py:68 — revisar facet 'thread-safety revisada' em test_api_stats_and_templates
06476. [x] tests\test_api_server.py:68 — revisar facet 'performance (sem loops O(n^2))' em test_api_stats_and_templates
06477. [x] tests\test_api_server.py:68 — revisar facet 'coberto por testes' em test_api_stats_and_templates
06478. [x] tests\test_api_server.py:69 — atribuição: test_api_stats_and_templates ← server
06479. [x] tests\test_api_server.py:70 — try em test_api_stats_and_templates
06480. [x] tests\test_api_server.py:71 — atribuição: test_api_stats_and_templates ← base
06481. [x] tests\test_api_server.py:73 — atribuição: test_api_stats_and_templates ← ?
06482. [x] tests\test_api_server.py:78 — atribuição: test_api_stats_and_templates ← ?
06483. [x] tests\test_api_server.py:80 — atribuição: test_api_stats_and_templates ← template_id
06484. [x] tests\test_api_server.py:82 — atribuição: test_api_stats_and_templates ← ?
06485. [x] tests\test_api_server.py:89 — definir/revisar FunctionDef: test_api_unknown_batch_404
06486. [x] tests\test_api_server.py:89 — revisar facet 'assinatura/args consistentes' em test_api_unknown_batch_404
06487. [x] tests\test_api_server.py:89 — revisar facet 'docstring em português' em test_api_unknown_batch_404
06488. [x] tests\test_api_server.py:89 — revisar facet 'nomenclatura clara (PEP8)' em test_api_unknown_batch_404
06489. [x] tests\test_api_server.py:89 — revisar facet 'type hints presentes' em test_api_unknown_batch_404
06490. [x] tests\test_api_server.py:89 — revisar facet 'tratamento de erros adequado' em test_api_unknown_batch_404
06491. [x] tests\test_api_server.py:89 — revisar facet 'sem comentários inline desnecessários' em test_api_unknown_batch_404
06492. [x] tests\test_api_server.py:89 — revisar facet 'não imprime side-effects na UI/IO' em test_api_unknown_batch_404
06493. [x] tests\test_api_server.py:89 — revisar facet 'thread-safety revisada' em test_api_unknown_batch_404
06494. [x] tests\test_api_server.py:89 — revisar facet 'performance (sem loops O(n^2))' em test_api_unknown_batch_404
06495. [x] tests\test_api_server.py:89 — revisar facet 'coberto por testes' em test_api_unknown_batch_404
06496. [x] tests\test_api_server.py:90 — atribuição: test_api_unknown_batch_404 ← server
06497. [x] tests\test_api_server.py:91 — try em test_api_unknown_batch_404
06498. [x] tests\test_api_server.py:92 — atribuição: test_api_unknown_batch_404 ← ?
06499. [x] Existência e estrutura do módulo: tests\test_batch_export_service.py
06500. [x] tests\test_batch_export_service.py:3 — import: pathlib
06501. [x] tests\test_batch_export_service.py:6 — definir/revisar FunctionDef: test_export_all_files_and_manifest
06502. [x] tests\test_batch_export_service.py:6 — revisar facet 'assinatura/args consistentes' em test_export_all_files_and_manifest
06503. [x] tests\test_batch_export_service.py:6 — revisar facet 'docstring em português' em test_export_all_files_and_manifest
06504. [x] tests\test_batch_export_service.py:6 — revisar facet 'nomenclatura clara (PEP8)' em test_export_all_files_and_manifest
06505. [x] tests\test_batch_export_service.py:6 — revisar facet 'type hints presentes' em test_export_all_files_and_manifest
06506. [x] tests\test_batch_export_service.py:6 — revisar facet 'tratamento de erros adequado' em test_export_all_files_and_manifest
06507. [x] tests\test_batch_export_service.py:6 — revisar facet 'sem comentários inline desnecessários' em test_export_all_files_and_manifest
06508. [x] tests\test_batch_export_service.py:6 — revisar facet 'não imprime side-effects na UI/IO' em test_export_all_files_and_manifest
06509. [x] tests\test_batch_export_service.py:6 — revisar facet 'thread-safety revisada' em test_export_all_files_and_manifest
06510. [x] tests\test_batch_export_service.py:6 — revisar facet 'performance (sem loops O(n^2))' em test_export_all_files_and_manifest
06511. [x] tests\test_batch_export_service.py:6 — revisar facet 'coberto por testes' em test_export_all_files_and_manifest
06512. [x] tests\test_batch_export_service.py:7 — atribuição: test_export_all_files_and_manifest ← out_root
06513. [x] tests\test_batch_export_service.py:8 — atribuição: test_export_all_files_and_manifest ← manifest
06514. [x] tests\test_batch_export_service.py:13 — atribuição: test_export_all_files_and_manifest ← files
06515. [x] tests\test_batch_export_service.py:16 — atribuição: test_export_all_files_and_manifest ← manifest_file
06516. [x] tests\test_batch_export_service.py:18 — atribuição: test_export_all_files_and_manifest ← contents
06517. [x] tests\test_batch_export_service.py:22 — definir/revisar FunctionDef: test_export_checkpoint_can_resume
06518. [x] tests\test_batch_export_service.py:22 — revisar facet 'assinatura/args consistentes' em test_export_checkpoint_can_resume
06519. [x] tests\test_batch_export_service.py:22 — revisar facet 'docstring em português' em test_export_checkpoint_can_resume
06520. [x] tests\test_batch_export_service.py:22 — revisar facet 'nomenclatura clara (PEP8)' em test_export_checkpoint_can_resume
06521. [x] tests\test_batch_export_service.py:22 — revisar facet 'type hints presentes' em test_export_checkpoint_can_resume
06522. [x] tests\test_batch_export_service.py:22 — revisar facet 'tratamento de erros adequado' em test_export_checkpoint_can_resume
06523. [x] tests\test_batch_export_service.py:22 — revisar facet 'sem comentários inline desnecessários' em test_export_checkpoint_can_resume
06524. [x] tests\test_batch_export_service.py:22 — revisar facet 'não imprime side-effects na UI/IO' em test_export_checkpoint_can_resume
06525. [x] tests\test_batch_export_service.py:22 — revisar facet 'thread-safety revisada' em test_export_checkpoint_can_resume
06526. [x] tests\test_batch_export_service.py:22 — revisar facet 'performance (sem loops O(n^2))' em test_export_checkpoint_can_resume
06527. [x] tests\test_batch_export_service.py:22 — revisar facet 'coberto por testes' em test_export_checkpoint_can_resume
06528. [x] tests\test_batch_export_service.py:23 — atribuição: test_export_checkpoint_can_resume ← captured_checkpoints
06529. [x] tests\test_batch_export_service.py:25 — atribuição: test_export_checkpoint_can_resume ← manifest
06530. [x] tests\test_batch_export_service.py:32 — atribuição: test_export_checkpoint_can_resume ← last_id
06531. [x] tests\test_batch_export_service.py:34 — atribuição: test_export_checkpoint_can_resume ← second
06532. [x] tests\test_batch_export_service.py:40 — atribuição: test_export_checkpoint_can_resume ← names_full
06533. [x] tests\test_batch_export_service.py:41 — atribuição: test_export_checkpoint_can_resume ← names_resume
06534. [x] tests\test_batch_export_service.py:46 — definir/revisar FunctionDef: test_export_stop_check
06535. [x] tests\test_batch_export_service.py:46 — revisar facet 'assinatura/args consistentes' em test_export_stop_check
06536. [x] tests\test_batch_export_service.py:46 — revisar facet 'docstring em português' em test_export_stop_check
06537. [x] tests\test_batch_export_service.py:46 — revisar facet 'nomenclatura clara (PEP8)' em test_export_stop_check
06538. [x] tests\test_batch_export_service.py:46 — revisar facet 'type hints presentes' em test_export_stop_check
06539. [x] tests\test_batch_export_service.py:46 — revisar facet 'tratamento de erros adequado' em test_export_stop_check
06540. [x] tests\test_batch_export_service.py:46 — revisar facet 'sem comentários inline desnecessários' em test_export_stop_check
06541. [x] tests\test_batch_export_service.py:46 — revisar facet 'não imprime side-effects na UI/IO' em test_export_stop_check
06542. [x] tests\test_batch_export_service.py:46 — revisar facet 'thread-safety revisada' em test_export_stop_check
06543. [x] tests\test_batch_export_service.py:46 — revisar facet 'performance (sem loops O(n^2))' em test_export_stop_check
06544. [x] tests\test_batch_export_service.py:46 — revisar facet 'coberto por testes' em test_export_stop_check
06545. [x] tests\test_batch_export_service.py:47 — atribuição: test_export_stop_check ← calls
06546. [x] tests\test_batch_export_service.py:49 — definir/revisar FunctionDef: test_export_stop_check.stop
06547. [x] tests\test_batch_export_service.py:49 — revisar facet 'assinatura/args consistentes' em test_export_stop_check.stop
06548. [x] tests\test_batch_export_service.py:49 — revisar facet 'docstring em português' em test_export_stop_check.stop
06549. [x] tests\test_batch_export_service.py:49 — revisar facet 'nomenclatura clara (PEP8)' em test_export_stop_check.stop
06550. [x] tests\test_batch_export_service.py:49 — revisar facet 'type hints presentes' em test_export_stop_check.stop
06551. [x] tests\test_batch_export_service.py:49 — revisar facet 'tratamento de erros adequado' em test_export_stop_check.stop
06552. [x] tests\test_batch_export_service.py:49 — revisar facet 'sem comentários inline desnecessários' em test_export_stop_check.stop
06553. [x] tests\test_batch_export_service.py:49 — revisar facet 'não imprime side-effects na UI/IO' em test_export_stop_check.stop
06554. [x] tests\test_batch_export_service.py:49 — revisar facet 'thread-safety revisada' em test_export_stop_check.stop
06555. [x] tests\test_batch_export_service.py:49 — revisar facet 'performance (sem loops O(n^2))' em test_export_stop_check.stop
06556. [x] tests\test_batch_export_service.py:49 — revisar facet 'coberto por testes' em test_export_stop_check.stop
06557. [x] tests\test_batch_export_service.py:51 — return em test_export_stop_check.stop
06558. [x] tests\test_batch_export_service.py:53 — import: pytest
06559. [x] tests\test_batch_export_service.py:55 — controle with em test_export_stop_check
06560. [x] tests\test_batch_export_service.py:62 — definir/revisar FunctionDef: test_export_raises_for_missing_version
06561. [x] tests\test_batch_export_service.py:62 — revisar facet 'assinatura/args consistentes' em test_export_raises_for_missing_version
06562. [x] tests\test_batch_export_service.py:62 — revisar facet 'docstring em português' em test_export_raises_for_missing_version
06563. [x] tests\test_batch_export_service.py:62 — revisar facet 'nomenclatura clara (PEP8)' em test_export_raises_for_missing_version
06564. [x] tests\test_batch_export_service.py:62 — revisar facet 'type hints presentes' em test_export_raises_for_missing_version
06565. [x] tests\test_batch_export_service.py:62 — revisar facet 'tratamento de erros adequado' em test_export_raises_for_missing_version
06566. [x] tests\test_batch_export_service.py:62 — revisar facet 'sem comentários inline desnecessários' em test_export_raises_for_missing_version
06567. [x] tests\test_batch_export_service.py:62 — revisar facet 'não imprime side-effects na UI/IO' em test_export_raises_for_missing_version
06568. [x] tests\test_batch_export_service.py:62 — revisar facet 'thread-safety revisada' em test_export_raises_for_missing_version
06569. [x] tests\test_batch_export_service.py:62 — revisar facet 'performance (sem loops O(n^2))' em test_export_raises_for_missing_version
06570. [x] tests\test_batch_export_service.py:62 — revisar facet 'coberto por testes' em test_export_raises_for_missing_version
06571. [x] tests\test_batch_export_service.py:63 — import: pytest
06572. [x] tests\test_batch_export_service.py:65 — controle with em test_export_raises_for_missing_version
06573. [x] tests\test_batch_export_service.py:69 — definir/revisar FunctionDef: test_export_empty_batch_raises
06574. [x] tests\test_batch_export_service.py:69 — revisar facet 'assinatura/args consistentes' em test_export_empty_batch_raises
06575. [x] tests\test_batch_export_service.py:69 — revisar facet 'docstring em português' em test_export_empty_batch_raises
06576. [x] tests\test_batch_export_service.py:69 — revisar facet 'nomenclatura clara (PEP8)' em test_export_empty_batch_raises
06577. [x] tests\test_batch_export_service.py:69 — revisar facet 'type hints presentes' em test_export_empty_batch_raises
06578. [x] tests\test_batch_export_service.py:69 — revisar facet 'tratamento de erros adequado' em test_export_empty_batch_raises
06579. [x] tests\test_batch_export_service.py:69 — revisar facet 'sem comentários inline desnecessários' em test_export_empty_batch_raises
06580. [x] tests\test_batch_export_service.py:69 — revisar facet 'não imprime side-effects na UI/IO' em test_export_empty_batch_raises
06581. [x] tests\test_batch_export_service.py:69 — revisar facet 'thread-safety revisada' em test_export_empty_batch_raises
06582. [x] tests\test_batch_export_service.py:69 — revisar facet 'performance (sem loops O(n^2))' em test_export_empty_batch_raises
06583. [x] tests\test_batch_export_service.py:69 — revisar facet 'coberto por testes' em test_export_empty_batch_raises
06584. [x] tests\test_batch_export_service.py:70 — import: pytest
06585. [x] tests\test_batch_export_service.py:73 — atribuição: test_export_empty_batch_raises ← vid
06586. [x] tests\test_batch_export_service.py:74 — controle with em test_export_empty_batch_raises
06587. [x] Existência e estrutura do módulo: tests\test_distribution_registry.py
06588. [x] tests\test_distribution_registry.py:3 — import: pytest
06589. [x] tests\test_distribution_registry.py:5 — import: numpy
06590. [x] tests\test_distribution_registry.py:7 — import: app.domain.entities
06591. [x] tests\test_distribution_registry.py:10 — definir/revisar FunctionDef: test_scipy_list_distributions
06592. [x] tests\test_distribution_registry.py:10 — revisar facet 'assinatura/args consistentes' em test_scipy_list_distributions
06593. [x] tests\test_distribution_registry.py:10 — revisar facet 'docstring em português' em test_scipy_list_distributions
06594. [x] tests\test_distribution_registry.py:10 — revisar facet 'nomenclatura clara (PEP8)' em test_scipy_list_distributions
06595. [x] tests\test_distribution_registry.py:10 — revisar facet 'type hints presentes' em test_scipy_list_distributions
06596. [x] tests\test_distribution_registry.py:10 — revisar facet 'tratamento de erros adequado' em test_scipy_list_distributions
06597. [x] tests\test_distribution_registry.py:10 — revisar facet 'sem comentários inline desnecessários' em test_scipy_list_distributions
06598. [x] tests\test_distribution_registry.py:10 — revisar facet 'não imprime side-effects na UI/IO' em test_scipy_list_distributions
06599. [x] tests\test_distribution_registry.py:10 — revisar facet 'thread-safety revisada' em test_scipy_list_distributions
06600. [x] tests\test_distribution_registry.py:10 — revisar facet 'performance (sem loops O(n^2))' em test_scipy_list_distributions
06601. [x] tests\test_distribution_registry.py:10 — revisar facet 'coberto por testes' em test_scipy_list_distributions
06602. [x] tests\test_distribution_registry.py:11 — atribuição: test_scipy_list_distributions ← provider
06603. [x] tests\test_distribution_registry.py:12 — atribuição: test_scipy_list_distributions ← names
06604. [x] tests\test_distribution_registry.py:16 — definir/revisar FunctionDef: test_scipy_parameter_names
06605. [x] tests\test_distribution_registry.py:16 — revisar facet 'assinatura/args consistentes' em test_scipy_parameter_names
06606. [x] tests\test_distribution_registry.py:16 — revisar facet 'docstring em português' em test_scipy_parameter_names
06607. [x] tests\test_distribution_registry.py:16 — revisar facet 'nomenclatura clara (PEP8)' em test_scipy_parameter_names
06608. [x] tests\test_distribution_registry.py:16 — revisar facet 'type hints presentes' em test_scipy_parameter_names
06609. [x] tests\test_distribution_registry.py:16 — revisar facet 'tratamento de erros adequado' em test_scipy_parameter_names
06610. [x] tests\test_distribution_registry.py:16 — revisar facet 'sem comentários inline desnecessários' em test_scipy_parameter_names
06611. [x] tests\test_distribution_registry.py:16 — revisar facet 'não imprime side-effects na UI/IO' em test_scipy_parameter_names
06612. [x] tests\test_distribution_registry.py:16 — revisar facet 'thread-safety revisada' em test_scipy_parameter_names
06613. [x] tests\test_distribution_registry.py:16 — revisar facet 'performance (sem loops O(n^2))' em test_scipy_parameter_names
06614. [x] tests\test_distribution_registry.py:16 — revisar facet 'coberto por testes' em test_scipy_parameter_names
06615. [x] tests\test_distribution_registry.py:17 — atribuição: test_scipy_parameter_names ← provider
06616. [x] tests\test_distribution_registry.py:19 — atribuição: test_scipy_parameter_names ← triang
06617. [x] tests\test_distribution_registry.py:23 — definir/revisar FunctionDef: test_fixed_sample
06618. [x] tests\test_distribution_registry.py:23 — revisar facet 'assinatura/args consistentes' em test_fixed_sample
06619. [x] tests\test_distribution_registry.py:23 — revisar facet 'docstring em português' em test_fixed_sample
06620. [x] tests\test_distribution_registry.py:23 — revisar facet 'nomenclatura clara (PEP8)' em test_fixed_sample
06621. [x] tests\test_distribution_registry.py:23 — revisar facet 'type hints presentes' em test_fixed_sample
06622. [x] tests\test_distribution_registry.py:23 — revisar facet 'tratamento de erros adequado' em test_fixed_sample
06623. [x] tests\test_distribution_registry.py:23 — revisar facet 'sem comentários inline desnecessários' em test_fixed_sample
06624. [x] tests\test_distribution_registry.py:23 — revisar facet 'não imprime side-effects na UI/IO' em test_fixed_sample
06625. [x] tests\test_distribution_registry.py:23 — revisar facet 'thread-safety revisada' em test_fixed_sample
06626. [x] tests\test_distribution_registry.py:23 — revisar facet 'performance (sem loops O(n^2))' em test_fixed_sample
06627. [x] tests\test_distribution_registry.py:23 — revisar facet 'coberto por testes' em test_fixed_sample
06628. [x] tests\test_distribution_registry.py:24 — atribuição: test_fixed_sample ← provider
06629. [x] tests\test_distribution_registry.py:25 — atribuição: test_fixed_sample ← spec
06630. [x] tests\test_distribution_registry.py:26 — atribuição: test_fixed_sample ← values
06631. [x] tests\test_distribution_registry.py:30 — definir/revisar FunctionDef: test_fixed_validate
06632. [x] tests\test_distribution_registry.py:30 — revisar facet 'assinatura/args consistentes' em test_fixed_validate
06633. [x] tests\test_distribution_registry.py:30 — revisar facet 'docstring em português' em test_fixed_validate
06634. [x] tests\test_distribution_registry.py:30 — revisar facet 'nomenclatura clara (PEP8)' em test_fixed_validate
06635. [x] tests\test_distribution_registry.py:30 — revisar facet 'type hints presentes' em test_fixed_validate
06636. [x] tests\test_distribution_registry.py:30 — revisar facet 'tratamento de erros adequado' em test_fixed_validate
06637. [x] tests\test_distribution_registry.py:30 — revisar facet 'sem comentários inline desnecessários' em test_fixed_validate
06638. [x] tests\test_distribution_registry.py:30 — revisar facet 'não imprime side-effects na UI/IO' em test_fixed_validate
06639. [x] tests\test_distribution_registry.py:30 — revisar facet 'thread-safety revisada' em test_fixed_validate
06640. [x] tests\test_distribution_registry.py:30 — revisar facet 'performance (sem loops O(n^2))' em test_fixed_validate
06641. [x] tests\test_distribution_registry.py:30 — revisar facet 'coberto por testes' em test_fixed_validate
06642. [x] tests\test_distribution_registry.py:31 — atribuição: test_fixed_validate ← spec
06643. [x] tests\test_distribution_registry.py:35 — definir/revisar FunctionDef: test_scipy_validate
06644. [x] tests\test_distribution_registry.py:35 — revisar facet 'assinatura/args consistentes' em test_scipy_validate
06645. [x] tests\test_distribution_registry.py:35 — revisar facet 'docstring em português' em test_scipy_validate
06646. [x] tests\test_distribution_registry.py:35 — revisar facet 'nomenclatura clara (PEP8)' em test_scipy_validate
06647. [x] tests\test_distribution_registry.py:35 — revisar facet 'type hints presentes' em test_scipy_validate
06648. [x] tests\test_distribution_registry.py:35 — revisar facet 'tratamento de erros adequado' em test_scipy_validate
06649. [x] tests\test_distribution_registry.py:35 — revisar facet 'sem comentários inline desnecessários' em test_scipy_validate
06650. [x] tests\test_distribution_registry.py:35 — revisar facet 'não imprime side-effects na UI/IO' em test_scipy_validate
06651. [x] tests\test_distribution_registry.py:35 — revisar facet 'thread-safety revisada' em test_scipy_validate
06652. [x] tests\test_distribution_registry.py:35 — revisar facet 'performance (sem loops O(n^2))' em test_scipy_validate
06653. [x] tests\test_distribution_registry.py:35 — revisar facet 'coberto por testes' em test_scipy_validate
06654. [x] tests\test_distribution_registry.py:36 — atribuição: test_scipy_validate ← spec
06655. [x] tests\test_distribution_registry.py:40 — definir/revisar FunctionDef: test_registry_get_unknown
06656. [x] tests\test_distribution_registry.py:40 — revisar facet 'assinatura/args consistentes' em test_registry_get_unknown
06657. [x] tests\test_distribution_registry.py:40 — revisar facet 'docstring em português' em test_registry_get_unknown
06658. [x] tests\test_distribution_registry.py:40 — revisar facet 'nomenclatura clara (PEP8)' em test_registry_get_unknown
06659. [x] tests\test_distribution_registry.py:40 — revisar facet 'type hints presentes' em test_registry_get_unknown
06660. [x] tests\test_distribution_registry.py:40 — revisar facet 'tratamento de erros adequado' em test_registry_get_unknown
06661. [x] tests\test_distribution_registry.py:40 — revisar facet 'sem comentários inline desnecessários' em test_registry_get_unknown
06662. [x] tests\test_distribution_registry.py:40 — revisar facet 'não imprime side-effects na UI/IO' em test_registry_get_unknown
06663. [x] tests\test_distribution_registry.py:40 — revisar facet 'thread-safety revisada' em test_registry_get_unknown
06664. [x] tests\test_distribution_registry.py:40 — revisar facet 'performance (sem loops O(n^2))' em test_registry_get_unknown
06665. [x] tests\test_distribution_registry.py:40 — revisar facet 'coberto por testes' em test_registry_get_unknown
06666. [x] tests\test_distribution_registry.py:41 — import: app.infrastructure.distribution_registry
06667. [x] tests\test_distribution_registry.py:43 — atribuição: test_registry_get_unknown ← r
06668. [x] tests\test_distribution_registry.py:45 — controle with em test_registry_get_unknown
06669. [x] tests\test_distribution_registry.py:49 — definir/revisar FunctionDef: test_plugin_loader_registers_provider
06670. [x] tests\test_distribution_registry.py:49 — revisar facet 'assinatura/args consistentes' em test_plugin_loader_registers_provider
06671. [x] tests\test_distribution_registry.py:49 — revisar facet 'docstring em português' em test_plugin_loader_registers_provider
06672. [x] tests\test_distribution_registry.py:49 — revisar facet 'nomenclatura clara (PEP8)' em test_plugin_loader_registers_provider
06673. [x] tests\test_distribution_registry.py:49 — revisar facet 'type hints presentes' em test_plugin_loader_registers_provider
06674. [x] tests\test_distribution_registry.py:49 — revisar facet 'tratamento de erros adequado' em test_plugin_loader_registers_provider
06675. [x] tests\test_distribution_registry.py:49 — revisar facet 'sem comentários inline desnecessários' em test_plugin_loader_registers_provider
06676. [x] tests\test_distribution_registry.py:49 — revisar facet 'não imprime side-effects na UI/IO' em test_plugin_loader_registers_provider
06677. [x] tests\test_distribution_registry.py:49 — revisar facet 'thread-safety revisada' em test_plugin_loader_registers_provider
06678. [x] tests\test_distribution_registry.py:49 — revisar facet 'performance (sem loops O(n^2))' em test_plugin_loader_registers_provider
06679. [x] tests\test_distribution_registry.py:49 — revisar facet 'coberto por testes' em test_plugin_loader_registers_provider
06680. [x] tests\test_distribution_registry.py:50 — import: app.infrastructure.plugins.loader
06681. [x] tests\test_distribution_registry.py:52 — atribuição: test_plugin_loader_registers_provider ← plugin_code
06682. [x] tests\test_distribution_registry.py:76 — atribuição: test_plugin_loader_registers_provider ← dir_path
06683. [x] tests\test_distribution_registry.py:81 — atribuição: test_plugin_loader_registers_provider ← loader
06684. [x] tests\test_distribution_registry.py:82 — atribuição: test_plugin_loader_registers_provider ← report
06685. [x] tests\test_distribution_registry.py:86 — atribuição: test_plugin_loader_registers_provider ← provider
06686. [x] tests\test_distribution_registry.py:87 — atribuição: test_plugin_loader_registers_provider ← spec
06687. [x] tests\test_distribution_registry.py:91 — definir/revisar FunctionDef: test_plugin_loader_reports_failure
06688. [x] tests\test_distribution_registry.py:91 — revisar facet 'assinatura/args consistentes' em test_plugin_loader_reports_failure
06689. [x] tests\test_distribution_registry.py:91 — revisar facet 'docstring em português' em test_plugin_loader_reports_failure
06690. [x] tests\test_distribution_registry.py:91 — revisar facet 'nomenclatura clara (PEP8)' em test_plugin_loader_reports_failure
06691. [x] tests\test_distribution_registry.py:91 — revisar facet 'type hints presentes' em test_plugin_loader_reports_failure
06692. [x] tests\test_distribution_registry.py:91 — revisar facet 'tratamento de erros adequado' em test_plugin_loader_reports_failure
06693. [x] tests\test_distribution_registry.py:91 — revisar facet 'sem comentários inline desnecessários' em test_plugin_loader_reports_failure
06694. [x] tests\test_distribution_registry.py:91 — revisar facet 'não imprime side-effects na UI/IO' em test_plugin_loader_reports_failure
06695. [x] tests\test_distribution_registry.py:91 — revisar facet 'thread-safety revisada' em test_plugin_loader_reports_failure
06696. [x] tests\test_distribution_registry.py:91 — revisar facet 'performance (sem loops O(n^2))' em test_plugin_loader_reports_failure
06697. [x] tests\test_distribution_registry.py:91 — revisar facet 'coberto por testes' em test_plugin_loader_reports_failure
06698. [x] tests\test_distribution_registry.py:92 — import: app.infrastructure.plugins.loader
06699. [x] tests\test_distribution_registry.py:94 — atribuição: test_plugin_loader_reports_failure ← dir_path
06700. [x] tests\test_distribution_registry.py:98 — import: app.infrastructure.distribution_registry
06701. [x] tests\test_distribution_registry.py:100 — atribuição: test_plugin_loader_reports_failure ← loader
06702. [x] tests\test_distribution_registry.py:101 — atribuição: test_plugin_loader_reports_failure ← report
06703. [x] Existência e estrutura do módulo: tests\test_font_zoom.py
06704. [x] tests\test_font_zoom.py:3 — import: os
06705. [x] tests\test_font_zoom.py:5 — import: pytest
06706. [x] tests\test_font_zoom.py:6 — import: PySide6.QtCore
06707. [x] tests\test_font_zoom.py:7 — import: PySide6.QtGui
06708. [x] tests\test_font_zoom.py:9 — import: app.ui.editor.themes
06709. [x] tests\test_font_zoom.py:13 — definir/revisar FunctionDef: _reset_scale
06710. [x] tests\test_font_zoom.py:13 — revisar facet 'assinatura/args consistentes' em _reset_scale
06711. [x] tests\test_font_zoom.py:13 — revisar facet 'docstring em português' em _reset_scale
06712. [x] tests\test_font_zoom.py:13 — revisar facet 'nomenclatura clara (PEP8)' em _reset_scale
06713. [x] tests\test_font_zoom.py:13 — revisar facet 'type hints presentes' em _reset_scale
06714. [x] tests\test_font_zoom.py:13 — revisar facet 'tratamento de erros adequado' em _reset_scale
06715. [x] tests\test_font_zoom.py:13 — revisar facet 'sem comentários inline desnecessários' em _reset_scale
06716. [x] tests\test_font_zoom.py:13 — revisar facet 'não imprime side-effects na UI/IO' em _reset_scale
06717. [x] tests\test_font_zoom.py:13 — revisar facet 'thread-safety revisada' em _reset_scale
06718. [x] tests\test_font_zoom.py:13 — revisar facet 'performance (sem loops O(n^2))' em _reset_scale
06719. [x] tests\test_font_zoom.py:13 — revisar facet 'coberto por testes' em _reset_scale
06720. [x] tests\test_font_zoom.py:21 — definir/revisar FunctionDef: _wheel
06721. [x] tests\test_font_zoom.py:21 — revisar facet 'assinatura/args consistentes' em _wheel
06722. [x] tests\test_font_zoom.py:21 — revisar facet 'docstring em português' em _wheel
06723. [x] tests\test_font_zoom.py:21 — revisar facet 'nomenclatura clara (PEP8)' em _wheel
06724. [x] tests\test_font_zoom.py:21 — revisar facet 'type hints presentes' em _wheel
06725. [x] tests\test_font_zoom.py:21 — revisar facet 'tratamento de erros adequado' em _wheel
06726. [x] tests\test_font_zoom.py:21 — revisar facet 'sem comentários inline desnecessários' em _wheel
06727. [x] tests\test_font_zoom.py:21 — revisar facet 'não imprime side-effects na UI/IO' em _wheel
06728. [x] tests\test_font_zoom.py:21 — revisar facet 'thread-safety revisada' em _wheel
06729. [x] tests\test_font_zoom.py:21 — revisar facet 'performance (sem loops O(n^2))' em _wheel
06730. [x] tests\test_font_zoom.py:21 — revisar facet 'coberto por testes' em _wheel
06731. [x] tests\test_font_zoom.py:22 — return em _wheel
06732. [x] tests\test_font_zoom.py:29 — definir/revisar FunctionDef: _key
06733. [x] tests\test_font_zoom.py:29 — revisar facet 'assinatura/args consistentes' em _key
06734. [x] tests\test_font_zoom.py:29 — revisar facet 'docstring em português' em _key
06735. [x] tests\test_font_zoom.py:29 — revisar facet 'nomenclatura clara (PEP8)' em _key
06736. [x] tests\test_font_zoom.py:29 — revisar facet 'type hints presentes' em _key
06737. [x] tests\test_font_zoom.py:29 — revisar facet 'tratamento de erros adequado' em _key
06738. [x] tests\test_font_zoom.py:29 — revisar facet 'sem comentários inline desnecessários' em _key
06739. [x] tests\test_font_zoom.py:29 — revisar facet 'não imprime side-effects na UI/IO' em _key
06740. [x] tests\test_font_zoom.py:29 — revisar facet 'thread-safety revisada' em _key
06741. [x] tests\test_font_zoom.py:29 — revisar facet 'performance (sem loops O(n^2))' em _key
06742. [x] tests\test_font_zoom.py:29 — revisar facet 'coberto por testes' em _key
06743. [x] tests\test_font_zoom.py:30 — atribuição: _key ← event
06744. [x] tests\test_font_zoom.py:34 — definir/revisar FunctionDef: test_dialog_no_pending_attribute_error
06745. [x] tests\test_font_zoom.py:34 — revisar facet 'assinatura/args consistentes' em test_dialog_no_pending_attribute_error
06746. [x] tests\test_font_zoom.py:34 — revisar facet 'docstring em português' em test_dialog_no_pending_attribute_error
06747. [x] tests\test_font_zoom.py:34 — revisar facet 'nomenclatura clara (PEP8)' em test_dialog_no_pending_attribute_error
06748. [x] tests\test_font_zoom.py:34 — revisar facet 'type hints presentes' em test_dialog_no_pending_attribute_error
06749. [x] tests\test_font_zoom.py:34 — revisar facet 'tratamento de erros adequado' em test_dialog_no_pending_attribute_error
06750. [x] tests\test_font_zoom.py:34 — revisar facet 'sem comentários inline desnecessários' em test_dialog_no_pending_attribute_error
06751. [x] tests\test_font_zoom.py:34 — revisar facet 'não imprime side-effects na UI/IO' em test_dialog_no_pending_attribute_error
06752. [x] tests\test_font_zoom.py:34 — revisar facet 'thread-safety revisada' em test_dialog_no_pending_attribute_error
06753. [x] tests\test_font_zoom.py:34 — revisar facet 'performance (sem loops O(n^2))' em test_dialog_no_pending_attribute_error
06754. [x] tests\test_font_zoom.py:34 — revisar facet 'coberto por testes' em test_dialog_no_pending_attribute_error
06755. [x] tests\test_font_zoom.py:35 — import: app.ui.widgets.distribution_dialog
06756. [x] tests\test_font_zoom.py:37 — atribuição: test_dialog_no_pending_attribute_error ← dlg
06757. [x] tests\test_font_zoom.py:42 — atribuição: test_dialog_no_pending_attribute_error ← spec
06758. [x] tests\test_font_zoom.py:46 — definir/revisar FunctionDef: test_dialog_restores_existing_spec
06759. [x] tests\test_font_zoom.py:46 — revisar facet 'assinatura/args consistentes' em test_dialog_restores_existing_spec
06760. [x] tests\test_font_zoom.py:46 — revisar facet 'docstring em português' em test_dialog_restores_existing_spec
06761. [x] tests\test_font_zoom.py:46 — revisar facet 'nomenclatura clara (PEP8)' em test_dialog_restores_existing_spec
06762. [x] tests\test_font_zoom.py:46 — revisar facet 'type hints presentes' em test_dialog_restores_existing_spec
06763. [x] tests\test_font_zoom.py:46 — revisar facet 'tratamento de erros adequado' em test_dialog_restores_existing_spec
06764. [x] tests\test_font_zoom.py:46 — revisar facet 'sem comentários inline desnecessários' em test_dialog_restores_existing_spec
06765. [x] tests\test_font_zoom.py:46 — revisar facet 'não imprime side-effects na UI/IO' em test_dialog_restores_existing_spec
06766. [x] tests\test_font_zoom.py:46 — revisar facet 'thread-safety revisada' em test_dialog_restores_existing_spec
06767. [x] tests\test_font_zoom.py:46 — revisar facet 'performance (sem loops O(n^2))' em test_dialog_restores_existing_spec
06768. [x] tests\test_font_zoom.py:46 — revisar facet 'coberto por testes' em test_dialog_restores_existing_spec
06769. [x] tests\test_font_zoom.py:47 — import: app.domain.entities
06770. [x] tests\test_font_zoom.py:48 — import: app.ui.widgets.distribution_dialog
06771. [x] tests\test_font_zoom.py:50 — atribuição: test_dialog_restores_existing_spec ← current
06772. [x] tests\test_font_zoom.py:53 — atribuição: test_dialog_restores_existing_spec ← dlg
06773. [x] tests\test_font_zoom.py:57 — atribuição: test_dialog_restores_existing_spec ← params
06774. [x] tests\test_font_zoom.py:61 — definir/revisar FunctionDef: test_editor_zoom_methods
06775. [x] tests\test_font_zoom.py:61 — revisar facet 'assinatura/args consistentes' em test_editor_zoom_methods
06776. [x] tests\test_font_zoom.py:61 — revisar facet 'docstring em português' em test_editor_zoom_methods
06777. [x] tests\test_font_zoom.py:61 — revisar facet 'nomenclatura clara (PEP8)' em test_editor_zoom_methods
06778. [x] tests\test_font_zoom.py:61 — revisar facet 'type hints presentes' em test_editor_zoom_methods
06779. [x] tests\test_font_zoom.py:61 — revisar facet 'tratamento de erros adequado' em test_editor_zoom_methods
06780. [x] tests\test_font_zoom.py:61 — revisar facet 'sem comentários inline desnecessários' em test_editor_zoom_methods
06781. [x] tests\test_font_zoom.py:61 — revisar facet 'não imprime side-effects na UI/IO' em test_editor_zoom_methods
06782. [x] tests\test_font_zoom.py:61 — revisar facet 'thread-safety revisada' em test_editor_zoom_methods
06783. [x] tests\test_font_zoom.py:61 — revisar facet 'performance (sem loops O(n^2))' em test_editor_zoom_methods
06784. [x] tests\test_font_zoom.py:61 — revisar facet 'coberto por testes' em test_editor_zoom_methods
06785. [x] tests\test_font_zoom.py:62 — atribuição: test_editor_zoom_methods ← editor
06786. [x] tests\test_font_zoom.py:63 — atribuição: test_editor_zoom_methods ← base
06787. [x] tests\test_font_zoom.py:75 — definir/revisar FunctionDef: test_editor_zoom_shortcuts
06788. [x] tests\test_font_zoom.py:75 — revisar facet 'assinatura/args consistentes' em test_editor_zoom_shortcuts
06789. [x] tests\test_font_zoom.py:75 — revisar facet 'docstring em português' em test_editor_zoom_shortcuts
06790. [x] tests\test_font_zoom.py:75 — revisar facet 'nomenclatura clara (PEP8)' em test_editor_zoom_shortcuts
06791. [x] tests\test_font_zoom.py:75 — revisar facet 'type hints presentes' em test_editor_zoom_shortcuts
06792. [x] tests\test_font_zoom.py:75 — revisar facet 'tratamento de erros adequado' em test_editor_zoom_shortcuts
06793. [x] tests\test_font_zoom.py:75 — revisar facet 'sem comentários inline desnecessários' em test_editor_zoom_shortcuts
06794. [x] tests\test_font_zoom.py:75 — revisar facet 'não imprime side-effects na UI/IO' em test_editor_zoom_shortcuts
06795. [x] tests\test_font_zoom.py:75 — revisar facet 'thread-safety revisada' em test_editor_zoom_shortcuts
06796. [x] tests\test_font_zoom.py:75 — revisar facet 'performance (sem loops O(n^2))' em test_editor_zoom_shortcuts
06797. [x] tests\test_font_zoom.py:75 — revisar facet 'coberto por testes' em test_editor_zoom_shortcuts
06798. [x] tests\test_font_zoom.py:76 — atribuição: test_editor_zoom_shortcuts ← editor
06799. [x] tests\test_font_zoom.py:77 — atribuição: test_editor_zoom_shortcuts ← base
06800. [x] tests\test_font_zoom.py:89 — definir/revisar FunctionDef: test_editor_zoom_ctrl_wheel
06801. [x] tests\test_font_zoom.py:89 — revisar facet 'assinatura/args consistentes' em test_editor_zoom_ctrl_wheel
06802. [x] tests\test_font_zoom.py:89 — revisar facet 'docstring em português' em test_editor_zoom_ctrl_wheel
06803. [x] tests\test_font_zoom.py:89 — revisar facet 'nomenclatura clara (PEP8)' em test_editor_zoom_ctrl_wheel
06804. [x] tests\test_font_zoom.py:89 — revisar facet 'type hints presentes' em test_editor_zoom_ctrl_wheel
06805. [x] tests\test_font_zoom.py:89 — revisar facet 'tratamento de erros adequado' em test_editor_zoom_ctrl_wheel
06806. [x] tests\test_font_zoom.py:89 — revisar facet 'sem comentários inline desnecessários' em test_editor_zoom_ctrl_wheel
06807. [x] tests\test_font_zoom.py:89 — revisar facet 'não imprime side-effects na UI/IO' em test_editor_zoom_ctrl_wheel
06808. [x] tests\test_font_zoom.py:89 — revisar facet 'thread-safety revisada' em test_editor_zoom_ctrl_wheel
06809. [x] tests\test_font_zoom.py:89 — revisar facet 'performance (sem loops O(n^2))' em test_editor_zoom_ctrl_wheel
06810. [x] tests\test_font_zoom.py:89 — revisar facet 'coberto por testes' em test_editor_zoom_ctrl_wheel
06811. [x] tests\test_font_zoom.py:90 — atribuição: test_editor_zoom_ctrl_wheel ← editor
06812. [x] tests\test_font_zoom.py:91 — atribuição: test_editor_zoom_ctrl_wheel ← base
06813. [x] tests\test_font_zoom.py:97 — definir/revisar FunctionDef: test_menu_zoom_applies_to_all_tabs
06814. [x] tests\test_font_zoom.py:97 — revisar facet 'assinatura/args consistentes' em test_menu_zoom_applies_to_all_tabs
06815. [x] tests\test_font_zoom.py:97 — revisar facet 'docstring em português' em test_menu_zoom_applies_to_all_tabs
06816. [x] tests\test_font_zoom.py:97 — revisar facet 'nomenclatura clara (PEP8)' em test_menu_zoom_applies_to_all_tabs
06817. [x] tests\test_font_zoom.py:97 — revisar facet 'type hints presentes' em test_menu_zoom_applies_to_all_tabs
06818. [x] tests\test_font_zoom.py:97 — revisar facet 'tratamento de erros adequado' em test_menu_zoom_applies_to_all_tabs
06819. [x] tests\test_font_zoom.py:97 — revisar facet 'sem comentários inline desnecessários' em test_menu_zoom_applies_to_all_tabs
06820. [x] tests\test_font_zoom.py:97 — revisar facet 'não imprime side-effects na UI/IO' em test_menu_zoom_applies_to_all_tabs
06821. [x] tests\test_font_zoom.py:97 — revisar facet 'thread-safety revisada' em test_menu_zoom_applies_to_all_tabs
06822. [x] tests\test_font_zoom.py:97 — revisar facet 'performance (sem loops O(n^2))' em test_menu_zoom_applies_to_all_tabs
06823. [x] tests\test_font_zoom.py:97 — revisar facet 'coberto por testes' em test_menu_zoom_applies_to_all_tabs
06824. [x] tests\test_font_zoom.py:98 — atribuição: test_menu_zoom_applies_to_all_tabs ← window
06825. [x] tests\test_font_zoom.py:100 — atribuição: test_menu_zoom_applies_to_all_tabs ← base
06826. [x] tests\test_font_zoom.py:103 — atribuição: test_menu_zoom_applies_to_all_tabs ← sizes
06827. [x] tests\test_font_zoom.py:110 — controle for em test_menu_zoom_applies_to_all_tabs
06828. [x] tests\test_font_zoom.py:111 — atribuição: test_menu_zoom_applies_to_all_tabs ← tab
06829. [x] tests\test_font_zoom.py:112 — controle if em test_menu_zoom_applies_to_all_tabs
06830. [x] tests\test_font_zoom.py:116 — definir/revisar FunctionDef: test_system_font_scale
06831. [x] tests\test_font_zoom.py:116 — revisar facet 'assinatura/args consistentes' em test_system_font_scale
06832. [x] tests\test_font_zoom.py:116 — revisar facet 'docstring em português' em test_system_font_scale
06833. [x] tests\test_font_zoom.py:116 — revisar facet 'nomenclatura clara (PEP8)' em test_system_font_scale
06834. [x] tests\test_font_zoom.py:116 — revisar facet 'type hints presentes' em test_system_font_scale
06835. [x] tests\test_font_zoom.py:116 — revisar facet 'tratamento de erros adequado' em test_system_font_scale
06836. [x] tests\test_font_zoom.py:116 — revisar facet 'sem comentários inline desnecessários' em test_system_font_scale
06837. [x] tests\test_font_zoom.py:116 — revisar facet 'não imprime side-effects na UI/IO' em test_system_font_scale
06838. [x] tests\test_font_zoom.py:116 — revisar facet 'thread-safety revisada' em test_system_font_scale
06839. [x] tests\test_font_zoom.py:116 — revisar facet 'performance (sem loops O(n^2))' em test_system_font_scale
06840. [x] tests\test_font_zoom.py:116 — revisar facet 'coberto por testes' em test_system_font_scale
06841. [x] tests\test_font_zoom.py:117 — import: PySide6.QtWidgets
06842. [x] tests\test_font_zoom.py:119 — atribuição: test_system_font_scale ← window
06843. [x] tests\test_font_zoom.py:123 — atribuição: test_system_font_scale ← ref
06844. [x] Existência e estrutura do módulo: tests\test_gui_startup.py
06845. [x] tests\test_gui_startup.py:3 — import: json
06846. [x] tests\test_gui_startup.py:4 — import: os
06847. [x] tests\test_gui_startup.py:5 — import: subprocess
06848. [x] tests\test_gui_startup.py:6 — import: sys
06849. [x] tests\test_gui_startup.py:7 — import: pathlib
06850. [x] tests\test_gui_startup.py:9 — import: pytest
06851. [x] tests\test_gui_startup.py:13 — atribuição:  ← PROJECT_ROOT
06852. [x] tests\test_gui_startup.py:17 — definir/revisar FunctionDef: boot
06853. [x] tests\test_gui_startup.py:17 — revisar facet 'assinatura/args consistentes' em boot
06854. [x] tests\test_gui_startup.py:17 — revisar facet 'docstring em português' em boot
06855. [x] tests\test_gui_startup.py:17 — revisar facet 'nomenclatura clara (PEP8)' em boot
06856. [x] tests\test_gui_startup.py:17 — revisar facet 'type hints presentes' em boot
06857. [x] tests\test_gui_startup.py:17 — revisar facet 'tratamento de erros adequado' em boot
06858. [x] tests\test_gui_startup.py:17 — revisar facet 'sem comentários inline desnecessários' em boot
06859. [x] tests\test_gui_startup.py:17 — revisar facet 'não imprime side-effects na UI/IO' em boot
06860. [x] tests\test_gui_startup.py:17 — revisar facet 'thread-safety revisada' em boot
06861. [x] tests\test_gui_startup.py:17 — revisar facet 'performance (sem loops O(n^2))' em boot
06862. [x] tests\test_gui_startup.py:17 — revisar facet 'coberto por testes' em boot
06863. [x] tests\test_gui_startup.py:20 — definir/revisar FunctionDef: boot._boot
06864. [x] tests\test_gui_startup.py:20 — revisar facet 'assinatura/args consistentes' em boot._boot
06865. [x] tests\test_gui_startup.py:20 — revisar facet 'docstring em português' em boot._boot
06866. [x] tests\test_gui_startup.py:20 — revisar facet 'nomenclatura clara (PEP8)' em boot._boot
06867. [x] tests\test_gui_startup.py:20 — revisar facet 'type hints presentes' em boot._boot
06868. [x] tests\test_gui_startup.py:20 — revisar facet 'tratamento de erros adequado' em boot._boot
06869. [x] tests\test_gui_startup.py:20 — revisar facet 'sem comentários inline desnecessários' em boot._boot
06870. [x] tests\test_gui_startup.py:20 — revisar facet 'não imprime side-effects na UI/IO' em boot._boot
06871. [x] tests\test_gui_startup.py:20 — revisar facet 'thread-safety revisada' em boot._boot
06872. [x] tests\test_gui_startup.py:20 — revisar facet 'performance (sem loops O(n^2))' em boot._boot
06873. [x] tests\test_gui_startup.py:20 — revisar facet 'coberto por testes' em boot._boot
06874. [x] tests\test_gui_startup.py:21 — import: PySide6.QtWidgets
06875. [x] tests\test_gui_startup.py:23 — atribuição: boot._boot ← app
06876. [x] tests\test_gui_startup.py:25 — import: app.container
06877. [x] tests\test_gui_startup.py:26 — import: app.ui.main_window
06878. [x] tests\test_gui_startup.py:28 — atribuição: boot._boot ← container
06879. [x] tests\test_gui_startup.py:29 — atribuição: boot._boot ← window
06880. [x] tests\test_gui_startup.py:31 — return em boot._boot
06881. [x] tests\test_gui_startup.py:33 — return em boot
06882. [x] tests\test_gui_startup.py:39 — definir/revisar FunctionDef: test_application_and_window_created
06883. [x] tests\test_gui_startup.py:39 — revisar facet 'assinatura/args consistentes' em test_application_and_window_created
06884. [x] tests\test_gui_startup.py:39 — revisar facet 'docstring em português' em test_application_and_window_created
06885. [x] tests\test_gui_startup.py:39 — revisar facet 'nomenclatura clara (PEP8)' em test_application_and_window_created
06886. [x] tests\test_gui_startup.py:39 — revisar facet 'type hints presentes' em test_application_and_window_created
06887. [x] tests\test_gui_startup.py:39 — revisar facet 'tratamento de erros adequado' em test_application_and_window_created
06888. [x] tests\test_gui_startup.py:39 — revisar facet 'sem comentários inline desnecessários' em test_application_and_window_created
06889. [x] tests\test_gui_startup.py:39 — revisar facet 'não imprime side-effects na UI/IO' em test_application_and_window_created
06890. [x] tests\test_gui_startup.py:39 — revisar facet 'thread-safety revisada' em test_application_and_window_created
06891. [x] tests\test_gui_startup.py:39 — revisar facet 'performance (sem loops O(n^2))' em test_application_and_window_created
06892. [x] tests\test_gui_startup.py:39 — revisar facet 'coberto por testes' em test_application_and_window_created
06893. [x] tests\test_gui_startup.py:40 — atribuição: test_application_and_window_created ← ?
06894. [x] tests\test_gui_startup.py:48 — definir/revisar FunctionDef: test_window_has_editor_and_variables
06895. [x] tests\test_gui_startup.py:48 — revisar facet 'assinatura/args consistentes' em test_window_has_editor_and_variables
06896. [x] tests\test_gui_startup.py:48 — revisar facet 'docstring em português' em test_window_has_editor_and_variables
06897. [x] tests\test_gui_startup.py:48 — revisar facet 'nomenclatura clara (PEP8)' em test_window_has_editor_and_variables
06898. [x] tests\test_gui_startup.py:48 — revisar facet 'type hints presentes' em test_window_has_editor_and_variables
06899. [x] tests\test_gui_startup.py:48 — revisar facet 'tratamento de erros adequado' em test_window_has_editor_and_variables
06900. [x] tests\test_gui_startup.py:48 — revisar facet 'sem comentários inline desnecessários' em test_window_has_editor_and_variables
06901. [x] tests\test_gui_startup.py:48 — revisar facet 'não imprime side-effects na UI/IO' em test_window_has_editor_and_variables
06902. [x] tests\test_gui_startup.py:48 — revisar facet 'thread-safety revisada' em test_window_has_editor_and_variables
06903. [x] tests\test_gui_startup.py:48 — revisar facet 'performance (sem loops O(n^2))' em test_window_has_editor_and_variables
06904. [x] tests\test_gui_startup.py:48 — revisar facet 'coberto por testes' em test_window_has_editor_and_variables
06905. [x] tests\test_gui_startup.py:49 — atribuição: test_window_has_editor_and_variables ← ?
06906. [x] tests\test_gui_startup.py:51 — atribuição: test_window_has_editor_and_variables ← editor
06907. [x] tests\test_gui_startup.py:60 — definir/revisar FunctionDef: test_main_window_components
06908. [x] tests\test_gui_startup.py:60 — revisar facet 'assinatura/args consistentes' em test_main_window_components
06909. [x] tests\test_gui_startup.py:60 — revisar facet 'docstring em português' em test_main_window_components
06910. [x] tests\test_gui_startup.py:60 — revisar facet 'nomenclatura clara (PEP8)' em test_main_window_components
06911. [x] tests\test_gui_startup.py:60 — revisar facet 'type hints presentes' em test_main_window_components
06912. [x] tests\test_gui_startup.py:60 — revisar facet 'tratamento de erros adequado' em test_main_window_components
06913. [x] tests\test_gui_startup.py:60 — revisar facet 'sem comentários inline desnecessários' em test_main_window_components
06914. [x] tests\test_gui_startup.py:60 — revisar facet 'não imprime side-effects na UI/IO' em test_main_window_components
06915. [x] tests\test_gui_startup.py:60 — revisar facet 'thread-safety revisada' em test_main_window_components
06916. [x] tests\test_gui_startup.py:60 — revisar facet 'performance (sem loops O(n^2))' em test_main_window_components
06917. [x] tests\test_gui_startup.py:60 — revisar facet 'coberto por testes' em test_main_window_components
06918. [x] tests\test_gui_startup.py:61 — atribuição: test_main_window_components ← ?
06919. [x] tests\test_gui_startup.py:71 — definir/revisar FunctionDef: test_main_window_menus
06920. [x] tests\test_gui_startup.py:71 — revisar facet 'assinatura/args consistentes' em test_main_window_menus
06921. [x] tests\test_gui_startup.py:71 — revisar facet 'docstring em português' em test_main_window_menus
06922. [x] tests\test_gui_startup.py:71 — revisar facet 'nomenclatura clara (PEP8)' em test_main_window_menus
06923. [x] tests\test_gui_startup.py:71 — revisar facet 'type hints presentes' em test_main_window_menus
06924. [x] tests\test_gui_startup.py:71 — revisar facet 'tratamento de erros adequado' em test_main_window_menus
06925. [x] tests\test_gui_startup.py:71 — revisar facet 'sem comentários inline desnecessários' em test_main_window_menus
06926. [x] tests\test_gui_startup.py:71 — revisar facet 'não imprime side-effects na UI/IO' em test_main_window_menus
06927. [x] tests\test_gui_startup.py:71 — revisar facet 'thread-safety revisada' em test_main_window_menus
06928. [x] tests\test_gui_startup.py:71 — revisar facet 'performance (sem loops O(n^2))' em test_main_window_menus
06929. [x] tests\test_gui_startup.py:71 — revisar facet 'coberto por testes' em test_main_window_menus
06930. [x] tests\test_gui_startup.py:72 — atribuição: test_main_window_menus ← ?
06931. [x] tests\test_gui_startup.py:75 — atribuição: test_main_window_menus ← menubar
06932. [x] tests\test_gui_startup.py:76 — atribuição: test_main_window_menus ← actions
06933. [x] tests\test_gui_startup.py:77 — atribuição: test_main_window_menus ← names
06934. [x] tests\test_gui_startup.py:81 — atribuição: test_main_window_menus ← file_menu
06935. [x] tests\test_gui_startup.py:82 — atribuição: test_main_window_menus ← file_names
06936. [x] tests\test_gui_startup.py:88 — definir/revisar FunctionDef: test_main_window_first_new_tab
06937. [x] tests\test_gui_startup.py:88 — revisar facet 'assinatura/args consistentes' em test_main_window_first_new_tab
06938. [x] tests\test_gui_startup.py:88 — revisar facet 'docstring em português' em test_main_window_first_new_tab
06939. [x] tests\test_gui_startup.py:88 — revisar facet 'nomenclatura clara (PEP8)' em test_main_window_first_new_tab
06940. [x] tests\test_gui_startup.py:88 — revisar facet 'type hints presentes' em test_main_window_first_new_tab
06941. [x] tests\test_gui_startup.py:88 — revisar facet 'tratamento de erros adequado' em test_main_window_first_new_tab
06942. [x] tests\test_gui_startup.py:88 — revisar facet 'sem comentários inline desnecessários' em test_main_window_first_new_tab
06943. [x] tests\test_gui_startup.py:88 — revisar facet 'não imprime side-effects na UI/IO' em test_main_window_first_new_tab
06944. [x] tests\test_gui_startup.py:88 — revisar facet 'thread-safety revisada' em test_main_window_first_new_tab
06945. [x] tests\test_gui_startup.py:88 — revisar facet 'performance (sem loops O(n^2))' em test_main_window_first_new_tab
06946. [x] tests\test_gui_startup.py:88 — revisar facet 'coberto por testes' em test_main_window_first_new_tab
06947. [x] tests\test_gui_startup.py:89 — atribuição: test_main_window_first_new_tab ← ?
06948. [x] tests\test_gui_startup.py:91 — atribuição: test_main_window_first_new_tab ← editor
06949. [x] tests\test_gui_startup.py:98 — definir/revisar FunctionDef: test_container_loads_storages
06950. [x] tests\test_gui_startup.py:98 — revisar facet 'assinatura/args consistentes' em test_container_loads_storages
06951. [x] tests\test_gui_startup.py:98 — revisar facet 'docstring em português' em test_container_loads_storages
06952. [x] tests\test_gui_startup.py:98 — revisar facet 'nomenclatura clara (PEP8)' em test_container_loads_storages
06953. [x] tests\test_gui_startup.py:98 — revisar facet 'type hints presentes' em test_container_loads_storages
06954. [x] tests\test_gui_startup.py:98 — revisar facet 'tratamento de erros adequado' em test_container_loads_storages
06955. [x] tests\test_gui_startup.py:98 — revisar facet 'sem comentários inline desnecessários' em test_container_loads_storages
06956. [x] tests\test_gui_startup.py:98 — revisar facet 'não imprime side-effects na UI/IO' em test_container_loads_storages
06957. [x] tests\test_gui_startup.py:98 — revisar facet 'thread-safety revisada' em test_container_loads_storages
06958. [x] tests\test_gui_startup.py:98 — revisar facet 'performance (sem loops O(n^2))' em test_container_loads_storages
06959. [x] tests\test_gui_startup.py:98 — revisar facet 'coberto por testes' em test_container_loads_storages
06960. [x] tests\test_gui_startup.py:99 — atribuição: test_container_loads_storages ← ?
06961. [x] tests\test_gui_startup.py:108 — definir/revisar FunctionDef: test_container_shutdown_closes_all_repos
06962. [x] tests\test_gui_startup.py:108 — revisar facet 'assinatura/args consistentes' em test_container_shutdown_closes_all_repos
06963. [x] tests\test_gui_startup.py:108 — revisar facet 'docstring em português' em test_container_shutdown_closes_all_repos
06964. [x] tests\test_gui_startup.py:108 — revisar facet 'nomenclatura clara (PEP8)' em test_container_shutdown_closes_all_repos
06965. [x] tests\test_gui_startup.py:108 — revisar facet 'type hints presentes' em test_container_shutdown_closes_all_repos
06966. [x] tests\test_gui_startup.py:108 — revisar facet 'tratamento de erros adequado' em test_container_shutdown_closes_all_repos
06967. [x] tests\test_gui_startup.py:108 — revisar facet 'sem comentários inline desnecessários' em test_container_shutdown_closes_all_repos
06968. [x] tests\test_gui_startup.py:108 — revisar facet 'não imprime side-effects na UI/IO' em test_container_shutdown_closes_all_repos
06969. [x] tests\test_gui_startup.py:108 — revisar facet 'thread-safety revisada' em test_container_shutdown_closes_all_repos
06970. [x] tests\test_gui_startup.py:108 — revisar facet 'performance (sem loops O(n^2))' em test_container_shutdown_closes_all_repos
06971. [x] tests\test_gui_startup.py:108 — revisar facet 'coberto por testes' em test_container_shutdown_closes_all_repos
06972. [x] tests\test_gui_startup.py:109 — atribuição: test_container_shutdown_closes_all_repos ← ?
06973. [x] tests\test_gui_startup.py:113 — controle with em test_container_shutdown_closes_all_repos
06974. [x] tests\test_gui_startup.py:120 — definir/revisar FunctionDef: test_close_event_triggers_shutdown
06975. [x] tests\test_gui_startup.py:120 — revisar facet 'assinatura/args consistentes' em test_close_event_triggers_shutdown
06976. [x] tests\test_gui_startup.py:120 — revisar facet 'docstring em português' em test_close_event_triggers_shutdown
06977. [x] tests\test_gui_startup.py:120 — revisar facet 'nomenclatura clara (PEP8)' em test_close_event_triggers_shutdown
06978. [x] tests\test_gui_startup.py:120 — revisar facet 'type hints presentes' em test_close_event_triggers_shutdown
06979. [x] tests\test_gui_startup.py:120 — revisar facet 'tratamento de erros adequado' em test_close_event_triggers_shutdown
06980. [x] tests\test_gui_startup.py:120 — revisar facet 'sem comentários inline desnecessários' em test_close_event_triggers_shutdown
06981. [x] tests\test_gui_startup.py:120 — revisar facet 'não imprime side-effects na UI/IO' em test_close_event_triggers_shutdown
06982. [x] tests\test_gui_startup.py:120 — revisar facet 'thread-safety revisada' em test_close_event_triggers_shutdown
06983. [x] tests\test_gui_startup.py:120 — revisar facet 'performance (sem loops O(n^2))' em test_close_event_triggers_shutdown
06984. [x] tests\test_gui_startup.py:120 — revisar facet 'coberto por testes' em test_close_event_triggers_shutdown
06985. [x] tests\test_gui_startup.py:121 — atribuição: test_close_event_triggers_shutdown ← ?
06986. [x] tests\test_gui_startup.py:128 — definir/revisar FunctionDef: test_repeated_instance_boot
06987. [x] tests\test_gui_startup.py:128 — revisar facet 'assinatura/args consistentes' em test_repeated_instance_boot
06988. [x] tests\test_gui_startup.py:128 — revisar facet 'docstring em português' em test_repeated_instance_boot
06989. [x] tests\test_gui_startup.py:128 — revisar facet 'nomenclatura clara (PEP8)' em test_repeated_instance_boot
06990. [x] tests\test_gui_startup.py:128 — revisar facet 'type hints presentes' em test_repeated_instance_boot
06991. [x] tests\test_gui_startup.py:128 — revisar facet 'tratamento de erros adequado' em test_repeated_instance_boot
06992. [x] tests\test_gui_startup.py:128 — revisar facet 'sem comentários inline desnecessários' em test_repeated_instance_boot
06993. [x] tests\test_gui_startup.py:128 — revisar facet 'não imprime side-effects na UI/IO' em test_repeated_instance_boot
06994. [x] tests\test_gui_startup.py:128 — revisar facet 'thread-safety revisada' em test_repeated_instance_boot
06995. [x] tests\test_gui_startup.py:128 — revisar facet 'performance (sem loops O(n^2))' em test_repeated_instance_boot
06996. [x] tests\test_gui_startup.py:128 — revisar facet 'coberto por testes' em test_repeated_instance_boot
06997. [x] tests\test_gui_startup.py:129 — atribuição: test_repeated_instance_boot ← ?
06998. [x] tests\test_gui_startup.py:131 — atribuição: test_repeated_instance_boot ← window2
06999. [x] tests\test_gui_startup.py:142 — definir/revisar FunctionDef: test_main_window_loads_data_template
07000. [x] tests\test_gui_startup.py:142 — revisar facet 'assinatura/args consistentes' em test_main_window_loads_data_template
07001. [x] tests\test_gui_startup.py:142 — revisar facet 'docstring em português' em test_main_window_loads_data_template
07002. [x] tests\test_gui_startup.py:142 — revisar facet 'nomenclatura clara (PEP8)' em test_main_window_loads_data_template
07003. [x] tests\test_gui_startup.py:142 — revisar facet 'type hints presentes' em test_main_window_loads_data_template
07004. [x] tests\test_gui_startup.py:142 — revisar facet 'tratamento de erros adequado' em test_main_window_loads_data_template
07005. [x] tests\test_gui_startup.py:142 — revisar facet 'sem comentários inline desnecessários' em test_main_window_loads_data_template
07006. [x] tests\test_gui_startup.py:142 — revisar facet 'não imprime side-effects na UI/IO' em test_main_window_loads_data_template
07007. [x] tests\test_gui_startup.py:142 — revisar facet 'thread-safety revisada' em test_main_window_loads_data_template
07008. [x] tests\test_gui_startup.py:142 — revisar facet 'performance (sem loops O(n^2))' em test_main_window_loads_data_template
07009. [x] tests\test_gui_startup.py:142 — revisar facet 'coberto por testes' em test_main_window_loads_data_template
07010. [x] tests\test_gui_startup.py:143 — atribuição: test_main_window_loads_data_template ← ?
07011. [x] tests\test_gui_startup.py:145 — atribuição: test_main_window_loads_data_template ← editor
07012. [x] tests\test_gui_startup.py:152 — definir/revisar FunctionDef: test_starting_with_dock_layout
07013. [x] tests\test_gui_startup.py:152 — revisar facet 'assinatura/args consistentes' em test_starting_with_dock_layout
07014. [x] tests\test_gui_startup.py:152 — revisar facet 'docstring em português' em test_starting_with_dock_layout
07015. [x] tests\test_gui_startup.py:152 — revisar facet 'nomenclatura clara (PEP8)' em test_starting_with_dock_layout
07016. [x] tests\test_gui_startup.py:152 — revisar facet 'type hints presentes' em test_starting_with_dock_layout
07017. [x] tests\test_gui_startup.py:152 — revisar facet 'tratamento de erros adequado' em test_starting_with_dock_layout
07018. [x] tests\test_gui_startup.py:152 — revisar facet 'sem comentários inline desnecessários' em test_starting_with_dock_layout
07019. [x] tests\test_gui_startup.py:152 — revisar facet 'não imprime side-effects na UI/IO' em test_starting_with_dock_layout
07020. [x] tests\test_gui_startup.py:152 — revisar facet 'thread-safety revisada' em test_starting_with_dock_layout
07021. [x] tests\test_gui_startup.py:152 — revisar facet 'performance (sem loops O(n^2))' em test_starting_with_dock_layout
07022. [x] tests\test_gui_startup.py:152 — revisar facet 'coberto por testes' em test_starting_with_dock_layout
07023. [x] tests\test_gui_startup.py:153 — atribuição: test_starting_with_dock_layout ← ?
07024. [x] tests\test_gui_startup.py:155 — atribuição: test_starting_with_dock_layout ← docks
07025. [x] tests\test_gui_startup.py:158 — atribuição: test_starting_with_dock_layout ← titles
07026. [x] tests\test_gui_startup.py:164 — definir/revisar FunctionDef: test_startup_updates_progress_bar
07027. [x] tests\test_gui_startup.py:164 — revisar facet 'assinatura/args consistentes' em test_startup_updates_progress_bar
07028. [x] tests\test_gui_startup.py:164 — revisar facet 'docstring em português' em test_startup_updates_progress_bar
07029. [x] tests\test_gui_startup.py:164 — revisar facet 'nomenclatura clara (PEP8)' em test_startup_updates_progress_bar
07030. [x] tests\test_gui_startup.py:164 — revisar facet 'type hints presentes' em test_startup_updates_progress_bar
07031. [x] tests\test_gui_startup.py:164 — revisar facet 'tratamento de erros adequado' em test_startup_updates_progress_bar
07032. [x] tests\test_gui_startup.py:164 — revisar facet 'sem comentários inline desnecessários' em test_startup_updates_progress_bar
07033. [x] tests\test_gui_startup.py:164 — revisar facet 'não imprime side-effects na UI/IO' em test_startup_updates_progress_bar
07034. [x] tests\test_gui_startup.py:164 — revisar facet 'thread-safety revisada' em test_startup_updates_progress_bar
07035. [x] tests\test_gui_startup.py:164 — revisar facet 'performance (sem loops O(n^2))' em test_startup_updates_progress_bar
07036. [x] tests\test_gui_startup.py:164 — revisar facet 'coberto por testes' em test_startup_updates_progress_bar
07037. [x] tests\test_gui_startup.py:165 — import: app.domain.events
07038. [x] tests\test_gui_startup.py:167 — atribuição: test_startup_updates_progress_bar ← ?
07039. [x] tests\test_gui_startup.py:173 — definir/revisar FunctionDef: test_startup_pipeline_sample_template
07040. [x] tests\test_gui_startup.py:173 — revisar facet 'assinatura/args consistentes' em test_startup_pipeline_sample_template
07041. [x] tests\test_gui_startup.py:173 — revisar facet 'docstring em português' em test_startup_pipeline_sample_template
07042. [x] tests\test_gui_startup.py:173 — revisar facet 'nomenclatura clara (PEP8)' em test_startup_pipeline_sample_template
07043. [x] tests\test_gui_startup.py:173 — revisar facet 'type hints presentes' em test_startup_pipeline_sample_template
07044. [x] tests\test_gui_startup.py:173 — revisar facet 'tratamento de erros adequado' em test_startup_pipeline_sample_template
07045. [x] tests\test_gui_startup.py:173 — revisar facet 'sem comentários inline desnecessários' em test_startup_pipeline_sample_template
07046. [x] tests\test_gui_startup.py:173 — revisar facet 'não imprime side-effects na UI/IO' em test_startup_pipeline_sample_template
07047. [x] tests\test_gui_startup.py:173 — revisar facet 'thread-safety revisada' em test_startup_pipeline_sample_template
07048. [x] tests\test_gui_startup.py:173 — revisar facet 'performance (sem loops O(n^2))' em test_startup_pipeline_sample_template
07049. [x] tests\test_gui_startup.py:173 — revisar facet 'coberto por testes' em test_startup_pipeline_sample_template
07050. [x] tests\test_gui_startup.py:174 — import: app.domain.entities
07051. [x] tests\test_gui_startup.py:176 — atribuição: test_startup_pipeline_sample_template ← ?
07052. [x] tests\test_gui_startup.py:178 — atribuição: test_startup_pipeline_sample_template ← editor
07053. [x] tests\test_gui_startup.py:181 — import: app.core.parsing
07054. [x] tests\test_gui_startup.py:183 — atribuição: test_startup_pipeline_sample_template ← var_ids
07055. [x] tests\test_gui_startup.py:186 — atribuição: test_startup_pipeline_sample_template ← specs
07056. [x] tests\test_gui_startup.py:190 — atribuição: test_startup_pipeline_sample_template ← request
07057. [x] tests\test_gui_startup.py:191 — atribuição: test_startup_pipeline_sample_template ← result
07058. [x] tests\test_gui_startup.py:203 — atribuição:  ← RUNNER
07059. [x] tests\test_gui_startup.py:238 — definir/revisar FunctionDef: test_subprocess_full_gui_startup
07060. [x] tests\test_gui_startup.py:238 — revisar facet 'assinatura/args consistentes' em test_subprocess_full_gui_startup
07061. [x] tests\test_gui_startup.py:238 — revisar facet 'docstring em português' em test_subprocess_full_gui_startup
07062. [x] tests\test_gui_startup.py:238 — revisar facet 'nomenclatura clara (PEP8)' em test_subprocess_full_gui_startup
07063. [x] tests\test_gui_startup.py:238 — revisar facet 'type hints presentes' em test_subprocess_full_gui_startup
07064. [x] tests\test_gui_startup.py:238 — revisar facet 'tratamento de erros adequado' em test_subprocess_full_gui_startup
07065. [x] tests\test_gui_startup.py:238 — revisar facet 'sem comentários inline desnecessários' em test_subprocess_full_gui_startup
07066. [x] tests\test_gui_startup.py:238 — revisar facet 'não imprime side-effects na UI/IO' em test_subprocess_full_gui_startup
07067. [x] tests\test_gui_startup.py:238 — revisar facet 'thread-safety revisada' em test_subprocess_full_gui_startup
07068. [x] tests\test_gui_startup.py:238 — revisar facet 'performance (sem loops O(n^2))' em test_subprocess_full_gui_startup
07069. [x] tests\test_gui_startup.py:238 — revisar facet 'coberto por testes' em test_subprocess_full_gui_startup
07070. [x] tests\test_gui_startup.py:239 — atribuição: test_subprocess_full_gui_startup ← runner
07071. [x] tests\test_gui_startup.py:242 — atribuição: test_subprocess_full_gui_startup ← boot_dir
07072. [x] tests\test_gui_startup.py:245 — atribuição: test_subprocess_full_gui_startup ← env
07073. [x] tests\test_gui_startup.py:246 — atribuição: test_subprocess_full_gui_startup ← ?
07074. [x] tests\test_gui_startup.py:247 — atribuição: test_subprocess_full_gui_startup ← ?
07075. [x] tests\test_gui_startup.py:249 — atribuição: test_subprocess_full_gui_startup ← result
07076. [x] tests\test_gui_startup.py:256 — atribuição: test_subprocess_full_gui_startup ← report_line
07077. [x] tests\test_gui_startup.py:259 — atribuição: test_subprocess_full_gui_startup ← report
07078. [x] Existência e estrutura do módulo: tests\test_log_service.py
07079. [x] tests\test_log_service.py:3 — import: time
07080. [x] tests\test_log_service.py:6 — definir/revisar FunctionDef: test_log_write_and_fetch
07081. [x] tests\test_log_service.py:6 — revisar facet 'assinatura/args consistentes' em test_log_write_and_fetch
07082. [x] tests\test_log_service.py:6 — revisar facet 'docstring em português' em test_log_write_and_fetch
07083. [x] tests\test_log_service.py:6 — revisar facet 'nomenclatura clara (PEP8)' em test_log_write_and_fetch
07084. [x] tests\test_log_service.py:6 — revisar facet 'type hints presentes' em test_log_write_and_fetch
07085. [x] tests\test_log_service.py:6 — revisar facet 'tratamento de erros adequado' em test_log_write_and_fetch
07086. [x] tests\test_log_service.py:6 — revisar facet 'sem comentários inline desnecessários' em test_log_write_and_fetch
07087. [x] tests\test_log_service.py:6 — revisar facet 'não imprime side-effects na UI/IO' em test_log_write_and_fetch
07088. [x] tests\test_log_service.py:6 — revisar facet 'thread-safety revisada' em test_log_write_and_fetch
07089. [x] tests\test_log_service.py:6 — revisar facet 'performance (sem loops O(n^2))' em test_log_write_and_fetch
07090. [x] tests\test_log_service.py:6 — revisar facet 'coberto por testes' em test_log_write_and_fetch
07091. [x] tests\test_log_service.py:11 — atribuição: test_log_write_and_fetch ← repo
07092. [x] tests\test_log_service.py:14 — atribuição: test_log_write_and_fetch ← rows
07093. [x] tests\test_log_service.py:18 — atribuição: test_log_write_and_fetch ← errors
07094. [x] tests\test_log_service.py:22 — atribuição: test_log_write_and_fetch ← search
07095. [x] tests\test_log_service.py:26 — definir/revisar FunctionDef: test_log_write_does_not_block
07096. [x] tests\test_log_service.py:26 — revisar facet 'assinatura/args consistentes' em test_log_write_does_not_block
07097. [x] tests\test_log_service.py:26 — revisar facet 'docstring em português' em test_log_write_does_not_block
07098. [x] tests\test_log_service.py:26 — revisar facet 'nomenclatura clara (PEP8)' em test_log_write_does_not_block
07099. [x] tests\test_log_service.py:26 — revisar facet 'type hints presentes' em test_log_write_does_not_block
07100. [x] tests\test_log_service.py:26 — revisar facet 'tratamento de erros adequado' em test_log_write_does_not_block
07101. [x] tests\test_log_service.py:26 — revisar facet 'sem comentários inline desnecessários' em test_log_write_does_not_block
07102. [x] tests\test_log_service.py:26 — revisar facet 'não imprime side-effects na UI/IO' em test_log_write_does_not_block
07103. [x] tests\test_log_service.py:26 — revisar facet 'thread-safety revisada' em test_log_write_does_not_block
07104. [x] tests\test_log_service.py:26 — revisar facet 'performance (sem loops O(n^2))' em test_log_write_does_not_block
07105. [x] tests\test_log_service.py:26 — revisar facet 'coberto por testes' em test_log_write_does_not_block
07106. [x] tests\test_log_service.py:27 — import: app.services.log_service
07107. [x] tests\test_log_service.py:29 — atribuição: test_log_write_does_not_block ← svc
07108. [x] tests\test_log_service.py:30 — atribuição: test_log_write_does_not_block ← t0
07109. [x] tests\test_log_service.py:31 — controle for em test_log_write_does_not_block
07110. [x] tests\test_log_service.py:33 — atribuição: test_log_write_does_not_block ← elapsed
07111. [x] tests\test_log_service.py:37 — definir/revisar FunctionDef: test_event_bus_sanity
07112. [x] tests\test_log_service.py:37 — revisar facet 'assinatura/args consistentes' em test_event_bus_sanity
07113. [x] tests\test_log_service.py:37 — revisar facet 'docstring em português' em test_event_bus_sanity
07114. [x] tests\test_log_service.py:37 — revisar facet 'nomenclatura clara (PEP8)' em test_event_bus_sanity
07115. [x] tests\test_log_service.py:37 — revisar facet 'type hints presentes' em test_event_bus_sanity
07116. [x] tests\test_log_service.py:37 — revisar facet 'tratamento de erros adequado' em test_event_bus_sanity
07117. [x] tests\test_log_service.py:37 — revisar facet 'sem comentários inline desnecessários' em test_event_bus_sanity
07118. [x] tests\test_log_service.py:37 — revisar facet 'não imprime side-effects na UI/IO' em test_event_bus_sanity
07119. [x] tests\test_log_service.py:37 — revisar facet 'thread-safety revisada' em test_event_bus_sanity
07120. [x] tests\test_log_service.py:37 — revisar facet 'performance (sem loops O(n^2))' em test_event_bus_sanity
07121. [x] tests\test_log_service.py:37 — revisar facet 'coberto por testes' em test_event_bus_sanity
07122. [x] tests\test_log_service.py:38 — import: app.domain.events
07123. [x] tests\test_log_service.py:39 — import: app.infrastructure.event_bus
07124. [x] tests\test_log_service.py:41 — atribuição: test_event_bus_sanity ← bus
07125. [x] tests\test_log_service.py:42 — atribuição: test_event_bus_sanity ← received
07126. [x] Existência e estrutura do módulo: tests\test_parsing.py
07127. [x] tests\test_parsing.py:3 — import: pytest
07128. [x] tests\test_parsing.py:5 — import: app.core.parsing
07129. [x] tests\test_parsing.py:8 — atribuição:  ← TEMPLATE
07130. [x] tests\test_parsing.py:16 — definir/revisar FunctionDef: test_variation_forms_detected
07131. [x] tests\test_parsing.py:16 — revisar facet 'assinatura/args consistentes' em test_variation_forms_detected
07132. [x] tests\test_parsing.py:16 — revisar facet 'docstring em português' em test_variation_forms_detected
07133. [x] tests\test_parsing.py:16 — revisar facet 'nomenclatura clara (PEP8)' em test_variation_forms_detected
07134. [x] tests\test_parsing.py:16 — revisar facet 'type hints presentes' em test_variation_forms_detected
07135. [x] tests\test_parsing.py:16 — revisar facet 'tratamento de erros adequado' em test_variation_forms_detected
07136. [x] tests\test_parsing.py:16 — revisar facet 'sem comentários inline desnecessários' em test_variation_forms_detected
07137. [x] tests\test_parsing.py:16 — revisar facet 'não imprime side-effects na UI/IO' em test_variation_forms_detected
07138. [x] tests\test_parsing.py:16 — revisar facet 'thread-safety revisada' em test_variation_forms_detected
07139. [x] tests\test_parsing.py:16 — revisar facet 'performance (sem loops O(n^2))' em test_variation_forms_detected
07140. [x] tests\test_parsing.py:16 — revisar facet 'coberto por testes' em test_variation_forms_detected
07141. [x] tests\test_parsing.py:18 — atribuição: test_variation_forms_detected ← var_ids
07142. [x] tests\test_parsing.py:22 — definir/revisar FunctionDef: test_dollar_and_var_are_distinct_variables
07143. [x] tests\test_parsing.py:22 — revisar facet 'assinatura/args consistentes' em test_dollar_and_var_are_distinct_variables
07144. [x] tests\test_parsing.py:22 — revisar facet 'docstring em português' em test_dollar_and_var_are_distinct_variables
07145. [x] tests\test_parsing.py:22 — revisar facet 'nomenclatura clara (PEP8)' em test_dollar_and_var_are_distinct_variables
07146. [x] tests\test_parsing.py:22 — revisar facet 'type hints presentes' em test_dollar_and_var_are_distinct_variables
07147. [x] tests\test_parsing.py:22 — revisar facet 'tratamento de erros adequado' em test_dollar_and_var_are_distinct_variables
07148. [x] tests\test_parsing.py:22 — revisar facet 'sem comentários inline desnecessários' em test_dollar_and_var_are_distinct_variables
07149. [x] tests\test_parsing.py:22 — revisar facet 'não imprime side-effects na UI/IO' em test_dollar_and_var_are_distinct_variables
07150. [x] tests\test_parsing.py:22 — revisar facet 'thread-safety revisada' em test_dollar_and_var_are_distinct_variables
07151. [x] tests\test_parsing.py:22 — revisar facet 'performance (sem loops O(n^2))' em test_dollar_and_var_are_distinct_variables
07152. [x] tests\test_parsing.py:22 — revisar facet 'coberto por testes' em test_dollar_and_var_are_distinct_variables
07153. [x] tests\test_parsing.py:27 — definir/revisar FunctionDef: test_token_regex_does_not_match_prefix
07154. [x] tests\test_parsing.py:27 — revisar facet 'assinatura/args consistentes' em test_token_regex_does_not_match_prefix
07155. [x] tests\test_parsing.py:27 — revisar facet 'docstring em português' em test_token_regex_does_not_match_prefix
07156. [x] tests\test_parsing.py:27 — revisar facet 'nomenclatura clara (PEP8)' em test_token_regex_does_not_match_prefix
07157. [x] tests\test_parsing.py:27 — revisar facet 'type hints presentes' em test_token_regex_does_not_match_prefix
07158. [x] tests\test_parsing.py:27 — revisar facet 'tratamento de erros adequado' em test_token_regex_does_not_match_prefix
07159. [x] tests\test_parsing.py:27 — revisar facet 'sem comentários inline desnecessários' em test_token_regex_does_not_match_prefix
07160. [x] tests\test_parsing.py:27 — revisar facet 'não imprime side-effects na UI/IO' em test_token_regex_does_not_match_prefix
07161. [x] tests\test_parsing.py:27 — revisar facet 'thread-safety revisada' em test_token_regex_does_not_match_prefix
07162. [x] tests\test_parsing.py:27 — revisar facet 'performance (sem loops O(n^2))' em test_token_regex_does_not_match_prefix
07163. [x] tests\test_parsing.py:27 — revisar facet 'coberto por testes' em test_token_regex_does_not_match_prefix
07164. [x] tests\test_parsing.py:28 — atribuição: test_token_regex_does_not_match_prefix ← m
07165. [x] tests\test_parsing.py:30 — atribuição: test_token_regex_does_not_match_prefix ← d
07166. [x] tests\test_parsing.py:34 — definir/revisar FunctionDef: test_token_match_dollar_number
07167. [x] tests\test_parsing.py:34 — revisar facet 'assinatura/args consistentes' em test_token_match_dollar_number
07168. [x] tests\test_parsing.py:34 — revisar facet 'docstring em português' em test_token_match_dollar_number
07169. [x] tests\test_parsing.py:34 — revisar facet 'nomenclatura clara (PEP8)' em test_token_match_dollar_number
07170. [x] tests\test_parsing.py:34 — revisar facet 'type hints presentes' em test_token_match_dollar_number
07171. [x] tests\test_parsing.py:34 — revisar facet 'tratamento de erros adequado' em test_token_match_dollar_number
07172. [x] tests\test_parsing.py:34 — revisar facet 'sem comentários inline desnecessários' em test_token_match_dollar_number
07173. [x] tests\test_parsing.py:34 — revisar facet 'não imprime side-effects na UI/IO' em test_token_match_dollar_number
07174. [x] tests\test_parsing.py:34 — revisar facet 'thread-safety revisada' em test_token_match_dollar_number
07175. [x] tests\test_parsing.py:34 — revisar facet 'performance (sem loops O(n^2))' em test_token_match_dollar_number
07176. [x] tests\test_parsing.py:34 — revisar facet 'coberto por testes' em test_token_match_dollar_number
07177. [x] tests\test_parsing.py:35 — atribuição: test_token_match_dollar_number ← text
07178. [x] tests\test_parsing.py:36 — atribuição: test_token_match_dollar_number ← m
07179. [x] tests\test_parsing.py:40 — definir/revisar FunctionDef: test_render_template_substitutes_values
07180. [x] tests\test_parsing.py:40 — revisar facet 'assinatura/args consistentes' em test_render_template_substitutes_values
07181. [x] tests\test_parsing.py:40 — revisar facet 'docstring em português' em test_render_template_substitutes_values
07182. [x] tests\test_parsing.py:40 — revisar facet 'nomenclatura clara (PEP8)' em test_render_template_substitutes_values
07183. [x] tests\test_parsing.py:40 — revisar facet 'type hints presentes' em test_render_template_substitutes_values
07184. [x] tests\test_parsing.py:40 — revisar facet 'tratamento de erros adequado' em test_render_template_substitutes_values
07185. [x] tests\test_parsing.py:40 — revisar facet 'sem comentários inline desnecessários' em test_render_template_substitutes_values
07186. [x] tests\test_parsing.py:40 — revisar facet 'não imprime side-effects na UI/IO' em test_render_template_substitutes_values
07187. [x] tests\test_parsing.py:40 — revisar facet 'thread-safety revisada' em test_render_template_substitutes_values
07188. [x] tests\test_parsing.py:40 — revisar facet 'performance (sem loops O(n^2))' em test_render_template_substitutes_values
07189. [x] tests\test_parsing.py:40 — revisar facet 'coberto por testes' em test_render_template_substitutes_values
07190. [x] tests\test_parsing.py:41 — atribuição: test_render_template_substitutes_values ← text
07191. [x] tests\test_parsing.py:42 — atribuição: test_render_template_substitutes_values ← out
07192. [x] tests\test_parsing.py:49 — definir/revisar FunctionDef: test_render_template_missing_raises
07193. [x] tests\test_parsing.py:49 — revisar facet 'assinatura/args consistentes' em test_render_template_missing_raises
07194. [x] tests\test_parsing.py:49 — revisar facet 'docstring em português' em test_render_template_missing_raises
07195. [x] tests\test_parsing.py:49 — revisar facet 'nomenclatura clara (PEP8)' em test_render_template_missing_raises
07196. [x] tests\test_parsing.py:49 — revisar facet 'type hints presentes' em test_render_template_missing_raises
07197. [x] tests\test_parsing.py:49 — revisar facet 'tratamento de erros adequado' em test_render_template_missing_raises
07198. [x] tests\test_parsing.py:49 — revisar facet 'sem comentários inline desnecessários' em test_render_template_missing_raises
07199. [x] tests\test_parsing.py:49 — revisar facet 'não imprime side-effects na UI/IO' em test_render_template_missing_raises
07200. [x] tests\test_parsing.py:49 — revisar facet 'thread-safety revisada' em test_render_template_missing_raises
07201. [x] tests\test_parsing.py:49 — revisar facet 'performance (sem loops O(n^2))' em test_render_template_missing_raises
07202. [x] tests\test_parsing.py:49 — revisar facet 'coberto por testes' em test_render_template_missing_raises
07203. [x] tests\test_parsing.py:50 — controle with em test_render_template_missing_raises
07204. [x] tests\test_parsing.py:55 — definir/revisar FunctionDef: test_render_template_namespaced_values
07205. [x] tests\test_parsing.py:55 — revisar facet 'assinatura/args consistentes' em test_render_template_namespaced_values
07206. [x] tests\test_parsing.py:55 — revisar facet 'docstring em português' em test_render_template_namespaced_values
07207. [x] tests\test_parsing.py:55 — revisar facet 'nomenclatura clara (PEP8)' em test_render_template_namespaced_values
07208. [x] tests\test_parsing.py:55 — revisar facet 'type hints presentes' em test_render_template_namespaced_values
07209. [x] tests\test_parsing.py:55 — revisar facet 'tratamento de erros adequado' em test_render_template_namespaced_values
07210. [x] tests\test_parsing.py:55 — revisar facet 'sem comentários inline desnecessários' em test_render_template_namespaced_values
07211. [x] tests\test_parsing.py:55 — revisar facet 'não imprime side-effects na UI/IO' em test_render_template_namespaced_values
07212. [x] tests\test_parsing.py:55 — revisar facet 'thread-safety revisada' em test_render_template_namespaced_values
07213. [x] tests\test_parsing.py:55 — revisar facet 'performance (sem loops O(n^2))' em test_render_template_namespaced_values
07214. [x] tests\test_parsing.py:55 — revisar facet 'coberto por testes' em test_render_template_namespaced_values
07215. [x] tests\test_parsing.py:56 — atribuição: test_render_template_namespaced_values ← out
07216. [x] tests\test_parsing.py:61 — definir/revisar FunctionDef: test_var_label_roundtrip
07217. [x] tests\test_parsing.py:61 — revisar facet 'assinatura/args consistentes' em test_var_label_roundtrip
07218. [x] tests\test_parsing.py:61 — revisar facet 'docstring em português' em test_var_label_roundtrip
07219. [x] tests\test_parsing.py:61 — revisar facet 'nomenclatura clara (PEP8)' em test_var_label_roundtrip
07220. [x] tests\test_parsing.py:61 — revisar facet 'type hints presentes' em test_var_label_roundtrip
07221. [x] tests\test_parsing.py:61 — revisar facet 'tratamento de erros adequado' em test_var_label_roundtrip
07222. [x] tests\test_parsing.py:61 — revisar facet 'sem comentários inline desnecessários' em test_var_label_roundtrip
07223. [x] tests\test_parsing.py:61 — revisar facet 'não imprime side-effects na UI/IO' em test_var_label_roundtrip
07224. [x] tests\test_parsing.py:61 — revisar facet 'thread-safety revisada' em test_var_label_roundtrip
07225. [x] tests\test_parsing.py:61 — revisar facet 'performance (sem loops O(n^2))' em test_var_label_roundtrip
07226. [x] tests\test_parsing.py:61 — revisar facet 'coberto por testes' em test_var_label_roundtrip
07227. [x] tests\test_parsing.py:67 — definir/revisar FunctionDef: test_render_without_variables_unchanged
07228. [x] tests\test_parsing.py:67 — revisar facet 'assinatura/args consistentes' em test_render_without_variables_unchanged
07229. [x] tests\test_parsing.py:67 — revisar facet 'docstring em português' em test_render_without_variables_unchanged
07230. [x] tests\test_parsing.py:67 — revisar facet 'nomenclatura clara (PEP8)' em test_render_without_variables_unchanged
07231. [x] tests\test_parsing.py:67 — revisar facet 'type hints presentes' em test_render_without_variables_unchanged
07232. [x] tests\test_parsing.py:67 — revisar facet 'tratamento de erros adequado' em test_render_without_variables_unchanged
07233. [x] tests\test_parsing.py:67 — revisar facet 'sem comentários inline desnecessários' em test_render_without_variables_unchanged
07234. [x] tests\test_parsing.py:67 — revisar facet 'não imprime side-effects na UI/IO' em test_render_without_variables_unchanged
07235. [x] tests\test_parsing.py:67 — revisar facet 'thread-safety revisada' em test_render_without_variables_unchanged
07236. [x] tests\test_parsing.py:67 — revisar facet 'performance (sem loops O(n^2))' em test_render_without_variables_unchanged
07237. [x] tests\test_parsing.py:67 — revisar facet 'coberto por testes' em test_render_without_variables_unchanged
07238. [x] tests\test_parsing.py:68 — atribuição: test_render_without_variables_unchanged ← text
07239. [x] Existência e estrutura do módulo: tests\test_repositories.py
07240. [x] tests\test_repositories.py:3 — import: pytest
07241. [x] tests\test_repositories.py:6 — definir/revisar FunctionDef: test_experiment_repository_roundtrip
07242. [x] tests\test_repositories.py:6 — revisar facet 'assinatura/args consistentes' em test_experiment_repository_roundtrip
07243. [x] tests\test_repositories.py:6 — revisar facet 'docstring em português' em test_experiment_repository_roundtrip
07244. [x] tests\test_repositories.py:6 — revisar facet 'nomenclatura clara (PEP8)' em test_experiment_repository_roundtrip
07245. [x] tests\test_repositories.py:6 — revisar facet 'type hints presentes' em test_experiment_repository_roundtrip
07246. [x] tests\test_repositories.py:6 — revisar facet 'tratamento de erros adequado' em test_experiment_repository_roundtrip
07247. [x] tests\test_repositories.py:6 — revisar facet 'sem comentários inline desnecessários' em test_experiment_repository_roundtrip
07248. [x] tests\test_repositories.py:6 — revisar facet 'não imprime side-effects na UI/IO' em test_experiment_repository_roundtrip
07249. [x] tests\test_repositories.py:6 — revisar facet 'thread-safety revisada' em test_experiment_repository_roundtrip
07250. [x] tests\test_repositories.py:6 — revisar facet 'performance (sem loops O(n^2))' em test_experiment_repository_roundtrip
07251. [x] tests\test_repositories.py:6 — revisar facet 'coberto por testes' em test_experiment_repository_roundtrip
07252. [x] tests\test_repositories.py:7 — atribuição: test_experiment_repository_roundtrip ← exp
07253. [x] tests\test_repositories.py:12 — atribuição: test_experiment_repository_roundtrip ← var_ids
07254. [x] tests\test_repositories.py:15 — atribuição: test_experiment_repository_roundtrip ← page_rows
07255. [x] tests\test_repositories.py:19 — atribuição: test_experiment_repository_roundtrip ← values
07256. [x] tests\test_repositories.py:22 — atribuição: test_experiment_repository_roundtrip ← row
07257. [x] tests\test_repositories.py:26 — definir/revisar FunctionDef: test_template_repository_versions_and_current
07258. [x] tests\test_repositories.py:26 — revisar facet 'assinatura/args consistentes' em test_template_repository_versions_and_current
07259. [x] tests\test_repositories.py:26 — revisar facet 'docstring em português' em test_template_repository_versions_and_current
07260. [x] tests\test_repositories.py:26 — revisar facet 'nomenclatura clara (PEP8)' em test_template_repository_versions_and_current
07261. [x] tests\test_repositories.py:26 — revisar facet 'type hints presentes' em test_template_repository_versions_and_current
07262. [x] tests\test_repositories.py:26 — revisar facet 'tratamento de erros adequado' em test_template_repository_versions_and_current
07263. [x] tests\test_repositories.py:26 — revisar facet 'sem comentários inline desnecessários' em test_template_repository_versions_and_current
07264. [x] tests\test_repositories.py:26 — revisar facet 'não imprime side-effects na UI/IO' em test_template_repository_versions_and_current
07265. [x] tests\test_repositories.py:26 — revisar facet 'thread-safety revisada' em test_template_repository_versions_and_current
07266. [x] tests\test_repositories.py:26 — revisar facet 'performance (sem loops O(n^2))' em test_template_repository_versions_and_current
07267. [x] tests\test_repositories.py:26 — revisar facet 'coberto por testes' em test_template_repository_versions_and_current
07268. [x] tests\test_repositories.py:27 — atribuição: test_template_repository_versions_and_current ← tpl
07269. [x] tests\test_repositories.py:28 — atribuição: test_template_repository_versions_and_current ← template_id
07270. [x] tests\test_repositories.py:31 — atribuição: test_template_repository_versions_and_current ← v1
07271. [x] tests\test_repositories.py:32 — atribuição: test_template_repository_versions_and_current ← v2
07272. [x] tests\test_repositories.py:34 — atribuição: test_template_repository_versions_and_current ← versions
07273. [x] tests\test_repositories.py:37 — atribuição: test_template_repository_versions_and_current ← current
07274. [x] tests\test_repositories.py:43 — definir/revisar FunctionDef: test_template_repository_get_version
07275. [x] tests\test_repositories.py:43 — revisar facet 'assinatura/args consistentes' em test_template_repository_get_version
07276. [x] tests\test_repositories.py:43 — revisar facet 'docstring em português' em test_template_repository_get_version
07277. [x] tests\test_repositories.py:43 — revisar facet 'nomenclatura clara (PEP8)' em test_template_repository_get_version
07278. [x] tests\test_repositories.py:43 — revisar facet 'type hints presentes' em test_template_repository_get_version
07279. [x] tests\test_repositories.py:43 — revisar facet 'tratamento de erros adequado' em test_template_repository_get_version
07280. [x] tests\test_repositories.py:43 — revisar facet 'sem comentários inline desnecessários' em test_template_repository_get_version
07281. [x] tests\test_repositories.py:43 — revisar facet 'não imprime side-effects na UI/IO' em test_template_repository_get_version
07282. [x] tests\test_repositories.py:43 — revisar facet 'thread-safety revisada' em test_template_repository_get_version
07283. [x] tests\test_repositories.py:43 — revisar facet 'performance (sem loops O(n^2))' em test_template_repository_get_version
07284. [x] tests\test_repositories.py:43 — revisar facet 'coberto por testes' em test_template_repository_get_version
07285. [x] tests\test_repositories.py:44 — atribuição: test_template_repository_get_version ← tpl
07286. [x] tests\test_repositories.py:45 — atribuição: test_template_repository_get_version ← template_id
07287. [x] tests\test_repositories.py:46 — atribuição: test_template_repository_get_version ← version_id
07288. [x] tests\test_repositories.py:47 — atribuição: test_template_repository_get_version ← version
07289. [x] tests\test_repositories.py:52 — definir/revisar FunctionDef: test_task_repository_create_and_flow
07290. [x] tests\test_repositories.py:52 — revisar facet 'assinatura/args consistentes' em test_task_repository_create_and_flow
07291. [x] tests\test_repositories.py:52 — revisar facet 'docstring em português' em test_task_repository_create_and_flow
07292. [x] tests\test_repositories.py:52 — revisar facet 'nomenclatura clara (PEP8)' em test_task_repository_create_and_flow
07293. [x] tests\test_repositories.py:52 — revisar facet 'type hints presentes' em test_task_repository_create_and_flow
07294. [x] tests\test_repositories.py:52 — revisar facet 'tratamento de erros adequado' em test_task_repository_create_and_flow
07295. [x] tests\test_repositories.py:52 — revisar facet 'sem comentários inline desnecessários' em test_task_repository_create_and_flow
07296. [x] tests\test_repositories.py:52 — revisar facet 'não imprime side-effects na UI/IO' em test_task_repository_create_and_flow
07297. [x] tests\test_repositories.py:52 — revisar facet 'thread-safety revisada' em test_task_repository_create_and_flow
07298. [x] tests\test_repositories.py:52 — revisar facet 'performance (sem loops O(n^2))' em test_task_repository_create_and_flow
07299. [x] tests\test_repositories.py:52 — revisar facet 'coberto por testes' em test_task_repository_create_and_flow
07300. [x] tests\test_repositories.py:53 — import: app.domain.tasks
07301. [x] tests\test_repositories.py:54 — import: app.infrastructure.task_repository
07302. [x] tests\test_repositories.py:56 — atribuição: test_task_repository_create_and_flow ← repo
07303. [x] tests\test_repositories.py:58 — atribuição: test_task_repository_create_and_flow ← task
07304. [x] tests\test_repositories.py:61 — atribuição: test_task_repository_create_and_flow ← claimed
07305. [x] tests\test_repositories.py:66 — atribuição: test_task_repository_create_and_flow ← updated
07306. [x] tests\test_repositories.py:72 — atribuição: test_task_repository_create_and_flow ← done
07307. [x] tests\test_repositories.py:79 — definir/revisar FunctionDef: test_task_repository_fail_pause_recover
07308. [x] tests\test_repositories.py:79 — revisar facet 'assinatura/args consistentes' em test_task_repository_fail_pause_recover
07309. [x] tests\test_repositories.py:79 — revisar facet 'docstring em português' em test_task_repository_fail_pause_recover
07310. [x] tests\test_repositories.py:79 — revisar facet 'nomenclatura clara (PEP8)' em test_task_repository_fail_pause_recover
07311. [x] tests\test_repositories.py:79 — revisar facet 'type hints presentes' em test_task_repository_fail_pause_recover
07312. [x] tests\test_repositories.py:79 — revisar facet 'tratamento de erros adequado' em test_task_repository_fail_pause_recover
07313. [x] tests\test_repositories.py:79 — revisar facet 'sem comentários inline desnecessários' em test_task_repository_fail_pause_recover
07314. [x] tests\test_repositories.py:79 — revisar facet 'não imprime side-effects na UI/IO' em test_task_repository_fail_pause_recover
07315. [x] tests\test_repositories.py:79 — revisar facet 'thread-safety revisada' em test_task_repository_fail_pause_recover
07316. [x] tests\test_repositories.py:79 — revisar facet 'performance (sem loops O(n^2))' em test_task_repository_fail_pause_recover
07317. [x] tests\test_repositories.py:79 — revisar facet 'coberto por testes' em test_task_repository_fail_pause_recover
07318. [x] tests\test_repositories.py:80 — import: app.domain.tasks
07319. [x] tests\test_repositories.py:81 — import: app.infrastructure.task_repository
07320. [x] tests\test_repositories.py:83 — atribuição: test_task_repository_fail_pause_recover ← repo
07321. [x] tests\test_repositories.py:84 — atribuição: test_task_repository_fail_pause_recover ← t1
07322. [x] tests\test_repositories.py:85 — atribuição: test_task_repository_fail_pause_recover ← t2
07323. [x] tests\test_repositories.py:95 — atribuição: test_task_repository_fail_pause_recover ← recovered
07324. [x] tests\test_repositories.py:99 — atribuição: test_task_repository_fail_pause_recover ← task
07325. [x] Existência e estrutura do módulo: tests\test_sampling_service.py
07326. [x] tests\test_sampling_service.py:3 — import: numpy
07327. [x] tests\test_sampling_service.py:4 — import: pytest
07328. [x] tests\test_sampling_service.py:6 — import: app.domain.entities
07329. [x] tests\test_sampling_service.py:9 — definir/revisar FunctionDef: _spec_norm
07330. [x] tests\test_sampling_service.py:9 — revisar facet 'assinatura/args consistentes' em _spec_norm
07331. [x] tests\test_sampling_service.py:9 — revisar facet 'docstring em português' em _spec_norm
07332. [x] tests\test_sampling_service.py:9 — revisar facet 'nomenclatura clara (PEP8)' em _spec_norm
07333. [x] tests\test_sampling_service.py:9 — revisar facet 'type hints presentes' em _spec_norm
07334. [x] tests\test_sampling_service.py:9 — revisar facet 'tratamento de erros adequado' em _spec_norm
07335. [x] tests\test_sampling_service.py:9 — revisar facet 'sem comentários inline desnecessários' em _spec_norm
07336. [x] tests\test_sampling_service.py:9 — revisar facet 'não imprime side-effects na UI/IO' em _spec_norm
07337. [x] tests\test_sampling_service.py:9 — revisar facet 'thread-safety revisada' em _spec_norm
07338. [x] tests\test_sampling_service.py:9 — revisar facet 'performance (sem loops O(n^2))' em _spec_norm
07339. [x] tests\test_sampling_service.py:9 — revisar facet 'coberto por testes' em _spec_norm
07340. [x] tests\test_sampling_service.py:10 — return em _spec_norm
07341. [x] tests\test_sampling_service.py:13 — atribuição:  ← SPECS
07342. [x] tests\test_sampling_service.py:20 — definir/revisar FunctionDef: test_monte_carlo_shape_and_reproducibility
07343. [x] tests\test_sampling_service.py:20 — revisar facet 'assinatura/args consistentes' em test_monte_carlo_shape_and_reproducibility
07344. [x] tests\test_sampling_service.py:20 — revisar facet 'docstring em português' em test_monte_carlo_shape_and_reproducibility
07345. [x] tests\test_sampling_service.py:20 — revisar facet 'nomenclatura clara (PEP8)' em test_monte_carlo_shape_and_reproducibility
07346. [x] tests\test_sampling_service.py:20 — revisar facet 'type hints presentes' em test_monte_carlo_shape_and_reproducibility
07347. [x] tests\test_sampling_service.py:20 — revisar facet 'tratamento de erros adequado' em test_monte_carlo_shape_and_reproducibility
07348. [x] tests\test_sampling_service.py:20 — revisar facet 'sem comentários inline desnecessários' em test_monte_carlo_shape_and_reproducibility
07349. [x] tests\test_sampling_service.py:20 — revisar facet 'não imprime side-effects na UI/IO' em test_monte_carlo_shape_and_reproducibility
07350. [x] tests\test_sampling_service.py:20 — revisar facet 'thread-safety revisada' em test_monte_carlo_shape_and_reproducibility
07351. [x] tests\test_sampling_service.py:20 — revisar facet 'performance (sem loops O(n^2))' em test_monte_carlo_shape_and_reproducibility
07352. [x] tests\test_sampling_service.py:20 — revisar facet 'coberto por testes' em test_monte_carlo_shape_and_reproducibility
07353. [x] tests\test_sampling_service.py:21 — atribuição: test_monte_carlo_shape_and_reproducibility ← r1
07354. [x] tests\test_sampling_service.py:24 — atribuição: test_monte_carlo_shape_and_reproducibility ← r2
07355. [x] tests\test_sampling_service.py:33 — definir/revisar FunctionDef: test_lhs_marginals_reduced_dispersion
07356. [x] tests\test_sampling_service.py:33 — revisar facet 'assinatura/args consistentes' em test_lhs_marginals_reduced_dispersion
07357. [x] tests\test_sampling_service.py:33 — revisar facet 'docstring em português' em test_lhs_marginals_reduced_dispersion
07358. [x] tests\test_sampling_service.py:33 — revisar facet 'nomenclatura clara (PEP8)' em test_lhs_marginals_reduced_dispersion
07359. [x] tests\test_sampling_service.py:33 — revisar facet 'type hints presentes' em test_lhs_marginals_reduced_dispersion
07360. [x] tests\test_sampling_service.py:33 — revisar facet 'tratamento de erros adequado' em test_lhs_marginals_reduced_dispersion
07361. [x] tests\test_sampling_service.py:33 — revisar facet 'sem comentários inline desnecessários' em test_lhs_marginals_reduced_dispersion
07362. [x] tests\test_sampling_service.py:33 — revisar facet 'não imprime side-effects na UI/IO' em test_lhs_marginals_reduced_dispersion
07363. [x] tests\test_sampling_service.py:33 — revisar facet 'thread-safety revisada' em test_lhs_marginals_reduced_dispersion
07364. [x] tests\test_sampling_service.py:33 — revisar facet 'performance (sem loops O(n^2))' em test_lhs_marginals_reduced_dispersion
07365. [x] tests\test_sampling_service.py:33 — revisar facet 'coberto por testes' em test_lhs_marginals_reduced_dispersion
07366. [x] tests\test_sampling_service.py:34 — atribuição: test_lhs_marginals_reduced_dispersion ← lhs
07367. [x] tests\test_sampling_service.py:37 — atribuição: test_lhs_marginals_reduced_dispersion ← mc
07368. [x] tests\test_sampling_service.py:40 — atribuição: test_lhs_marginals_reduced_dispersion ← b_lhs
07369. [x] tests\test_sampling_service.py:41 — atribuição: test_lhs_marginals_reduced_dispersion ← b_mc
07370. [x] tests\test_sampling_service.py:43 — atribuição: test_lhs_marginals_reduced_dispersion ← per_bin_lhs
07371. [x] tests\test_sampling_service.py:44 — atribuição: test_lhs_marginals_reduced_dispersion ← values
07372. [x] tests\test_sampling_service.py:45 — atribuição: test_lhs_marginals_reduced_dispersion ← bins
07373. [x] tests\test_sampling_service.py:46 — controle for em test_lhs_marginals_reduced_dispersion
07374. [x] tests\test_sampling_service.py:47 — atribuição: test_lhs_marginals_reduced_dispersion ← ?
07375. [x] tests\test_sampling_service.py:52 — definir/revisar FunctionDef: test_empty_request_returns_empty
07376. [x] tests\test_sampling_service.py:52 — revisar facet 'assinatura/args consistentes' em test_empty_request_returns_empty
07377. [x] tests\test_sampling_service.py:52 — revisar facet 'docstring em português' em test_empty_request_returns_empty
07378. [x] tests\test_sampling_service.py:52 — revisar facet 'nomenclatura clara (PEP8)' em test_empty_request_returns_empty
07379. [x] tests\test_sampling_service.py:52 — revisar facet 'type hints presentes' em test_empty_request_returns_empty
07380. [x] tests\test_sampling_service.py:52 — revisar facet 'tratamento de erros adequado' em test_empty_request_returns_empty
07381. [x] tests\test_sampling_service.py:52 — revisar facet 'sem comentários inline desnecessários' em test_empty_request_returns_empty
07382. [x] tests\test_sampling_service.py:52 — revisar facet 'não imprime side-effects na UI/IO' em test_empty_request_returns_empty
07383. [x] tests\test_sampling_service.py:52 — revisar facet 'thread-safety revisada' em test_empty_request_returns_empty
07384. [x] tests\test_sampling_service.py:52 — revisar facet 'performance (sem loops O(n^2))' em test_empty_request_returns_empty
07385. [x] tests\test_sampling_service.py:52 — revisar facet 'coberto por testes' em test_empty_request_returns_empty
07386. [x] tests\test_sampling_service.py:53 — atribuição: test_empty_request_returns_empty ← result
07387. [x] tests\test_sampling_service.py:57 — atribuição: test_empty_request_returns_empty ← result
07388. [x] tests\test_sampling_service.py:63 — definir/revisar FunctionDef: test_unknown_strategy_raises
07389. [x] tests\test_sampling_service.py:63 — revisar facet 'assinatura/args consistentes' em test_unknown_strategy_raises
07390. [x] tests\test_sampling_service.py:63 — revisar facet 'docstring em português' em test_unknown_strategy_raises
07391. [x] tests\test_sampling_service.py:63 — revisar facet 'nomenclatura clara (PEP8)' em test_unknown_strategy_raises
07392. [x] tests\test_sampling_service.py:63 — revisar facet 'type hints presentes' em test_unknown_strategy_raises
07393. [x] tests\test_sampling_service.py:63 — revisar facet 'tratamento de erros adequado' em test_unknown_strategy_raises
07394. [x] tests\test_sampling_service.py:63 — revisar facet 'sem comentários inline desnecessários' em test_unknown_strategy_raises
07395. [x] tests\test_sampling_service.py:63 — revisar facet 'não imprime side-effects na UI/IO' em test_unknown_strategy_raises
07396. [x] tests\test_sampling_service.py:63 — revisar facet 'thread-safety revisada' em test_unknown_strategy_raises
07397. [x] tests\test_sampling_service.py:63 — revisar facet 'performance (sem loops O(n^2))' em test_unknown_strategy_raises
07398. [x] tests\test_sampling_service.py:63 — revisar facet 'coberto por testes' em test_unknown_strategy_raises
07399. [x] tests\test_sampling_service.py:64 — controle with em test_unknown_strategy_raises
07400. [x] tests\test_sampling_service.py:70 — definir/revisar FunctionDef: test_pearson_correlated
07401. [x] tests\test_sampling_service.py:70 — revisar facet 'assinatura/args consistentes' em test_pearson_correlated
07402. [x] tests\test_sampling_service.py:70 — revisar facet 'docstring em português' em test_pearson_correlated
07403. [x] tests\test_sampling_service.py:70 — revisar facet 'nomenclatura clara (PEP8)' em test_pearson_correlated
07404. [x] tests\test_sampling_service.py:70 — revisar facet 'type hints presentes' em test_pearson_correlated
07405. [x] tests\test_sampling_service.py:70 — revisar facet 'tratamento de erros adequado' em test_pearson_correlated
07406. [x] tests\test_sampling_service.py:70 — revisar facet 'sem comentários inline desnecessários' em test_pearson_correlated
07407. [x] tests\test_sampling_service.py:70 — revisar facet 'não imprime side-effects na UI/IO' em test_pearson_correlated
07408. [x] tests\test_sampling_service.py:70 — revisar facet 'thread-safety revisada' em test_pearson_correlated
07409. [x] tests\test_sampling_service.py:70 — revisar facet 'performance (sem loops O(n^2))' em test_pearson_correlated
07410. [x] tests\test_sampling_service.py:70 — revisar facet 'coberto por testes' em test_pearson_correlated
07411. [x] tests\test_sampling_service.py:71 — atribuição: test_pearson_correlated ← specs
07412. [x] tests\test_sampling_service.py:72 — atribuição: test_pearson_correlated ← result
07413. [x] tests\test_sampling_service.py:78 — atribuição: test_pearson_correlated ← matrix
07414. [x] tests\test_sampling_service.py:79 — atribuição: test_pearson_correlated ← pearson
07415. [x] tests\test_sampling_service.py:83 — definir/revisar FunctionDef: test_register_strategy_extensibility
07416. [x] tests\test_sampling_service.py:83 — revisar facet 'assinatura/args consistentes' em test_register_strategy_extensibility
07417. [x] tests\test_sampling_service.py:83 — revisar facet 'docstring em português' em test_register_strategy_extensibility
07418. [x] tests\test_sampling_service.py:83 — revisar facet 'nomenclatura clara (PEP8)' em test_register_strategy_extensibility
07419. [x] tests\test_sampling_service.py:83 — revisar facet 'type hints presentes' em test_register_strategy_extensibility
07420. [x] tests\test_sampling_service.py:83 — revisar facet 'tratamento de erros adequado' em test_register_strategy_extensibility
07421. [x] tests\test_sampling_service.py:83 — revisar facet 'sem comentários inline desnecessários' em test_register_strategy_extensibility
07422. [x] tests\test_sampling_service.py:83 — revisar facet 'não imprime side-effects na UI/IO' em test_register_strategy_extensibility
07423. [x] tests\test_sampling_service.py:83 — revisar facet 'thread-safety revisada' em test_register_strategy_extensibility
07424. [x] tests\test_sampling_service.py:83 — revisar facet 'performance (sem loops O(n^2))' em test_register_strategy_extensibility
07425. [x] tests\test_sampling_service.py:83 — revisar facet 'coberto por testes' em test_register_strategy_extensibility
07426. [x] tests\test_sampling_service.py:84 — definir/revisar ClassDef: test_register_strategy_extensibility.HaltonLike
07427. [x] tests\test_sampling_service.py:85 — atribuição: test_register_strategy_extensibility.HaltonLike ← name
07428. [x] tests\test_sampling_service.py:87 — definir/revisar FunctionDef: test_register_strategy_extensibility.HaltonLike.generate_uniforms
07429. [x] tests\test_sampling_service.py:87 — revisar facet 'assinatura/args consistentes' em test_register_strategy_extensibility.HaltonLike.generate_uniforms
07430. [x] tests\test_sampling_service.py:87 — revisar facet 'docstring em português' em test_register_strategy_extensibility.HaltonLike.generate_uniforms
07431. [x] tests\test_sampling_service.py:87 — revisar facet 'nomenclatura clara (PEP8)' em test_register_strategy_extensibility.HaltonLike.generate_uniforms
07432. [x] tests\test_sampling_service.py:87 — revisar facet 'type hints presentes' em test_register_strategy_extensibility.HaltonLike.generate_uniforms
07433. [x] tests\test_sampling_service.py:87 — revisar facet 'tratamento de erros adequado' em test_register_strategy_extensibility.HaltonLike.generate_uniforms
07434. [x] tests\test_sampling_service.py:87 — revisar facet 'sem comentários inline desnecessários' em test_register_strategy_extensibility.HaltonLike.generate_uniforms
07435. [x] tests\test_sampling_service.py:87 — revisar facet 'não imprime side-effects na UI/IO' em test_register_strategy_extensibility.HaltonLike.generate_uniforms
07436. [x] tests\test_sampling_service.py:87 — revisar facet 'thread-safety revisada' em test_register_strategy_extensibility.HaltonLike.generate_uniforms
07437. [x] tests\test_sampling_service.py:87 — revisar facet 'performance (sem loops O(n^2))' em test_register_strategy_extensibility.HaltonLike.generate_uniforms
07438. [x] tests\test_sampling_service.py:87 — revisar facet 'coberto por testes' em test_register_strategy_extensibility.HaltonLike.generate_uniforms
07439. [x] tests\test_sampling_service.py:88 — return em test_register_strategy_extensibility.HaltonLike.generate_uniforms
07440. [x] tests\test_sampling_service.py:91 — atribuição: test_register_strategy_extensibility ← result
07441. [x] Existência e estrutura do módulo: tests\test_task_scheduler.py
07442. [x] tests\test_task_scheduler.py:3 — import: pathlib
07443. [x] tests\test_task_scheduler.py:5 — import: pytest
07444. [x] tests\test_task_scheduler.py:7 — import: app.domain.tasks
07445. [x] tests\test_task_scheduler.py:10 — definir/revisar FunctionDef: _make_scheduler
07446. [x] tests\test_task_scheduler.py:10 — revisar facet 'assinatura/args consistentes' em _make_scheduler
07447. [x] tests\test_task_scheduler.py:10 — revisar facet 'docstring em português' em _make_scheduler
07448. [x] tests\test_task_scheduler.py:10 — revisar facet 'nomenclatura clara (PEP8)' em _make_scheduler
07449. [x] tests\test_task_scheduler.py:10 — revisar facet 'type hints presentes' em _make_scheduler
07450. [x] tests\test_task_scheduler.py:10 — revisar facet 'tratamento de erros adequado' em _make_scheduler
07451. [x] tests\test_task_scheduler.py:10 — revisar facet 'sem comentários inline desnecessários' em _make_scheduler
07452. [x] tests\test_task_scheduler.py:10 — revisar facet 'não imprime side-effects na UI/IO' em _make_scheduler
07453. [x] tests\test_task_scheduler.py:10 — revisar facet 'thread-safety revisada' em _make_scheduler
07454. [x] tests\test_task_scheduler.py:10 — revisar facet 'performance (sem loops O(n^2))' em _make_scheduler
07455. [x] tests\test_task_scheduler.py:10 — revisar facet 'coberto por testes' em _make_scheduler
07456. [x] tests\test_task_scheduler.py:11 — import: app.infrastructure.task_repository
07457. [x] tests\test_task_scheduler.py:12 — import: app.services.task_scheduler
07458. [x] tests\test_task_scheduler.py:14 — atribuição: _make_scheduler ← repo
07459. [x] tests\test_task_scheduler.py:15 — return em _make_scheduler
07460. [x] tests\test_task_scheduler.py:18 — definir/revisar FunctionDef: test_scheduler_execute_export
07461. [x] tests\test_task_scheduler.py:18 — revisar facet 'assinatura/args consistentes' em test_scheduler_execute_export
07462. [x] tests\test_task_scheduler.py:18 — revisar facet 'docstring em português' em test_scheduler_execute_export
07463. [x] tests\test_task_scheduler.py:18 — revisar facet 'nomenclatura clara (PEP8)' em test_scheduler_execute_export
07464. [x] tests\test_task_scheduler.py:18 — revisar facet 'type hints presentes' em test_scheduler_execute_export
07465. [x] tests\test_task_scheduler.py:18 — revisar facet 'tratamento de erros adequado' em test_scheduler_execute_export
07466. [x] tests\test_task_scheduler.py:18 — revisar facet 'sem comentários inline desnecessários' em test_scheduler_execute_export
07467. [x] tests\test_task_scheduler.py:18 — revisar facet 'não imprime side-effects na UI/IO' em test_scheduler_execute_export
07468. [x] tests\test_task_scheduler.py:18 — revisar facet 'thread-safety revisada' em test_scheduler_execute_export
07469. [x] tests\test_task_scheduler.py:18 — revisar facet 'performance (sem loops O(n^2))' em test_scheduler_execute_export
07470. [x] tests\test_task_scheduler.py:18 — revisar facet 'coberto por testes' em test_scheduler_execute_export
07471. [x] tests\test_task_scheduler.py:19 — atribuição: test_scheduler_execute_export ← scheduler
07472. [x] tests\test_task_scheduler.py:20 — atribuição: test_scheduler_execute_export ← task
07473. [x] tests\test_task_scheduler.py:27 — atribuição: test_scheduler_execute_export ← claimed
07474. [x] tests\test_task_scheduler.py:30 — atribuição: test_scheduler_execute_export ← progress_seen
07475. [x] tests\test_task_scheduler.py:40 — atribuição: test_scheduler_execute_export ← out
07476. [x] tests\test_task_scheduler.py:46 — definir/revisar FunctionDef: test_scheduler_pause_resume
07477. [x] tests\test_task_scheduler.py:46 — revisar facet 'assinatura/args consistentes' em test_scheduler_pause_resume
07478. [x] tests\test_task_scheduler.py:46 — revisar facet 'docstring em português' em test_scheduler_pause_resume
07479. [x] tests\test_task_scheduler.py:46 — revisar facet 'nomenclatura clara (PEP8)' em test_scheduler_pause_resume
07480. [x] tests\test_task_scheduler.py:46 — revisar facet 'type hints presentes' em test_scheduler_pause_resume
07481. [x] tests\test_task_scheduler.py:46 — revisar facet 'tratamento de erros adequado' em test_scheduler_pause_resume
07482. [x] tests\test_task_scheduler.py:46 — revisar facet 'sem comentários inline desnecessários' em test_scheduler_pause_resume
07483. [x] tests\test_task_scheduler.py:46 — revisar facet 'não imprime side-effects na UI/IO' em test_scheduler_pause_resume
07484. [x] tests\test_task_scheduler.py:46 — revisar facet 'thread-safety revisada' em test_scheduler_pause_resume
07485. [x] tests\test_task_scheduler.py:46 — revisar facet 'performance (sem loops O(n^2))' em test_scheduler_pause_resume
07486. [x] tests\test_task_scheduler.py:46 — revisar facet 'coberto por testes' em test_scheduler_pause_resume
07487. [x] tests\test_task_scheduler.py:47 — atribuição: test_scheduler_pause_resume ← scheduler
07488. [x] tests\test_task_scheduler.py:48 — atribuição: test_scheduler_pause_resume ← task
07489. [x] tests\test_task_scheduler.py:58 — definir/revisar FunctionDef: test_scheduler_unknown_kind_supported
07490. [x] tests\test_task_scheduler.py:58 — revisar facet 'assinatura/args consistentes' em test_scheduler_unknown_kind_supported
07491. [x] tests\test_task_scheduler.py:58 — revisar facet 'docstring em português' em test_scheduler_unknown_kind_supported
07492. [x] tests\test_task_scheduler.py:58 — revisar facet 'nomenclatura clara (PEP8)' em test_scheduler_unknown_kind_supported
07493. [x] tests\test_task_scheduler.py:58 — revisar facet 'type hints presentes' em test_scheduler_unknown_kind_supported
07494. [x] tests\test_task_scheduler.py:58 — revisar facet 'tratamento de erros adequado' em test_scheduler_unknown_kind_supported
07495. [x] tests\test_task_scheduler.py:58 — revisar facet 'sem comentários inline desnecessários' em test_scheduler_unknown_kind_supported
07496. [x] tests\test_task_scheduler.py:58 — revisar facet 'não imprime side-effects na UI/IO' em test_scheduler_unknown_kind_supported
07497. [x] tests\test_task_scheduler.py:58 — revisar facet 'thread-safety revisada' em test_scheduler_unknown_kind_supported
07498. [x] tests\test_task_scheduler.py:58 — revisar facet 'performance (sem loops O(n^2))' em test_scheduler_unknown_kind_supported
07499. [x] tests\test_task_scheduler.py:58 — revisar facet 'coberto por testes' em test_scheduler_unknown_kind_supported
07500. [x] tests\test_task_scheduler.py:59 — atribuição: test_scheduler_unknown_kind_supported ← scheduler
07501. [x] tests\test_task_scheduler.py:60 — atribuição: test_scheduler_unknown_kind_supported ← fake
07502. [x] tests\test_task_scheduler.py:61 — atribuição: test_scheduler_unknown_kind_supported ← ?
07503. [x] tests\test_task_scheduler.py:62 — controle with em test_scheduler_unknown_kind_supported
07504. [x] Existência e estrutura do módulo: tests\test_theme_export.py
07505. [x] tests\test_theme_export.py:3 — import: pytest
07506. [x] tests\test_theme_export.py:8 — definir/revisar FunctionDef: _qapp
07507. [x] tests\test_theme_export.py:8 — revisar facet 'assinatura/args consistentes' em _qapp
07508. [x] tests\test_theme_export.py:8 — revisar facet 'docstring em português' em _qapp
07509. [x] tests\test_theme_export.py:8 — revisar facet 'nomenclatura clara (PEP8)' em _qapp
07510. [x] tests\test_theme_export.py:8 — revisar facet 'type hints presentes' em _qapp
07511. [x] tests\test_theme_export.py:8 — revisar facet 'tratamento de erros adequado' em _qapp
07512. [x] tests\test_theme_export.py:8 — revisar facet 'sem comentários inline desnecessários' em _qapp
07513. [x] tests\test_theme_export.py:8 — revisar facet 'não imprime side-effects na UI/IO' em _qapp
07514. [x] tests\test_theme_export.py:8 — revisar facet 'thread-safety revisada' em _qapp
07515. [x] tests\test_theme_export.py:8 — revisar facet 'performance (sem loops O(n^2))' em _qapp
07516. [x] tests\test_theme_export.py:8 — revisar facet 'coberto por testes' em _qapp
07517. [x] tests\test_theme_export.py:9 — import: PySide6.QtWidgets
07518. [x] tests\test_theme_export.py:11 — return em _qapp
07519. [x] tests\test_theme_export.py:14 — definir/revisar FunctionDef: test_default_theme_is_dracula
07520. [x] tests\test_theme_export.py:14 — revisar facet 'assinatura/args consistentes' em test_default_theme_is_dracula
07521. [x] tests\test_theme_export.py:14 — revisar facet 'docstring em português' em test_default_theme_is_dracula
07522. [x] tests\test_theme_export.py:14 — revisar facet 'nomenclatura clara (PEP8)' em test_default_theme_is_dracula
07523. [x] tests\test_theme_export.py:14 — revisar facet 'type hints presentes' em test_default_theme_is_dracula
07524. [x] tests\test_theme_export.py:14 — revisar facet 'tratamento de erros adequado' em test_default_theme_is_dracula
07525. [x] tests\test_theme_export.py:14 — revisar facet 'sem comentários inline desnecessários' em test_default_theme_is_dracula
07526. [x] tests\test_theme_export.py:14 — revisar facet 'não imprime side-effects na UI/IO' em test_default_theme_is_dracula
07527. [x] tests\test_theme_export.py:14 — revisar facet 'thread-safety revisada' em test_default_theme_is_dracula
07528. [x] tests\test_theme_export.py:14 — revisar facet 'performance (sem loops O(n^2))' em test_default_theme_is_dracula
07529. [x] tests\test_theme_export.py:14 — revisar facet 'coberto por testes' em test_default_theme_is_dracula
07530. [x] tests\test_theme_export.py:15 — import: app.ui.editor.code_editor
07531. [x] tests\test_theme_export.py:17 — atribuição: test_default_theme_is_dracula ← editor
07532. [x] tests\test_theme_export.py:23 — definir/revisar FunctionDef: test_apply_theme_dracula_changes_background
07533. [x] tests\test_theme_export.py:23 — revisar facet 'assinatura/args consistentes' em test_apply_theme_dracula_changes_background
07534. [x] tests\test_theme_export.py:23 — revisar facet 'docstring em português' em test_apply_theme_dracula_changes_background
07535. [x] tests\test_theme_export.py:23 — revisar facet 'nomenclatura clara (PEP8)' em test_apply_theme_dracula_changes_background
07536. [x] tests\test_theme_export.py:23 — revisar facet 'type hints presentes' em test_apply_theme_dracula_changes_background
07537. [x] tests\test_theme_export.py:23 — revisar facet 'tratamento de erros adequado' em test_apply_theme_dracula_changes_background
07538. [x] tests\test_theme_export.py:23 — revisar facet 'sem comentários inline desnecessários' em test_apply_theme_dracula_changes_background
07539. [x] tests\test_theme_export.py:23 — revisar facet 'não imprime side-effects na UI/IO' em test_apply_theme_dracula_changes_background
07540. [x] tests\test_theme_export.py:23 — revisar facet 'thread-safety revisada' em test_apply_theme_dracula_changes_background
07541. [x] tests\test_theme_export.py:23 — revisar facet 'performance (sem loops O(n^2))' em test_apply_theme_dracula_changes_background
07542. [x] tests\test_theme_export.py:23 — revisar facet 'coberto por testes' em test_apply_theme_dracula_changes_background
07543. [x] tests\test_theme_export.py:24 — import: PySide6.QtGui
07544. [x] tests\test_theme_export.py:26 — import: app.ui.editor.code_editor
07545. [x] tests\test_theme_export.py:28 — atribuição: test_apply_theme_dracula_changes_background ← editor
07546. [x] tests\test_theme_export.py:31 — atribuição: test_apply_theme_dracula_changes_background ← color
07547. [x] tests\test_theme_export.py:37 — definir/revisar FunctionDef: test_highlighter_theme_formats_dracula
07548. [x] tests\test_theme_export.py:37 — revisar facet 'assinatura/args consistentes' em test_highlighter_theme_formats_dracula
07549. [x] tests\test_theme_export.py:37 — revisar facet 'docstring em português' em test_highlighter_theme_formats_dracula
07550. [x] tests\test_theme_export.py:37 — revisar facet 'nomenclatura clara (PEP8)' em test_highlighter_theme_formats_dracula
07551. [x] tests\test_theme_export.py:37 — revisar facet 'type hints presentes' em test_highlighter_theme_formats_dracula
07552. [x] tests\test_theme_export.py:37 — revisar facet 'tratamento de erros adequado' em test_highlighter_theme_formats_dracula
07553. [x] tests\test_theme_export.py:37 — revisar facet 'sem comentários inline desnecessários' em test_highlighter_theme_formats_dracula
07554. [x] tests\test_theme_export.py:37 — revisar facet 'não imprime side-effects na UI/IO' em test_highlighter_theme_formats_dracula
07555. [x] tests\test_theme_export.py:37 — revisar facet 'thread-safety revisada' em test_highlighter_theme_formats_dracula
07556. [x] tests\test_theme_export.py:37 — revisar facet 'performance (sem loops O(n^2))' em test_highlighter_theme_formats_dracula
07557. [x] tests\test_theme_export.py:37 — revisar facet 'coberto por testes' em test_highlighter_theme_formats_dracula
07558. [x] tests\test_theme_export.py:38 — import: PySide6.QtGui
07559. [x] tests\test_theme_export.py:40 — import: app.ui.editor.code_editor
07560. [x] tests\test_theme_export.py:41 — import: app.ui.editor.highlighter
07561. [x] tests\test_theme_export.py:43 — atribuição: test_highlighter_theme_formats_dracula ← editor
07562. [x] tests\test_theme_export.py:45 — atribuição: test_highlighter_theme_formats_dracula ← high
07563. [x] tests\test_theme_export.py:51 — definir/revisar FunctionDef: test_editor_widget_theme_signal
07564. [x] tests\test_theme_export.py:51 — revisar facet 'assinatura/args consistentes' em test_editor_widget_theme_signal
07565. [x] tests\test_theme_export.py:51 — revisar facet 'docstring em português' em test_editor_widget_theme_signal
07566. [x] tests\test_theme_export.py:51 — revisar facet 'nomenclatura clara (PEP8)' em test_editor_widget_theme_signal
07567. [x] tests\test_theme_export.py:51 — revisar facet 'type hints presentes' em test_editor_widget_theme_signal
07568. [x] tests\test_theme_export.py:51 — revisar facet 'tratamento de erros adequado' em test_editor_widget_theme_signal
07569. [x] tests\test_theme_export.py:51 — revisar facet 'sem comentários inline desnecessários' em test_editor_widget_theme_signal
07570. [x] tests\test_theme_export.py:51 — revisar facet 'não imprime side-effects na UI/IO' em test_editor_widget_theme_signal
07571. [x] tests\test_theme_export.py:51 — revisar facet 'thread-safety revisada' em test_editor_widget_theme_signal
07572. [x] tests\test_theme_export.py:51 — revisar facet 'performance (sem loops O(n^2))' em test_editor_widget_theme_signal
07573. [x] tests\test_theme_export.py:51 — revisar facet 'coberto por testes' em test_editor_widget_theme_signal
07574. [x] tests\test_theme_export.py:52 — import: app.ui.editor.editor_widget
07575. [x] tests\test_theme_export.py:54 — atribuição: test_editor_widget_theme_signal ← tab
07576. [x] tests\test_theme_export.py:56 — atribuição: test_editor_widget_theme_signal ← received
07577. [x] tests\test_theme_export.py:65 — definir/revisar FunctionDef: test_theme_persist_roundtrip
07578. [x] tests\test_theme_export.py:65 — revisar facet 'assinatura/args consistentes' em test_theme_persist_roundtrip
07579. [x] tests\test_theme_export.py:65 — revisar facet 'docstring em português' em test_theme_persist_roundtrip
07580. [x] tests\test_theme_export.py:65 — revisar facet 'nomenclatura clara (PEP8)' em test_theme_persist_roundtrip
07581. [x] tests\test_theme_export.py:65 — revisar facet 'type hints presentes' em test_theme_persist_roundtrip
07582. [x] tests\test_theme_export.py:65 — revisar facet 'tratamento de erros adequado' em test_theme_persist_roundtrip
07583. [x] tests\test_theme_export.py:65 — revisar facet 'sem comentários inline desnecessários' em test_theme_persist_roundtrip
07584. [x] tests\test_theme_export.py:65 — revisar facet 'não imprime side-effects na UI/IO' em test_theme_persist_roundtrip
07585. [x] tests\test_theme_export.py:65 — revisar facet 'thread-safety revisada' em test_theme_persist_roundtrip
07586. [x] tests\test_theme_export.py:65 — revisar facet 'performance (sem loops O(n^2))' em test_theme_persist_roundtrip
07587. [x] tests\test_theme_export.py:65 — revisar facet 'coberto por testes' em test_theme_persist_roundtrip
07588. [x] tests\test_theme_export.py:66 — import: app.ui.editor.themes
07589. [x] tests\test_theme_export.py:74 — definir/revisar FunctionDef: test_dollar_and_var_same_number_distinct
07590. [x] tests\test_theme_export.py:74 — revisar facet 'assinatura/args consistentes' em test_dollar_and_var_same_number_distinct
07591. [x] tests\test_theme_export.py:74 — revisar facet 'docstring em português' em test_dollar_and_var_same_number_distinct
07592. [x] tests\test_theme_export.py:74 — revisar facet 'nomenclatura clara (PEP8)' em test_dollar_and_var_same_number_distinct
07593. [x] tests\test_theme_export.py:74 — revisar facet 'type hints presentes' em test_dollar_and_var_same_number_distinct
07594. [x] tests\test_theme_export.py:74 — revisar facet 'tratamento de erros adequado' em test_dollar_and_var_same_number_distinct
07595. [x] tests\test_theme_export.py:74 — revisar facet 'sem comentários inline desnecessários' em test_dollar_and_var_same_number_distinct
07596. [x] tests\test_theme_export.py:74 — revisar facet 'não imprime side-effects na UI/IO' em test_dollar_and_var_same_number_distinct
07597. [x] tests\test_theme_export.py:74 — revisar facet 'thread-safety revisada' em test_dollar_and_var_same_number_distinct
07598. [x] tests\test_theme_export.py:74 — revisar facet 'performance (sem loops O(n^2))' em test_dollar_and_var_same_number_distinct
07599. [x] tests\test_theme_export.py:74 — revisar facet 'coberto por testes' em test_dollar_and_var_same_number_distinct
07600. [x] tests\test_theme_export.py:75 — import: app.core.parsing
07601. [x] tests\test_theme_export.py:80 — definir/revisar FunctionDef: test_highliqhter_colors_plain_vs_prefixed
07602. [x] tests\test_theme_export.py:80 — revisar facet 'assinatura/args consistentes' em test_highliqhter_colors_plain_vs_prefixed
07603. [x] tests\test_theme_export.py:80 — revisar facet 'docstring em português' em test_highliqhter_colors_plain_vs_prefixed
07604. [x] tests\test_theme_export.py:80 — revisar facet 'nomenclatura clara (PEP8)' em test_highliqhter_colors_plain_vs_prefixed
07605. [x] tests\test_theme_export.py:80 — revisar facet 'type hints presentes' em test_highliqhter_colors_plain_vs_prefixed
07606. [x] tests\test_theme_export.py:80 — revisar facet 'tratamento de erros adequado' em test_highliqhter_colors_plain_vs_prefixed
07607. [x] tests\test_theme_export.py:80 — revisar facet 'sem comentários inline desnecessários' em test_highliqhter_colors_plain_vs_prefixed
07608. [x] tests\test_theme_export.py:80 — revisar facet 'não imprime side-effects na UI/IO' em test_highliqhter_colors_plain_vs_prefixed
07609. [x] tests\test_theme_export.py:80 — revisar facet 'thread-safety revisada' em test_highliqhter_colors_plain_vs_prefixed
07610. [x] tests\test_theme_export.py:80 — revisar facet 'performance (sem loops O(n^2))' em test_highliqhter_colors_plain_vs_prefixed
07611. [x] tests\test_theme_export.py:80 — revisar facet 'coberto por testes' em test_highliqhter_colors_plain_vs_prefixed
07612. [x] tests\test_theme_export.py:81 — import: PySide6.QtGui
07613. [x] tests\test_theme_export.py:83 — import: app.ui.editor.code_editor
07614. [x] tests\test_theme_export.py:84 — import: app.ui.editor.highlighter
07615. [x] tests\test_theme_export.py:86 — atribuição: test_highliqhter_colors_plain_vs_prefixed ← editor
07616. [x] tests\test_theme_export.py:88 — atribuição: test_highliqhter_colors_plain_vs_prefixed ← high
07617. [x] tests\test_theme_export.py:97 — definir/revisar FunctionDef: test_export_done_dialog_opens_folder_in_explorer
07618. [x] tests\test_theme_export.py:97 — revisar facet 'assinatura/args consistentes' em test_export_done_dialog_opens_folder_in_explorer
07619. [x] tests\test_theme_export.py:97 — revisar facet 'docstring em português' em test_export_done_dialog_opens_folder_in_explorer
07620. [x] tests\test_theme_export.py:97 — revisar facet 'nomenclatura clara (PEP8)' em test_export_done_dialog_opens_folder_in_explorer
07621. [x] tests\test_theme_export.py:97 — revisar facet 'type hints presentes' em test_export_done_dialog_opens_folder_in_explorer
07622. [x] tests\test_theme_export.py:97 — revisar facet 'tratamento de erros adequado' em test_export_done_dialog_opens_folder_in_explorer
07623. [x] tests\test_theme_export.py:97 — revisar facet 'sem comentários inline desnecessários' em test_export_done_dialog_opens_folder_in_explorer
07624. [x] tests\test_theme_export.py:97 — revisar facet 'não imprime side-effects na UI/IO' em test_export_done_dialog_opens_folder_in_explorer
07625. [x] tests\test_theme_export.py:97 — revisar facet 'thread-safety revisada' em test_export_done_dialog_opens_folder_in_explorer
07626. [x] tests\test_theme_export.py:97 — revisar facet 'performance (sem loops O(n^2))' em test_export_done_dialog_opens_folder_in_explorer
07627. [x] tests\test_theme_export.py:97 — revisar facet 'coberto por testes' em test_export_done_dialog_opens_folder_in_explorer
07628. [x] tests\test_theme_export.py:98 — import: PySide6.QtCore
07629. [x] tests\test_theme_export.py:100 — atribuição: test_export_done_dialog_opens_folder_in_explorer ← opened
07630. [x] tests\test_theme_export.py:106 — import: app.ui.widgets.export_done_dialog
07631. [x] tests\test_theme_export.py:108 — atribuição: test_export_done_dialog_opens_folder_in_explorer ← destino
07632. [x] tests\test_theme_export.py:109 — atribuição: test_export_done_dialog_opens_folder_in_explorer ← dialog
07633. [x] tests\test_theme_export.py:113 — atribuição: test_export_done_dialog_opens_folder_in_explorer ← btn_open
07634. [x] tests\test_theme_export.py:121 — definir/revisar FunctionDef: test_export_done_dialog_manifest
07635. [x] tests\test_theme_export.py:121 — revisar facet 'assinatura/args consistentes' em test_export_done_dialog_manifest
07636. [x] tests\test_theme_export.py:121 — revisar facet 'docstring em português' em test_export_done_dialog_manifest
07637. [x] tests\test_theme_export.py:121 — revisar facet 'nomenclatura clara (PEP8)' em test_export_done_dialog_manifest
07638. [x] tests\test_theme_export.py:121 — revisar facet 'type hints presentes' em test_export_done_dialog_manifest
07639. [x] tests\test_theme_export.py:121 — revisar facet 'tratamento de erros adequado' em test_export_done_dialog_manifest
07640. [x] tests\test_theme_export.py:121 — revisar facet 'sem comentários inline desnecessários' em test_export_done_dialog_manifest
07641. [x] tests\test_theme_export.py:121 — revisar facet 'não imprime side-effects na UI/IO' em test_export_done_dialog_manifest
07642. [x] tests\test_theme_export.py:121 — revisar facet 'thread-safety revisada' em test_export_done_dialog_manifest
07643. [x] tests\test_theme_export.py:121 — revisar facet 'performance (sem loops O(n^2))' em test_export_done_dialog_manifest
07644. [x] tests\test_theme_export.py:121 — revisar facet 'coberto por testes' em test_export_done_dialog_manifest
07645. [x] tests\test_theme_export.py:122 — atribuição: test_export_done_dialog_manifest ← opened
07646. [x] tests\test_theme_export.py:127 — import: pathlib
07647. [x] tests\test_theme_export.py:128 — import: PySide6.QtCore
07648. [x] tests\test_theme_export.py:130 — import: app.ui.widgets.export_done_dialog
07649. [x] tests\test_theme_export.py:132 — atribuição: test_export_done_dialog_manifest ← destino
07650. [x] tests\test_theme_export.py:134 — atribuição: test_export_done_dialog_manifest ← manifest
07651. [x] tests\test_theme_export.py:137 — atribuição: test_export_done_dialog_manifest ← dialog
07652. [x] tests\test_theme_export.py:139 — atribuição: test_export_done_dialog_manifest ← buttons
07653. [x] tests\test_theme_export.py:142 — atribuição: test_export_done_dialog_manifest ← labels
07654. [x] tests\test_theme_export.py:145 — atribuição: test_export_done_dialog_manifest ← btn_manifest
07655. [x] Existência e estrutura do módulo: tests\test_ui_qt.py
07656. [x] tests\test_ui_qt.py:3 — import: pytest
07657. [x] tests\test_ui_qt.py:9 — definir/revisar FunctionDef: qapp
07658. [x] tests\test_ui_qt.py:9 — revisar facet 'assinatura/args consistentes' em qapp
07659. [x] tests\test_ui_qt.py:9 — revisar facet 'docstring em português' em qapp
07660. [x] tests\test_ui_qt.py:9 — revisar facet 'nomenclatura clara (PEP8)' em qapp
07661. [x] tests\test_ui_qt.py:9 — revisar facet 'type hints presentes' em qapp
07662. [x] tests\test_ui_qt.py:9 — revisar facet 'tratamento de erros adequado' em qapp
07663. [x] tests\test_ui_qt.py:9 — revisar facet 'sem comentários inline desnecessários' em qapp
07664. [x] tests\test_ui_qt.py:9 — revisar facet 'não imprime side-effects na UI/IO' em qapp
07665. [x] tests\test_ui_qt.py:9 — revisar facet 'thread-safety revisada' em qapp
07666. [x] tests\test_ui_qt.py:9 — revisar facet 'performance (sem loops O(n^2))' em qapp
07667. [x] tests\test_ui_qt.py:9 — revisar facet 'coberto por testes' em qapp
07668. [x] tests\test_ui_qt.py:10 — import: PySide6.QtWidgets
07669. [x] tests\test_ui_qt.py:12 — atribuição: qapp ← app
07670. [x] tests\test_ui_qt.py:16 — definir/revisar FunctionDef: test_editor_widget_content_and_readonly
07671. [x] tests\test_ui_qt.py:16 — revisar facet 'assinatura/args consistentes' em test_editor_widget_content_and_readonly
07672. [x] tests\test_ui_qt.py:16 — revisar facet 'docstring em português' em test_editor_widget_content_and_readonly
07673. [x] tests\test_ui_qt.py:16 — revisar facet 'nomenclatura clara (PEP8)' em test_editor_widget_content_and_readonly
07674. [x] tests\test_ui_qt.py:16 — revisar facet 'type hints presentes' em test_editor_widget_content_and_readonly
07675. [x] tests\test_ui_qt.py:16 — revisar facet 'tratamento de erros adequado' em test_editor_widget_content_and_readonly
07676. [x] tests\test_ui_qt.py:16 — revisar facet 'sem comentários inline desnecessários' em test_editor_widget_content_and_readonly
07677. [x] tests\test_ui_qt.py:16 — revisar facet 'não imprime side-effects na UI/IO' em test_editor_widget_content_and_readonly
07678. [x] tests\test_ui_qt.py:16 — revisar facet 'thread-safety revisada' em test_editor_widget_content_and_readonly
07679. [x] tests\test_ui_qt.py:16 — revisar facet 'performance (sem loops O(n^2))' em test_editor_widget_content_and_readonly
07680. [x] tests\test_ui_qt.py:16 — revisar facet 'coberto por testes' em test_editor_widget_content_and_readonly
07681. [x] tests\test_ui_qt.py:17 — import: app.ui.editor.editor_widget
07682. [x] tests\test_ui_qt.py:19 — atribuição: test_editor_widget_content_and_readonly ← tab
07683. [x] tests\test_ui_qt.py:27 — definir/revisar FunctionDef: test_editor_tokenize_sidebar_numbers
07684. [x] tests\test_ui_qt.py:27 — revisar facet 'assinatura/args consistentes' em test_editor_tokenize_sidebar_numbers
07685. [x] tests\test_ui_qt.py:27 — revisar facet 'docstring em português' em test_editor_tokenize_sidebar_numbers
07686. [x] tests\test_ui_qt.py:27 — revisar facet 'nomenclatura clara (PEP8)' em test_editor_tokenize_sidebar_numbers
07687. [x] tests\test_ui_qt.py:27 — revisar facet 'type hints presentes' em test_editor_tokenize_sidebar_numbers
07688. [x] tests\test_ui_qt.py:27 — revisar facet 'tratamento de erros adequado' em test_editor_tokenize_sidebar_numbers
07689. [x] tests\test_ui_qt.py:27 — revisar facet 'sem comentários inline desnecessários' em test_editor_tokenize_sidebar_numbers
07690. [x] tests\test_ui_qt.py:27 — revisar facet 'não imprime side-effects na UI/IO' em test_editor_tokenize_sidebar_numbers
07691. [x] tests\test_ui_qt.py:27 — revisar facet 'thread-safety revisada' em test_editor_tokenize_sidebar_numbers
07692. [x] tests\test_ui_qt.py:27 — revisar facet 'performance (sem loops O(n^2))' em test_editor_tokenize_sidebar_numbers
07693. [x] tests\test_ui_qt.py:27 — revisar facet 'coberto por testes' em test_editor_tokenize_sidebar_numbers
07694. [x] tests\test_ui_qt.py:28 — import: app.ui.editor.code_editor
07695. [x] tests\test_ui_qt.py:30 — atribuição: test_editor_tokenize_sidebar_numbers ← editor
07696. [x] tests\test_ui_qt.py:36 — definir/revisar FunctionDef: test_find_replace
07697. [x] tests\test_ui_qt.py:36 — revisar facet 'assinatura/args consistentes' em test_find_replace
07698. [x] tests\test_ui_qt.py:36 — revisar facet 'docstring em português' em test_find_replace
07699. [x] tests\test_ui_qt.py:36 — revisar facet 'nomenclatura clara (PEP8)' em test_find_replace
07700. [x] tests\test_ui_qt.py:36 — revisar facet 'type hints presentes' em test_find_replace
07701. [x] tests\test_ui_qt.py:36 — revisar facet 'tratamento de erros adequado' em test_find_replace
07702. [x] tests\test_ui_qt.py:36 — revisar facet 'sem comentários inline desnecessários' em test_find_replace
07703. [x] tests\test_ui_qt.py:36 — revisar facet 'não imprime side-effects na UI/IO' em test_find_replace
07704. [x] tests\test_ui_qt.py:36 — revisar facet 'thread-safety revisada' em test_find_replace
07705. [x] tests\test_ui_qt.py:36 — revisar facet 'performance (sem loops O(n^2))' em test_find_replace
07706. [x] tests\test_ui_qt.py:36 — revisar facet 'coberto por testes' em test_find_replace
07707. [x] tests\test_ui_qt.py:37 — import: app.ui.editor.editor_widget
07708. [x] tests\test_ui_qt.py:39 — atribuição: test_find_replace ← tab
07709. [x] tests\test_ui_qt.py:51 — definir/revisar FunctionDef: test_editor_tabs_open_close
07710. [x] tests\test_ui_qt.py:51 — revisar facet 'assinatura/args consistentes' em test_editor_tabs_open_close
07711. [x] tests\test_ui_qt.py:51 — revisar facet 'docstring em português' em test_editor_tabs_open_close
07712. [x] tests\test_ui_qt.py:51 — revisar facet 'nomenclatura clara (PEP8)' em test_editor_tabs_open_close
07713. [x] tests\test_ui_qt.py:51 — revisar facet 'type hints presentes' em test_editor_tabs_open_close
07714. [x] tests\test_ui_qt.py:51 — revisar facet 'tratamento de erros adequado' em test_editor_tabs_open_close
07715. [x] tests\test_ui_qt.py:51 — revisar facet 'sem comentários inline desnecessários' em test_editor_tabs_open_close
07716. [x] tests\test_ui_qt.py:51 — revisar facet 'não imprime side-effects na UI/IO' em test_editor_tabs_open_close
07717. [x] tests\test_ui_qt.py:51 — revisar facet 'thread-safety revisada' em test_editor_tabs_open_close
07718. [x] tests\test_ui_qt.py:51 — revisar facet 'performance (sem loops O(n^2))' em test_editor_tabs_open_close
07719. [x] tests\test_ui_qt.py:51 — revisar facet 'coberto por testes' em test_editor_tabs_open_close
07720. [x] tests\test_ui_qt.py:52 — import: app.ui.editor.editor_tabs
07721. [x] tests\test_ui_qt.py:54 — atribuição: test_editor_tabs_open_close ← file_path
07722. [x] tests\test_ui_qt.py:57 — atribuição: test_editor_tabs_open_close ← tabs
07723. [x] tests\test_ui_qt.py:59 — atribuição: test_editor_tabs_open_close ← tab
07724. [x] tests\test_ui_qt.py:63 — atribuição: test_editor_tabs_open_close ← same
07725. [x] tests\test_ui_qt.py:71 — definir/revisar FunctionDef: test_variables_panel_tokens
07726. [x] tests\test_ui_qt.py:71 — revisar facet 'assinatura/args consistentes' em test_variables_panel_tokens
07727. [x] tests\test_ui_qt.py:71 — revisar facet 'docstring em português' em test_variables_panel_tokens
07728. [x] tests\test_ui_qt.py:71 — revisar facet 'nomenclatura clara (PEP8)' em test_variables_panel_tokens
07729. [x] tests\test_ui_qt.py:71 — revisar facet 'type hints presentes' em test_variables_panel_tokens
07730. [x] tests\test_ui_qt.py:71 — revisar facet 'tratamento de erros adequado' em test_variables_panel_tokens
07731. [x] tests\test_ui_qt.py:71 — revisar facet 'sem comentários inline desnecessários' em test_variables_panel_tokens
07732. [x] tests\test_ui_qt.py:71 — revisar facet 'não imprime side-effects na UI/IO' em test_variables_panel_tokens
07733. [x] tests\test_ui_qt.py:71 — revisar facet 'thread-safety revisada' em test_variables_panel_tokens
07734. [x] tests\test_ui_qt.py:71 — revisar facet 'performance (sem loops O(n^2))' em test_variables_panel_tokens
07735. [x] tests\test_ui_qt.py:71 — revisar facet 'coberto por testes' em test_variables_panel_tokens
07736. [x] tests\test_ui_qt.py:72 — import: app.ui.widgets.variables_panel
07737. [x] tests\test_ui_qt.py:74 — atribuição: test_variables_panel_tokens ← panel
07738. [x] tests\test_ui_qt.py:76 — atribuição: test_variables_panel_tokens ← var_ids
07739. [x] tests\test_ui_qt.py:79 — atribuição: test_variables_panel_tokens ← labels
07740. [x] tests\test_ui_qt.py:83 — definir/revisar FunctionDef: test_highlighter_rehighlight
07741. [x] tests\test_ui_qt.py:83 — revisar facet 'assinatura/args consistentes' em test_highlighter_rehighlight
07742. [x] tests\test_ui_qt.py:83 — revisar facet 'docstring em português' em test_highlighter_rehighlight
07743. [x] tests\test_ui_qt.py:83 — revisar facet 'nomenclatura clara (PEP8)' em test_highlighter_rehighlight
07744. [x] tests\test_ui_qt.py:83 — revisar facet 'type hints presentes' em test_highlighter_rehighlight
07745. [x] tests\test_ui_qt.py:83 — revisar facet 'tratamento de erros adequado' em test_highlighter_rehighlight
07746. [x] tests\test_ui_qt.py:83 — revisar facet 'sem comentários inline desnecessários' em test_highlighter_rehighlight
07747. [x] tests\test_ui_qt.py:83 — revisar facet 'não imprime side-effects na UI/IO' em test_highlighter_rehighlight
07748. [x] tests\test_ui_qt.py:83 — revisar facet 'thread-safety revisada' em test_highlighter_rehighlight
07749. [x] tests\test_ui_qt.py:83 — revisar facet 'performance (sem loops O(n^2))' em test_highlighter_rehighlight
07750. [x] tests\test_ui_qt.py:83 — revisar facet 'coberto por testes' em test_highlighter_rehighlight
07751. [x] tests\test_ui_qt.py:84 — import: app.ui.editor.code_editor
07752. [x] tests\test_ui_qt.py:85 — import: app.ui.editor.highlighter
07753. [x] tests\test_ui_qt.py:87 — atribuição: test_highlighter_rehighlight ← editor
07754. [x] tests\test_ui_qt.py:89 — atribuição: test_highlighter_rehighlight ← high
07755. [x] tests\test_ui_qt.py:95 — definir/revisar FunctionDef: test_experiments_panel_pagination
07756. [x] tests\test_ui_qt.py:95 — revisar facet 'assinatura/args consistentes' em test_experiments_panel_pagination
07757. [x] tests\test_ui_qt.py:95 — revisar facet 'docstring em português' em test_experiments_panel_pagination
07758. [x] tests\test_ui_qt.py:95 — revisar facet 'nomenclatura clara (PEP8)' em test_experiments_panel_pagination
07759. [x] tests\test_ui_qt.py:95 — revisar facet 'type hints presentes' em test_experiments_panel_pagination
07760. [x] tests\test_ui_qt.py:95 — revisar facet 'tratamento de erros adequado' em test_experiments_panel_pagination
07761. [x] tests\test_ui_qt.py:95 — revisar facet 'sem comentários inline desnecessários' em test_experiments_panel_pagination
07762. [x] tests\test_ui_qt.py:95 — revisar facet 'não imprime side-effects na UI/IO' em test_experiments_panel_pagination
07763. [x] tests\test_ui_qt.py:95 — revisar facet 'thread-safety revisada' em test_experiments_panel_pagination
07764. [x] tests\test_ui_qt.py:95 — revisar facet 'performance (sem loops O(n^2))' em test_experiments_panel_pagination
07765. [x] tests\test_ui_qt.py:95 — revisar facet 'coberto por testes' em test_experiments_panel_pagination
07766. [x] tests\test_ui_qt.py:96 — import: app.ui.models.repository_paged_model
07767. [x] tests\test_ui_qt.py:97 — import: app.ui.widgets.experiments_panel
07768. [x] tests\test_ui_qt.py:99 — atribuição: test_experiments_panel_pagination ← model
07769. [x] tests\test_ui_qt.py:100 — atribuição: test_experiments_panel_pagination ← panel
07770. [x] tests\test_ui_qt.py:115 — definir/revisar FunctionDef: test_main_window_instantiation
07771. [x] tests\test_ui_qt.py:115 — revisar facet 'assinatura/args consistentes' em test_main_window_instantiation
07772. [x] tests\test_ui_qt.py:115 — revisar facet 'docstring em português' em test_main_window_instantiation
07773. [x] tests\test_ui_qt.py:115 — revisar facet 'nomenclatura clara (PEP8)' em test_main_window_instantiation
07774. [x] tests\test_ui_qt.py:115 — revisar facet 'type hints presentes' em test_main_window_instantiation
07775. [x] tests\test_ui_qt.py:115 — revisar facet 'tratamento de erros adequado' em test_main_window_instantiation
07776. [x] tests\test_ui_qt.py:115 — revisar facet 'sem comentários inline desnecessários' em test_main_window_instantiation
07777. [x] tests\test_ui_qt.py:115 — revisar facet 'não imprime side-effects na UI/IO' em test_main_window_instantiation
07778. [x] tests\test_ui_qt.py:115 — revisar facet 'thread-safety revisada' em test_main_window_instantiation
07779. [x] tests\test_ui_qt.py:115 — revisar facet 'performance (sem loops O(n^2))' em test_main_window_instantiation
07780. [x] tests\test_ui_qt.py:115 — revisar facet 'coberto por testes' em test_main_window_instantiation
07781. [x] tests\test_ui_qt.py:116 — import: app.container
07782. [x] tests\test_ui_qt.py:117 — import: app.ui.main_window
07783. [x] tests\test_ui_qt.py:119 — atribuição: test_main_window_instantiation ← container
07784. [x] tests\test_ui_qt.py:120 — atribuição: test_main_window_instantiation ← window
07785. [x] tests\test_ui_qt.py:124 — atribuição: test_main_window_instantiation ← editor
07786. [x] tests\test_ui_qt.py:130 — import: PySide6.QtWidgets
07787. [x] Existência e estrutura do módulo: tests\test_workers.py
07788. [x] tests\test_workers.py:3 — import: pytest
07789. [x] tests\test_workers.py:7 — import: app.domain.entities
07790. [x] tests\test_workers.py:10 — definir/revisar FunctionDef: test_sampling_worker_run_to_completion
07791. [x] tests\test_workers.py:10 — revisar facet 'assinatura/args consistentes' em test_sampling_worker_run_to_completion
07792. [x] tests\test_workers.py:10 — revisar facet 'docstring em português' em test_sampling_worker_run_to_completion
07793. [x] tests\test_workers.py:10 — revisar facet 'nomenclatura clara (PEP8)' em test_sampling_worker_run_to_completion
07794. [x] tests\test_workers.py:10 — revisar facet 'type hints presentes' em test_sampling_worker_run_to_completion
07795. [x] tests\test_workers.py:10 — revisar facet 'tratamento de erros adequado' em test_sampling_worker_run_to_completion
07796. [x] tests\test_workers.py:10 — revisar facet 'sem comentários inline desnecessários' em test_sampling_worker_run_to_completion
07797. [x] tests\test_workers.py:10 — revisar facet 'não imprime side-effects na UI/IO' em test_sampling_worker_run_to_completion
07798. [x] tests\test_workers.py:10 — revisar facet 'thread-safety revisada' em test_sampling_worker_run_to_completion
07799. [x] tests\test_workers.py:10 — revisar facet 'performance (sem loops O(n^2))' em test_sampling_worker_run_to_completion
07800. [x] tests\test_workers.py:10 — revisar facet 'coberto por testes' em test_sampling_worker_run_to_completion
07801. [x] tests\test_workers.py:11 — import: PySide6.QtCore
07802. [x] tests\test_workers.py:13 — import: app.infrastructure.distribution_registry
07803. [x] tests\test_workers.py:14 — import: app.services.sampling_service
07804. [x] tests\test_workers.py:15 — import: app.workers.sampling_worker
07805. [x] tests\test_workers.py:17 — definir/revisar ClassDef: test_sampling_worker_run_to_completion.Capture
07806. [x] tests\test_workers.py:18 — definir/revisar FunctionDef: test_sampling_worker_run_to_completion.Capture.__init__
07807. [x] tests\test_workers.py:18 — revisar facet 'assinatura/args consistentes' em test_sampling_worker_run_to_completion.Capture.__init__
07808. [x] tests\test_workers.py:18 — revisar facet 'docstring em português' em test_sampling_worker_run_to_completion.Capture.__init__
07809. [x] tests\test_workers.py:18 — revisar facet 'nomenclatura clara (PEP8)' em test_sampling_worker_run_to_completion.Capture.__init__
07810. [x] tests\test_workers.py:18 — revisar facet 'type hints presentes' em test_sampling_worker_run_to_completion.Capture.__init__
07811. [x] tests\test_workers.py:18 — revisar facet 'tratamento de erros adequado' em test_sampling_worker_run_to_completion.Capture.__init__
07812. [x] tests\test_workers.py:18 — revisar facet 'sem comentários inline desnecessários' em test_sampling_worker_run_to_completion.Capture.__init__
07813. [x] tests\test_workers.py:18 — revisar facet 'não imprime side-effects na UI/IO' em test_sampling_worker_run_to_completion.Capture.__init__
07814. [x] tests\test_workers.py:18 — revisar facet 'thread-safety revisada' em test_sampling_worker_run_to_completion.Capture.__init__
07815. [x] tests\test_workers.py:18 — revisar facet 'performance (sem loops O(n^2))' em test_sampling_worker_run_to_completion.Capture.__init__
07816. [x] tests\test_workers.py:18 — revisar facet 'coberto por testes' em test_sampling_worker_run_to_completion.Capture.__init__
07817. [x] tests\test_workers.py:20 — atribuição: test_sampling_worker_run_to_completion.Capture.__init__ ← ?
07818. [x] tests\test_workers.py:23 — definir/revisar FunctionDef: test_sampling_worker_run_to_completion.Capture.on_completed
07819. [x] tests\test_workers.py:23 — revisar facet 'assinatura/args consistentes' em test_sampling_worker_run_to_completion.Capture.on_completed
07820. [x] tests\test_workers.py:23 — revisar facet 'docstring em português' em test_sampling_worker_run_to_completion.Capture.on_completed
07821. [x] tests\test_workers.py:23 — revisar facet 'nomenclatura clara (PEP8)' em test_sampling_worker_run_to_completion.Capture.on_completed
07822. [x] tests\test_workers.py:23 — revisar facet 'type hints presentes' em test_sampling_worker_run_to_completion.Capture.on_completed
07823. [x] tests\test_workers.py:23 — revisar facet 'tratamento de erros adequado' em test_sampling_worker_run_to_completion.Capture.on_completed
07824. [x] tests\test_workers.py:23 — revisar facet 'sem comentários inline desnecessários' em test_sampling_worker_run_to_completion.Capture.on_completed
07825. [x] tests\test_workers.py:23 — revisar facet 'não imprime side-effects na UI/IO' em test_sampling_worker_run_to_completion.Capture.on_completed
07826. [x] tests\test_workers.py:23 — revisar facet 'thread-safety revisada' em test_sampling_worker_run_to_completion.Capture.on_completed
07827. [x] tests\test_workers.py:23 — revisar facet 'performance (sem loops O(n^2))' em test_sampling_worker_run_to_completion.Capture.on_completed
07828. [x] tests\test_workers.py:23 — revisar facet 'coberto por testes' em test_sampling_worker_run_to_completion.Capture.on_completed
07829. [x] tests\test_workers.py:26 — atribuição: test_sampling_worker_run_to_completion ← specs
07830. [x] tests\test_workers.py:30 — atribuição: test_sampling_worker_run_to_completion ← request
07831. [x] tests\test_workers.py:31 — atribuição: test_sampling_worker_run_to_completion ← worker
07832. [x] tests\test_workers.py:32 — atribuição: test_sampling_worker_run_to_completion ← cap
