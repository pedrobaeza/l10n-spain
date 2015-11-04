.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

==========================================
Gestión de las periodificaciones españolas
==========================================

La periodificación es un instrumento contable para cumplir con el principio de
devengo e imputar en cada ejercicio únicamente los ingresos y gastos que le
correspondan cuando los mismos son de aplicación a un periodo más largo que el
del propio ejercicio.

Por ejemplo, el pago de un seguro anual en mitad del ejercicio se debería
periodificar para que sólo la parte proporcional de ese seguro que corresponde
al ejercicio se tenga en cuenta para los informes de situación, y el resto
se deje para el año siguiente.

Este módulo incorpora pequeñas facilidades a la funcionalidad ya existente en
el módulo comunitario:

* Cuentas contables por defecto.
* Instrucciones de uso en este archivo.

Instalación
===========

Este módulo requiere para su instalación del módulo *account_cutoff_prepaid*,
que se encuentra en https://github.com/OCA/account-closing.

Uso
===

Para poder realizar periodificaciones, es conveniente crear productos que
tengan marcada la casilla "Debe rellenar fecha de inicio y de fin", para asi
evitar olvidar esos datos.

Las imputaciones de gastos/ingresos se haran de la manera convencional via
facturas de proveedor/cliente, pero indicando en las nuevas columnas la fecha
de inicio y de fin para las que se aplica el mismo.

Antes de realizar el cierre de ejercicio fiscal, habra que ir al menú
*Contabilidad > Procesamiento periódico > Operaciones de cierre*, y ahí entrar
en *Ingreso anticipado* o *Gasto anticipado* dependiendo de si lo que se
imputaron fueron ingresos o gastos respectivamente.

Se crea un nuevo registro, y como fecha de la operación de cierre se marca
el último día del ejercicio fiscal (normalmente el 31 de diciembre).

Hay que pulsar el botón *Regenerar líneas*, y entonces aparecerán las líneas
de factura en las que se ha indicado unas fechas con la parte que corresponde
a la periodificación calculada.

Por último, hay que pulsar en *Crear asiento contable* para que se realice
el asiento que realiza los movimientos de saldo contable correspondiente a las
periodificaciones.

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/189/8.0

Problemas conocidos / Hoja de ruta
==================================

* Contemplar los ingresos y gastos devengados, pero no vencidos
  (cobrados/pagados), que se corresponden con trabajos iniciados en el
  ejercicio que aún no han finalizado y no se han cobrado/pagado.
* Adaptar el cierre de ejercicio fiscal para las periodificaciones.

Gestión de errores
==================

Los errores/fallos se gestionan en `las incidencias de GitHub <https://github.com/OCA/
l10n-spain/issues>`_.
En caso de problemas, compruebe por favor si su incidencia ha sido ya
reportada. Si fue el primero en descubrirla, ayúdenos a solucionarla proveyendo
una detallada y bienvenida retroalimentación
`aquí <https://github.com/OCA/
l10n-spain/issues/new?body=m%f3dulo:%20
l10_es_accrual%0Aversi%f3n:%20
8.0%0A%0A**Pasos%20para%20reproducirlo**%0A-%20...%0A%0A**Comportamiento%20actual**%0A%0A**Comportamiento%20esperado**>`_.

Créditos
========

Contribuidores
--------------

* Pedro M. Baeza <pedro.baeza@serviciosbaeza.com>

Maintainer
----------

.. image:: http://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: http://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit http://odoo-community.org.
