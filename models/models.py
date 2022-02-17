# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

log = logging.getLogger(__name__)


class ReportModule(models.Model):
    _name = 'report.module'
    _description = 'Report Module'

    xpath_route = fields.Char(string='Ruta del xpath', default='')
    info_report_id = fields.One2many('info.report', 'report_module_id',
                                     string='Lineas de firmas')
    position = fields.Char(string='Position', default='after')
    views_qweb_id = fields.Many2one(
        'ir.ui.view', domain="[('type', '=', 'qweb')]", string='Vista')

    def create_report(self):
        received_list = []
        created_by_list = []
        client_list = []
        for obj in self.info_report_id:
            received_list.append(obj.received_by)
            created_by_list.append(obj.created_by)
            client_list.append(obj.client)

        self.env['ir.ui.view'].create({"name": f'{self.views_qweb_id.name}01',
                                       "type": self.views_qweb_id.type,
                                       "inherit_id": self.views_qweb_id.id,
                                       "model": self.views_qweb_id.model,
                                       "mode": 'extension',
                                       "priority": self.views_qweb_id.priority,
                                       "key": self.views_qweb_id.key,
                                       "xml_id": self.views_qweb_id.xml_id,
                                       "arch_base": f'''<?xml version="1.0"?>
                                       <data inherit_id="{self.views_qweb_id.xml_id}" priority="{self.views_qweb_id.priority}">
                                       <xpath expr="{self.xpath_route}" position="{self.position}">  
                                        <br/>
                                        <div>
                                          <table style="border:none display:
                                          flex !important;">
                                            <tr style="border:none !important;">
                                            <span
                                            t-foreach="{self.received_list}"
                                            t-as="i">
    <td style="border:none !important;padding-right:10px;">___________________________________________</td>
                                            </span>
                                            <span
                                            t-foreach="{self.created_by_list}"
                                            t-as="i">
<td style="border:none
!important;padding-right:10px;">___________________________________________</td>
</span>
                                            <span
                                            t-foreach="{self.client_list}"
                                            t-as="i">
<td style="border:none
!important;padding-right:10px;">___________________________________________</td>
</span>
                                            </tr>
                                            <tr class='text-center' style="border:none !important;">
                                              <span
                                              t-foreach="{self.received_list}"
                                              t-as="i">
                                                  <td style="border:none
                                                  !important;">Recibido por <t
                                                  t-esc="i"/></td>
                                              </span>
                                              <span
                                              t-foreach="{self.created_by_list}"
                                              t-as="i">
                                                  <td style="border:none
                                                  !important;">Autorizado por
                                                  <t t-esc="i"/></td>
                                              </span>
                                              <span
                                              t-foreach="{self.client_list}"
                                              t-as="i">
                                              <td style="border:none
                                              !important;">Cliente <t t-esc="i"/></td>
                                              </span>
                                            </tr>
                        
                                          </table>
                                        </div>
                                       </xpath>
                                       </data>'''
                                       })


class InfoReport(models.Model):
    _name = 'info.report'
    _description = 'Informacion del reporte'

    report_module_id = fields.Many2one('report.module')
    received_by = fields.Char(string='Recibido por:')
    created_by = fields.Char(string='Creado por:')
    client = fields.Char(string='Cliente:')
